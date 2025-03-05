# AI-Based-Web-Scraping-Using-Django


# AI-Based Web Scraping Using Django

## 📌 Project Overview
This project is an **AI-powered web scraping tool** built using **Django, Selenium, and BeautifulSoup**. It extracts **headings and paragraphs** from any given website and classifies the content into predefined categories using **Google Gemini API**. The tool provides a **user-friendly web interface** where users can input a URL and receive structured data.

## 🚀 Features
- **Automated Web Scraping:** Extracts headings (H1, H2, H3) and meaningful paragraphs.
- **AI-Powered Categorization:** Uses Google Gemini API to classify the content.
- **User-Friendly Interface:** Simple form-based UI for URL input.
- **Django REST API Support:** Enables seamless integration with other applications.
- **Scalable & Secure:** Handles various website structures with error handling and security features.

---

## 📂 Project File Structure
```
AI_Scraper/
│-- scraper_project/           # Django project directory
│   │-- web_scraper/           # Django app directory
│   │   │-- migrations/        # Database migrations
│   │   │-- templates/         # HTML templates
│   │   │   │-- index.html     # Main UI for web scraping
│   │   │-- static/            # CSS and JS files
│   │   │   │-- style.css      # Styles for UI
│   │   │   │-- script.js      # JavaScript for interactivity
│   │   │-- views.py           # Backend logic for scraping
│   │   │-- urls.py            # Django URL routing
│   │   │-- models.py          # Database models (if needed)
│   │   │-- serializers.py     # DRF serializers
│   │-- settings.py            # Django settings
│   │-- urls.py                # Main project URL routing
│   │-- wsgi.py                # WSGI configuration
│   │-- asgi.py                # ASGI configuration
│-- requirements.txt           # Required dependencies
│-- manage.py                  # Django management script
│-- README.md                  # Project documentation
```

---

## 🛠 Setup & Installation
Follow these steps to set up the project on your local machine.

### 🔹 Prerequisites
Make sure you have the following installed:
- **Python 3.8+**
- **Django 4+**
- **Google Gemini API Key** (replace in `views.py`)
- **Selenium & ChromeDriver**
- **Git** (for version control)

### 🔹 1. Clone the Repository
```bash
git clone https://github.com/Shubhra55/AI-Based-Web-Scraping-Using-Django.git
cd AI-Based-Web-Scraping-Using-Django
```

### 🔹 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 🔹 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔹 4. Configure Google Gemini API Key
Edit `views.py` and replace `GEMINI_API_KEY` with your actual API key:
```python
GEMINI_API_KEY = "your_google_gemini_api_key_here"
```

### 🔹 5. Apply Migrations
```bash
python manage.py migrate
```

### 🔹 6. Run the Development Server
```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

---

## 🖥 Usage
1. **Enter a URL** in the input field.
2. **Click Scrape** to fetch data.
3. The tool will display **headings** and **categorized content**.

---

## 📜 API Endpoints
| Method | Endpoint   | Description |
|--------|-----------|-------------|
| `POST` | `/scrape/` | Accepts a JSON `{ "url": "website_url" }` and returns extracted data. |

Example Request:
```json
{
  "url": "https://books.toscrape.com/"
}
```

Example Response:
```json
{
  "message": "Scraping successful",
  "url": "https://books.toscrape.com/",
  "title": "All Products | Books to Scrape",
  "headings": ["All Products", "A Light in the...", "Tipping the Velvet"],
  "category": "E-commerce"
}
```

---

## 🛠 Deployment
To deploy the project on **Heroku**, **AWS**, or **any cloud platform**:
1. Install `gunicorn`:
   ```bash
   pip install gunicorn
   ```
2. Update `requirements.txt`:
   ```bash
   pip freeze > requirements.txt
   ```
3. Create a `Procfile`:
   ```
   web: gunicorn scraper_project.wsgi:application --log-file -
   ```
4. Deploy using GitHub Actions or manually.

---

## 📌 Contributing
Feel free to contribute by following these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a **Pull Request**.

---

## 📝 License
This project is licensed under the **MIT License**.

---

## 💬 Contact
For questions, reach out at **[Your Email or GitHub Issues](https://github.com/Shubhra55/AI-Based-Web-Scraping-Using-Django/issues)**.

�
