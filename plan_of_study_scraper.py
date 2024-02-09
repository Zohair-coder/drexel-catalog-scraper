from collections import defaultdict
import re
from helpers import send_request
from bs4 import BeautifulSoup


def scrape() -> dict:
    base_url = "https://catalog.drexel.edu"
    majors_url = base_url + "/majors"
    page = send_request(majors_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    main_div = soup.find("div", {"id": "textcontainer"})

    anchor_tags = main_div.find_all("a", href=True)
    anchor_tags = list(filter(lambda l: not l["href"].startswith("#") and l["href"] != "/accelerateddegreeprograms/" and l["href"] != "/certificates/", anchor_tags))

    data = {}
    for i, anchor_tag in enumerate(anchor_tags):
        link = base_url + anchor_tag["href"] + "#sampleplanofstudybstext"
        
        major = anchor_tag.text
        data[major] = scrape_page(link)
        print(f"({i+1}/{len(anchor_tags)}) Scraped {major}")
    
    return data
        

def scrape_page(url: str) -> dict:
    page = send_request(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    pattern = re.compile(r'sampleplans?ofstudy.*container')
    div_tag = soup.find('div', id=pattern)

    if not div_tag:
        pattern = re.compile(r'.*Plans? of Study.*', re.IGNORECASE)
        h2_tag = soup.find('h2', string=pattern)
        if not h2_tag:
            return {}
        div_tag = h2_tag.parent


    # Example: "4 year, 1 co-op"
    pattern = re.compile(r"(\w+[- ](?:Years?|YR)[.,]*\s*\w*\s*Co-?ops?\s*(?:\(?Fall\/Winter\)?|\(?Spring\/Summer\)?\s?Cycle)?)|((Fall Winter|Spring Summer) co-op cycle)", re.IGNORECASE)
    plan_names = div_tag.find_all(string=pattern)

    tables = soup.find_all("table", {"class": "sc_plangrid"})

    data = {}
    for i, table in enumerate(tables):
        table = tables[i]
        years = table.find_all("tr", {"class": "plangridyear"})
    
        years_data = defaultdict(list)
        for year in years:
            year_text = year.text.replace("&nbsp;", " ").replace("\u00a0", " ").strip()
            terms_element = year.find_next_sibling('tr', {'class': 'plangridterm'})
            terms_text = [t.text.replace("&nbsp;", " ").replace("\u00a0", " ").strip() for t in terms_element.find_all("th", {"class": "plangridtermhdr"})]
        
            term_data = defaultdict(list)
            for course_element in terms_element.next_siblings:
                if not course_element.name:
                    continue
                if "odd" not in course_element.attrs.get('class', []) and "even" not in course_element.attrs.get('class', []):
                    break
            
                count = 0
                for course_code in course_element.find_all("td"):
                    if "hourscol" in course_code.attrs.get('class', []):
                        continue
                    if "codecol" in course_code.attrs.get('class', []):
                        credits = course_code.find_next_sibling("td", {"class": "hourscol"})
                        term_data[terms_text[count]].append({
                        "course": course_code.text.replace("&nbsp;", " ").replace("\u00a0", " ").strip(),
                        "credits": credits.text.strip()
                    })
                    count += 1
        
            years_data[year_text] = term_data
        
        plan_name = plan_names[i].text if i < len(plan_names) else f"Plan {i+1}"
        data[plan_name.replace("&nbsp;", " ").replace("\u00a0", " ").strip()] = years_data
    
    return data