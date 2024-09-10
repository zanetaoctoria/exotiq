from django.shortcuts import render
from .models import Items

# def show_main(request):
#     items = Items.objects.all()  # Mengambil semua data dari model Items
#     context = {
#         'items': items
#     }
#     return render(request, 'main.html', context)

from django.shortcuts import render

def show_main(request):
    Items = [
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

    context = {
        'Items': Items
    }

    return render(request, "main.html", context)

# def show_main(request):
#     context = {
#         'name' : 'Lanvin Black Gold Pencil Cat Leather Shoulder Bag',
#         'price': '54.500.000',
#         'description': 'the Pencil Cat is embellished with a precious sculptural handle'
#     }

    # return render(request, "main.html", context)
# Create your views here.
