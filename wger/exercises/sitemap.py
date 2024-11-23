from django.contrib.sitemaps import Sitemap
from .models import Exercise  # Adjust this based on your actual Exercise model

class ExercisesSitemap(Sitemap):
    """
    Sitemap for exercises.
    """
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Exercise.objects.all()

    def lastmod(self, obj):
        return obj.updated  # Assuming the Exercise model has an `updated` field

