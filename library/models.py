from django.db import models

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street}, {self.city}"


class Library(models.Model):
    name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    books = models.ManyToManyField("book_outlet.Book")

    class Meta:
        verbose_name_plural = "Libraries"

    def __str__(self):
        return f"{self.name}"
