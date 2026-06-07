from django.contrib import admin
from . import models
from django.utils.translation import gettext as _
# Register your models here.


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
    list_display = ("__str__", "author", "rating", "is_best_seller")
    readonly_fields = ("slug",)
    list_filter = (
        "is_best_seller",
        RatingFilter,
    )


# admin.site.register(models.Book, BookAdmin)
