from django.shortcuts import render, redirect
from .models import Page


def list(request):
    context = {
        "pages":Page.objects.all()
    }
    return render(request, 'list.html', context)


def detail(request, page_id):
    context = {
        "pages": Page.objects.get(id=page_id)
    }
    return render(request, 'detail.html', context)
# Create your views here.
