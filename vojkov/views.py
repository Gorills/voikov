from django.shortcuts import render


from .models import DocCat
# Create your views here.
def home(request):

    return render(request, 'vojkov/home.html')


def dok(request):

    context = {
        'docs': DocCat.objects.all(),
    }


    return render(request, 'vojkov/dokumentatsiya.html', context)