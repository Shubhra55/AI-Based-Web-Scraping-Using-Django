from bs4 import BeautifulSoup
import requests

def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.title.string if soup.title else "No title found"
        headings = [h.get_text() for h in soup.find_all(["h1", "h2", "h3"])]
        paragraphs = [p.get_text() for p in soup.find_all("p")]

        return {"title": title, "headings": headings, "paragraphs": paragraphs}
    except Exception as e:
        return {"error": str(e)}
