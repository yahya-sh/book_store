from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    is_best_seller = models.BooleanField(default=False)
    slug = models.SlugField(db_index=True, unique=True)


    def get_absolute_url(self):
        return reverse("detail", args=[self.slug])
    
    def __str__(self):
        return self.title
    
    
