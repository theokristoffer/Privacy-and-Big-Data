from django.http import HttpResponse
from django.contrib.sitemaps import Sitemap


def index(request):
    return HttpResponse("Sitemap Index Placeholder")

def sitemap(request, section=None):
    return HttpResponse(f"Sitemap Section Placeholder: {section}")

