from django.shortcuts import render
from .models import Layouts
# Create your views here.


def layouts(request):

    context = {
        'layouts': Layouts.objects.all()
    }

    return render(request, 'layouts/layouts.html', context)


def layouts_detail(request, slug):

    context = {
        'layout': Layouts.objects.get(slug=slug),
    }

    return render(request, 'layouts/layouts_detail.html', context)