from django.shortcuts import render



def home(request):
    return render(request, 'home.html')


def services(request):
    return render(request, 'services.html')

def brief(request):
    return render(request, 'brief.html')

def jobs(request):
    return render(request, 'jobs.html')

def gallery(request):
    return render(request, 'gallery.html')