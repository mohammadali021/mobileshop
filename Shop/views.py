from django.shortcuts import render

from Shop.models import Header


# Create your views here.


def index(request):
    index_header = Header.objects.filter(active=False)
    active_object = Header.objects.filter(active=True)
    return render(request , 'Shop/index.html' , {'header':index_header , 'active_obj' : active_object})