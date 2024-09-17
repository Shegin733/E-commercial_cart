import operator
from django.shortcuts import render, get_object_or_404
from .models import Categ,product
from .models import *
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from django.urls import reverse


# Create your views here.
def home(request, c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
      c_page = get_object_or_404(Categ, slug=c_slug)
      prodt = product.objects.filter(category=c_page, available=True)
    else:
      prodt = product.objects.all().filter(available=True)
    categ = Categ.objects.all()

    paginator = Paginator(prodt, 2)
    try:
         page=int(request.GET.get('page','1'))
    except:
         page=1
    try:
         pro=paginator.page(page)
    except(EmptyPage,InvalidPage):
         pro=paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'pr': prodt, 'ct': categ,'pg':pro})


# Create your views here.
def detailing(request,c_slug,product_slug):
    try:
        prodt = product.objects.get(category__slug=c_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'item.html', {'pr': prodt})




def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'qr': query, 'pr': prod})
