
# El País Opinion Scraper + Cross-Browser Testing by Arnav Thakoor

Task 1 Requirements: 

1. Visit the website El País, a Spanish news outlet.
  - Ensure that the website's text is displayed in Spanish.
2. Scrape Articles from the Opinion Section:
  - Navigate to the Opinion section of the website.
  - Fetch the first five articles in this section.
  - Print the title and content of each article in Spanish.
  - If available, download and save the cover image of each article to your local machine.
3. Translate Article Headers:
  - Use a translation API of your choice, such as:
  - Google Translate API
  - Rapid Translate Multi Traduction API
  - Translate the title of each article to English.
  - Print the translated headers.
4. Analyze Translated Headers:
  - From the translated headers, identify any words that are repeated more than twice across all headers combined.
  - Print each repeated word along with the count of its occurrences.
5. Cross-Browser Testing:
  - Run the solution locally to verify functionality.
  - Once validated, execute the solution on BrowserStack across 5 parallel threads, testing across a combination of desktop and mobile browsers.


Project Details: 

This project was built as a full end-to-end automation task.  
It scrapes the first 5 opinion articles from the El País website, translates their headlines into English, downloads their headline images, and also performs a small analysis on the translated titles.

After validating everything locally, the project is also tested on BrowserStack across multiple desktop and mobile browsers.

---

## What the scraper does (Phase 1–4)

1. Opens `elpais.com`, accepts the cookie popup automatically.
2. Navigates to the Opinión section.
3. Extracts the first 5 valid article links on the page.
4. For each article:
   - Scrapes the Spanish title  
   - Translates it to English (Google Translate API endpoint)  
   - Scrapes the full Spanish content  
   - Downloads the main headline image in high resolution  
5. After all 5 articles are collected, the script analyzes the English titles and reports any words that appear more than twice.

The downloaded images are saved inside the `article_images` folder.

---

## Cross-Browser Testing (Phase 5)

A separate script, `run_browserstack.py`, is used to test that the El País homepage loads correctly on multiple real browsers and devices using BrowserStack Automate.

The test runs on 5 parallel threads:

- Chrome on Windows  
- Firefox on Windows  
- Safari on macOS  
- iPhone 14  
- Samsung Galaxy S23  

Each session simply loads the homepage and prints the title to confirm everything is working.

Your BrowserStack access key is not included in the repo (added to `.gitignore`).

---

## Folder structure
elpais_scraper/
│
├── scrapper.py
├── run_browserstack.py
├── requirements.txt
├── README.md
├── sample_output.txt
├── .gitignore
└── article_images/


## How to run

Install dependencies:

```
pip install -r requirements.txt
```

Run the scraper:
```
python scrapper.py
```

Run BrowserStack cross-browser testing:
```
python run_browserstack.py
```

---

## Notes

- The project works using only free and open APIs.
- All translations are done using the public Google Translate endpoint.
- No API keys are included in the repo.
- Built and tested on Python 3.12.10.
  

## TASK CONCLUSION:
I was able to complete and test all the above mentioend requirements.
Overall, it was interesting to build this project, I learnt a lot about crawling websites and analyzing the fetched data.
Thank you BrowserStack Team !


