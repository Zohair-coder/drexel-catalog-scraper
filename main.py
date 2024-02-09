import requests
from bs4 import BeautifulSoup
import json
from collections import defaultdict
import re

def main():
    url = "https://catalog.drexel.edu/undergraduate/schoolofeconomics/behavioraleconomicsbusinessandorganizations/#sampleplanofstudytext"
    data = scrape(url)
    with open('data.json', 'w') as f:
        f.write(json.dumps(data, indent=4))

def scrape(url: str) -> dict:
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    pattern = re.compile(r'sampleplans?ofstudy.*container')
    div_tag = soup.find('div', id=pattern)

    if not div_tag:
        div_tag = soup.find('h2', text="Sample Plan of Study").parent


    pattern = re.compile(r'\w+[ -](Year|YR)[.,]*? \w+ Co-?ops?\s*((in )?(\(?Fall/Winter\)?|\(?Spring/Summer\)?))?$', re.IGNORECASE)
    plan_names = div_tag.find_all(string=pattern)

    with open("debug.html", "w") as f:
        f.write(div_tag.prettify())

    tables = soup.find_all("table", {"class": "sc_plangrid"})

    data = {}
    for i, plan_name in enumerate(plan_names):
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
        
        data[plan_name.text.replace("&nbsp;", " ").replace("\u00a0", " ").strip()] = years_data
    
    return data


if __name__ == "__main__":
    main()