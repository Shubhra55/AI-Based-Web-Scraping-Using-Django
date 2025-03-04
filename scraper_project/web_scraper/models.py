from django.db import models

# Create your models here.

from django.db import models

class ScrapedWebsite(models.Model):
    url = models.URLField(unique=True)  # Website URL
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    headings = models.TextField()  # Store headings as JSON
    paragraphs = models.TextField()  # Store paragraphs as JSON
    scraped_at = models.DateTimeField(auto_now_add=True)  # Timestamp when scraped

    def __str__(self):
        return f"{self.title} - {self.category}"
