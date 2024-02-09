from collections import defaultdict
import re
import requests
from bs4 import BeautifulSoup

def scrape(url: str) -> dict:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    pattern = re.compile(r'sampleplans?ofstudy.*container')
    div_tag = soup.find('div', id=pattern)

    if not div_tag:
        pattern = re.compile(r'.*Plans? of Study.*', re.IGNORECASE)
        div_tag = soup.find('h2', string=pattern).parent


    pattern = re.compile(r"(\w+[ -](Years?|YR)[.,]*?\s*\w*\s*Co-?ops?\s*((in )?(\(?Fall\/Winter\)?|\(?Spring\/Summer\)?))?\s?(Cycle)?$)|((Fall Winter|Spring Summer) co-op cycle)", re.IGNORECASE)
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