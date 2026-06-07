from django.shortcuts import render, get_object_or_404
from . import models
from django.db.models import Avg


# Create your views here.
def index(request):
    book_list = models.Book.objects.all().order_by('title')
    total_count = book_list.count()
    rating_avg = book_list.aggregate(Avg("rating")).get('rating__avg')
    return render(
        request,
        "book_outlet/index.html",
        {
            "book_list": book_list,
            "total_count": total_count,
            "rating_avg": rating_avg,
        },
    )


def detail(request, slug):
    book = get_object_or_404(models.Book, slug=slug)
    return render(request, "book_outlet/detail.html", {"book": book})
