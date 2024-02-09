import json

import plan_of_study_scraper

def main():
    url = "https://catalog.drexel.edu/undergraduate/collegeofcomputingandinformatics/computingandsecuritytechnology/#sampleplansofstudytext"
    data = plan_of_study_scraper.scrape(url)
    with open('data.json', 'w') as f:
        f.write(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()