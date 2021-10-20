from django.shortcuts import render


from .models import DocCat, Page, HomeBlock
# Create your views here.
def home(request):

    context = {
        'blocks': HomeBlock.objects.all(),
        
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