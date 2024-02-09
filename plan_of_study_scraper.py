from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
from helpers import send_request
from bs4 import BeautifulSoup
import os


def scrape() -> dict:
    base_url = "https://catalog.drexel.edu"
    majors_url = base_url + "/majors"
    page = send_request(majors_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    main_div = soup.find("div", {"id": "textcontainer"})

    anchor_tags = main_div.find_all("a", href=True)
    anchor_tags = list(filter(lambda l: not l["href"].startswith("#") and l["href"] != "/accelerateddegreeprograms/" and l["href"] != "/certificates/", anchor_tags))

    data = {}
    futures = {}
    num_cores = os.cpu_count()

    with ThreadPoolExecutor(max_workers=num_cores) as executor:
        for anchor_tag in anchor_tags:
            link = base_url + anchor_tag["href"] + "#sampleplanofstudybstext"
            major = anchor_tag.text
            future = executor.submit(scrape_page, link)
            futures[future] = major
        
        for future in as_completed(futures):
            major = futures[future]
            
            try:
                data[major] = future.result()
                print(f"Scraped {major}")
            except Exception as e:
                print(f"Failed to scrape {major}: {e}")
    
    return data
        

def scrape_page(url: str) -> dict:
    page = send_request(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    tables = soup.find_all("table", {"class": "sc_plangrid"})

    data = {}
    for i, table in enumerate(tables):
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
        
        plan_name = f"Plan {i+1}"
        data[plan_name] = years_data
    
    return data