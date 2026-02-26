
---

# El País Opinion Scraper + Cross-Browser Testing

### by **Arnav Thakoor**

---

## Task Requirements

### 1. Visit the website El País

* Open the website in Spanish and ensure the text is correctly displayed.

### 2. Scrape Articles from the Opinion Section

* Navigate to the Opinión section.
* Fetch the first five articles.
* Print the title and content of each article in Spanish.
* Download and save each article’s cover image (if available).

### 3. Translate Article Headers

Use any translation API (Google Translate endpoint used here):

* Translate each article title to English.
* Print the translated titles.

### 4. Analyze Translated Headers

* Combine all translated titles.
* Identify repeated words appearing more than twice.
* Print each such word with its count.

### 5. Cross-Browser Testing

* Run the scraper locally first.
* Then test the solution on BrowserStack using 5 parallel threads across desktop and mobile browsers.

---

## Project Overview

This project performs a complete end-to-end web automation flow. It visits El País, extracts 5 opinion articles, translates their titles, downloads headline images, and performs a word frequency analysis on translated headers.

Once verified locally, the scraper is also validated through BrowserStack Automate on multiple real browsers and devices.

---

## What the Scraper Does (Phase 1–4)

1. Opens `elpais.com` and accepts the cookie popup automatically.
2. Navigates to the Opinión section.
3. Scrapes the first 5 valid article URLs.
4. For each article:

   * Scrapes the Spanish title
   * Translates it to English
   * Scrapes the full Spanish content
   * Downloads the main headline image in high resolution
5. After all articles are processed, the script analyzes the translated English titles and prints any words that appear more than twice.

All downloaded images are saved in the `article_images` folder.

---

## Cross-Browser Testing (Phase 5)

The script `run_browserstack.py` runs the homepage test across real devices and browsers using BrowserStack Automate.

The tests run in parallel on:

* Chrome on Windows
* Firefox on Windows
* Safari on macOS
* iPhone 14
* Samsung Galaxy S23

Each test loads the homepage and prints the page title to confirm successful rendering.

BrowserStack credentials are excluded using `.gitignore`.

---

## Folder Structure

```
elpais_scraper/
│
├── scrapper.py
├── run_browserstack.py
├── requirements.txt
├── README.md
├── sample_output.txt
├── .gitignore
└── article_images/
```

---

## How to Run

### Install dependencies:

```
pip install -r requirements.txt
```

### Run the scraper:

```
python scrapper.py
```

### Run BrowserStack cross-browser testing:

```
python run_browserstack.py
```

---

## Notes

* The project uses only free and open APIs.
* Translations are performed through the public Google Translate endpoint.
* No API keys are included in the repository.
* Built and tested on Python 3.12.10.

---

## Task Conclusion

All required tasks were fully completed and tested.
This was a meaningful project, and I learned a lot about scraping dynamic websites, translation automation, and cross-browser validation.

Thank you BrowserStack Team!

---
