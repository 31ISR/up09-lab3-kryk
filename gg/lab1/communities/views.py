from django.shortcuts import render
from .models import Communitie

def comms_list(request):
    comms = Communitie.objects.all().order_by('-date')
    return render(request, 'comms/comms_list.html', {'comms': comms})

def comm_page(request, slug):
    comm = Communitie.objects.get(slug=slug)
    return render(request, 'comms/comm_page.html', {'comm': comm})