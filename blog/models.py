from django.db import models
from django.utils.text import slugify
# Create your models here.
class Artikel(models.Model):
    judul = models.CharField(max_length=50)
    isi = models.TextField()
    kategori = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, editable=False)
    publish = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{}. {} | {}".format(self.id, self.judul, self.kategori)
    
    def save(self):
        self.slug = slugify(self.judul)
        super().save()