import json
import requests
import time
from django.http import JsonResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from django.views.decorators.csrf import csrf_exempt  # Import CSRF exemption

# Replace with your actual Gemini API Key
GEMINI_API_KEY = "AIzaSyDhDTWXi3I0smmkL_Rf1CCrpdo5NTZEf3E"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

def home(request):
    """Renders the index page."""
    return render(request, "index.html")  # Ensure "index.html" exists in templates folder

@csrf_exempt  # Disable CSRF protection for this view
def scrape(request):
    """Handles web scraping requests."""
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            website_url = data.get("url", "").strip()

            if not website_url:
                return JsonResponse({"error": "Invalid URL"}, status=400)

            # Scrape webpage content
            scraped_data = scrape_website(website_url)
            if not scraped_data:
                return JsonResponse({"error": "Failed to scrape content"}, status=500)

            # Categorize content using Gemini API
            category = categorize_content(scraped_data)

            # Ensure no unnecessary data is shown
            if scraped_data["headings"] and not scraped_data["paragraphs"]:
                scraped_data["paragraphs"] = None

            return JsonResponse({
                "message": "Scraping successful",
                "url": website_url,
                "title": scraped_data["title"],
                "headings": scraped_data["headings"],
                "paragraphs": scraped_data["paragraphs"],
                "category": category
            })
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)

def scrape_website(url):
    """Scrapes webpage and extracts relevant content."""
    try:
        # Set up Selenium with headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        )

        # Start WebDriver
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=chrome_options
        )
        driver.get(url)
        time.sleep(3)  # Allow JavaScript to load

        # Extract page source
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()

        # Extract title, headings, and paragraphs
        title = soup.title.string if soup.title else "No Title Found"
        headings = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])]
        paragraphs = [
            p.get_text(strip=True) for p in soup.find_all("p") if len(p.get_text(strip=True)) > 50
        ][:100]

        # If only headings exist, clear paragraphs
        if headings and not any(paragraphs):
            paragraphs = None

        return {
            "title": title,
            "headings": headings,
            "paragraphs": paragraphs,
        }

    except Exception as e:
        print("❌ Scraping Error:", str(e))
        return None

def categorize_content(scraped_data):
    """Uses Gemini API to classify scraped content into categories"""
    prompt = f"""
    Given the following webpage content, classify it into one of these categories: 
    ["E-commerce", "News", "Entertainment", "Education", "Finance", "Technology", "Travel & Hospitality", "Others"]

    - **Title**: {scraped_data['title']}
    - **Headings**: {', '.join(scraped_data['headings'])}
    - **Paragraphs**: {', '.join(scraped_data['paragraphs']) if scraped_data['paragraphs'] else 'N/A'}

    Ensure the response contains only the **category name** without extra text.
    """

    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
        response_data = response.json()

        # Extract category from Gemini's response
        if "candidates" in response_data and response_data["candidates"]:
            category = response_data["candidates"][0]["content"]["parts"][0]["text"].strip()
            return category if category in [
                "E-commerce",
                "News",
                "Entertainment",
                "Education",
                "Finance",
                "Technology",
                "Travel & Hospitality",
                "Others",
            ] else "Others"
    except Exception as e:
        print("❌ Error with Gemini API:", str(e))

    return "Others"
