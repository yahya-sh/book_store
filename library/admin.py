from django.contrib import admin
from django.urls import reverse
from . import models
from django.utils.html import format_html
from django.utils.translation import gettext as _

# Register your models here.


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city")


@admin.register(models.Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("__str__", "address_link")

    def address_link(self, obj):
        url = reverse('admin:library_address_change', args=[obj.address.pk])
        return format_html("<a href={}>{}</a>", url, obj.address)
    
    address_link.short_description = _("Address")
