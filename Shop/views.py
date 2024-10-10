from django.shortcuts import render

from Shop.models import Header, Mobile, Categories,Brands


# Create your views here.


def index(request):
    index_header = Header.objects.filter(active=False)
    active_object = Header.objects.filter(active=True)
    special_opportunity = Mobile.objects.filter(Special_opportunity=True)
    mobile = Mobile.objects.all()

    return render(request, 'Shop/index.html',
                  {'header': index_header, 'active_obj': active_object, 'special': special_opportunity , 'mobile':mobile})


def Mobile_Category(request):
    Brand = Brands.objects.all()
    return render(request, 'Shop/mobile_category.html', {'Brand': Brand})

def Mobile_Show(request , s):
    Brand = Brands.objects.get(slug=s)
    mobile = Mobile.objects.filter(Brand = Brand)
    return render(request, 'Shop/mobile_index.html', {'Brand': Brand, 'mobile': mobile})
