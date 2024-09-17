from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect   
from main.forms import ItemsEntryForm
from main.models import Items

# def show_main(request):
#     items = Items.objects.all()  # Mengambil semua data dari model Items
#     context = {
#         'items': items
#     }
#     return render(request, 'main.html', context)

from django.shortcuts import render


def show_main(request):
    item_entries = Items.objects.all()
    
    default_items  = [
        {
            'name' : 'Lanvin Black Gold Pencil Cat Leather Shoulder Bag',
            'price': '54.500.000',
            'description': 'the Pencil Cat is embellished with a precious sculptural handle'
        },

        {
            'name' : 'Schiaparelli Saturn Bag',
            'price': '100.000.000',
            'description': 'Exclusively made'
        },

        {
            'name' : 'Dolce and Gabbana Heart School Backpack',
            'price': '250.000.000',
            'description': 'Absolutely stunning, 100% Authentic, brand new with tags Dolce & Gabbana Women’s Bag'
        }
    ]

    # new_candy = []
    # for candy in candy_entries:
    #     new_candy.append({'name': candy.name, 'price': candy.price, 'description': candy.description, 'sweetness': candy.sweetness})
    # all_candies = default_candies + new_candy

    new_items = []
    for product in item_entries:
        new_items.append ({'name' : product.name, 'price' : product.price, 'description' : product.description})
    all_items = default_items  + new_items
    
    context = {
        'items': all_items,
    }

    return render(request, "main.html", context)

def show_xml(request):
    data = Items.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Items.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Items.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Items.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_items_entry(request):
    form = ItemsEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_items_entry.html", context)


# def show_main(request):
#     context = {
#         'name' : 'Lanvin Black Gold Pencil Cat Leather Shoulder Bag',
#         'price': '54.500.000',
#         'description': 'the Pencil Cat is embellished with a precious sculptural handle'
#     }

    # return render(request, "main.html", context)
# Create your views here.
