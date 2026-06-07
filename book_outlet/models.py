from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT, related_name='books')
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
