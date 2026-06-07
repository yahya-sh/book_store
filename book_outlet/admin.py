from django.contrib import admin
from django.urls import reverse
from . import models
from django.utils.translation import gettext as _
from django.utils.html import format_html

# Register your models here.
admin.site.register(models.Author)


class RatingFilter(admin.SimpleListFilter):
    parameter_name = "rating_level"
    title = _("Rating Ranges")

    def lookups(self, request, model_admin):
        return [
            ("bad", _("Bad Rating (1 < 3)")),
            ("medium", _("Medium Rating (3 < 4)")),
            ("good", _("Good Rating (4 < 5)")),
            ("perfect", _("Perfect Rating (5)")),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value == "bad":
            return queryset.filter(
                rating__lt=3,
            )
        if value == "medium":
            return queryset.filter(
                rating__gte=3,
                rating__lt=4,
            )
        if value == "good":
            return queryset.filter(
                rating__gte=4,
                rating__lt=5,
            )
        if value == "perfect":
            return queryset.filter(
                rating__gte=5,
            )


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("__str__", "author_link", "rating", "is_best_seller")
    list_filter = (
        "is_best_seller",
        RatingFilter,
        "author",
    )
    prepopulated_fields = {
        "slug": ("title",),
    }

    def author_link(self, obj):
        url = reverse(
            "admin:book_outlet_author_change",
            args=[obj.author.pk]
        )
        return format_html(
            '<a href="{}">{}</a>',
            url,
            obj.author,
        )

    author_link.short_description = "Author"


# admin.site.register(models.Book, BookAdmin)
