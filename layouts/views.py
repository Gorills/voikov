from django.shortcuts import render


from .models import Layouts, Room
from vojkov.models import Ipoteka, Banks, HodBlockImages
# Create your views here.


def layouts(request):

    context = {
        'layouts': Layouts.objects.filter(activ=True),
        
    }

    return render(request, 'layouts/layouts.html', context)


def layouts_detail(request, slug):

    context = {
        'layouts': Layouts.objects.all().order_by('-id'),
        'hods': HodBlockImages.objects.all().order_by('-id')[:4],
        'layout': Layouts.objects.get(slug=slug),
        'ipoteks': Ipoteka.objects.all().order_by('id'),
        'banks': Banks.objects.all().order_by('order'),
    }

    return render(request, 'layouts/layouts_detail.html', context)



def room(request, slug):

    context = {
        'room': Room.objects.get(slug=slug)
    }

    return render(request, 'layouts/room.html', context)