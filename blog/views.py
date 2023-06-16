from django.shortcuts import render
from .models import Artikel

# Create your views here.
def index(request):
    allkategori = Artikel.objects.values("kategori").distinct()
    artikel = Artikel.objects.all()
    context = {
        "heading": "Blog Page",
        "artikels": artikel, 
        "allkategori": allkategori,
    }
    return render(request, "blog/index.html", context)

def kategori(request, kategoriInput):
    postkategori = Artikel.objects.filter(kategori=kategoriInput)
    context = {
        "heading": "Post Per Kategori",
        "postkategori": postkategori,
    }
    return render(request, "blog/kategori.html", context)

def details(request, slugInput):
    detail = Artikel.objects.get(slug=slugInput)
    context = {
        "heading": "Detail Postingan",
        "details": detail,
    }
    return render(request, "blog/detail.html", context)
