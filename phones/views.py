from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        phones_list = phones.order_by('name')
    elif sort == 'min_price':
        phones_list = phones.order_by('price')
    elif sort == 'max_price':
        phones_list = phones.order_by('price').reverse()
    else:
        phones_list = phones
    context = {'phones': phones_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
