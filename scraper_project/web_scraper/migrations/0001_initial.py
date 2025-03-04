# Generated by Django 5.1.6 on 2025-03-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedWebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=100)),
                ('headings', models.TextField()),
                ('paragraphs', models.TextField()),
                ('scraped_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
