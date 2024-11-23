from django.contrib.sitemaps import Sitemap
from .models import Ingredient  # Adjust to your actual model

class NutritionSitemap(Sitemap):
    """
    Sitemap for nutrition items.
    """
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Ingredient.objects.all()  # Replace `Ingredient` with your actual model

    def lastmod(self, obj):
        return obj.updated  # Replace `updated` with the actual field in your model

