from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def index(request):
    book_list = models.Book.objects.all()
    return render(
        request,
        "book_outlet/index.html",
        {
            "book_list": book_list,
        },
    )


def detail(request, slug):
    book = get_object_or_404(models.Book, slug=slug)
    return render(request, "book_outlet/detail.html", {"book": book})
