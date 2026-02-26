import os
import time
import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from collections import Counter
import re


# -----------------------------------------
# Translation Function (Google Translate API)
# -----------------------------------------
def translate_to_english(text):
    try:
        url = "https://translate.googleapis.com/translate_a/single"
        params = {
            "client": "gtx",
            "sl": "es",
            "tl": "en",
            "dt": "t",
            "q": text
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        return data[0][0][0]   # return translated text
    except Exception as e:
        print(f"Translation error: {e}")
        return ""


# -----------------------------------------
# Setup
# -----------------------------------------
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

BASE_URL = "https://elpais.com/"
OPINION_URL = "https://elpais.com/opinion/"
IMAGE_DIR = "article_images"

os.makedirs(IMAGE_DIR, exist_ok=True)


# -----------------------------------------
# Step 1 – Accept cookies
# -----------------------------------------
driver.get(BASE_URL)
time.sleep(4)

try:
    accept_btn = driver.find_element(By.CSS_SELECTOR, "#didomi-notice-agree-button")
    driver.execute_script("arguments[0].click();", accept_btn)
    time.sleep(2)
    print("✓ Cookie popup accepted on homepage.")
except:
    print("❗ Cookie popup not visible or already accepted.")


# -----------------------------------------
# Step 2 – Go to Opinión section
# -----------------------------------------
driver.get(OPINION_URL)
time.sleep(3)
print("Navigated to Opinión section.")


# -----------------------------------------
# Step 3 – Scrape the first 5 real article links
# -----------------------------------------
articles = driver.find_elements(By.CSS_SELECTOR, "article a")[:20]
article_links = []

for a in articles:
    link = a.get_attribute("href")
    if not link:
        continue

    # Only accept real articles: URLs with date (/20xx/)
    if "/opinion/" in link and "/20" in link:
        if link not in article_links:
            article_links.append(link)

    if len(article_links) == 5:
        break

print(f"Found {len(article_links)} valid Opinion article links.\n")


# -----------------------------------------
# Helper: Download image
# -----------------------------------------
def download_image(url, filename):
    try:
        img_data = requests.get(url, timeout=10).content
        with open(os.path.join(IMAGE_DIR, filename), "wb") as f:
            f.write(img_data)
        print(f"✓ Image saved: {filename}")
    except Exception as e:
        print(f"Error saving image: {e}")


# -----------------------------------------
# Step 4 – Scrape Title, Translation, Content, Image
# -----------------------------------------
scraped_articles = []

for idx, link in enumerate(article_links, 1):
    print("\n==============================")
    print(f"  ARTICLE {idx}")
    print("==============================")
    print(f"URL: {link}")

    driver.get(link)
    time.sleep(4)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Title
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "No title found"

    print("\n--- TITLE (Spanish) ---")
    print(title)

    # Translate title
    translated_title = translate_to_english(title)

    print("\n--- TITLE (English) ---")
    print(translated_title)

    # Content
    paragraphs = soup.find_all("p")
    content = "\n".join([p.get_text(strip=True) for p in paragraphs])

    print("\n--- CONTENT (Spanish) ---")
    print(content[:600] + "...\n")

    # Image extraction
    img_tag = soup.select_one("img._re, img.a_m-h")
    img_url = None

    if img_tag:
        if img_tag.get("srcset"):
            srcset = img_tag["srcset"].split(",")
            last_item = srcset[-1].strip().split(" ")[0]
            img_url = last_item
        else:
            img_url = img_tag.get("src")

        if img_url:
            img_filename = f"article_{idx}.jpg"
            download_image(img_url, img_filename)
            print(f"✓ Headline image saved: {img_filename}")
    else:
        print("No headline image found.")

    scraped_articles.append({
        "title_es": title,
        "title_en": translated_title,
        "content": content
    })


# -----------------------------------------
# PHASE 4 – Analyze translated titles
# -----------------------------------------
print("\n==============================")
print(" PHASE 4: TRANSLATED TITLE WORD ANALYSIS")
print("==============================\n")

all_words = []

for art in scraped_articles:
    words = re.findall(r"[A-Za-z]+", art["title_en"].lower())
    all_words.extend(words)

counter = Counter(all_words)

# Only words appearing more than twice
repeated_words = {w: c for w, c in counter.items() if c > 2}

# Print results
if repeated_words:
    print(f"{'WORD':<15}{'COUNT'}")
    print("-" * 25)
    for word, count in repeated_words.items():
        print(f"{word:<15}{count}")
else:
    print("No repeated words (>2 occurrences) found.")


driver.quit()
print("\nScraping completed successfully.\n")