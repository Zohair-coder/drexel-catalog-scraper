import json

import plan_of_study_scraper

def main():
    data = plan_of_study_scraper.scrape()

    with open('data.json', 'w') as f:
        f.write(json.dumps(data, indent=4))
    
    print("Data written to data.json")

if __name__ == "__main__":
    main()