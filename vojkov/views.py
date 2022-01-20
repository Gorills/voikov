from django.shortcuts import render


from .models import DocCat, Page, HomeBlock, HodBlock, Ipoteka, Banks
from layouts.models import Room
# Create your views here.
def home(request):

    context = {
        'blocks': HomeBlock.objects.all().order_by('id'),
        'rooms': Room.objects.all()
        
    }


    return render(request, 'vojkov/home.html', context)


def dok(request):

    context = {
        'docs': DocCat.objects.all(),
    }


    return render(request, 'vojkov/dokumentatsiya.html', context)


def page(request, slug):
    context = {
        'page': Page.objects.get(slug=slug),
    }


    return render(request, 'vojkov/page.html', context)


def hod_stroitelstva(request):

    context = {
        'blocks': HodBlock.objects.all().order_by('-id'),

    }

    return render(request, 'vojkov/hod.html', context)


def ipoteka(request):

    context = {
        'ipoteks': Ipoteka.objects.all().order_by('id'),
        'banks': Banks.objects.all().order_by('id'),
    }
    return render(request, 'vojkov/ipoteka.html', context)