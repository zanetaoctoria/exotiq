import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, reverse   
from main.forms import ItemsEntryForm
from main.models import Items

# def show_main(request):
#     items = Items.objects.all()  # Mengambil semua data dari model Items
#     context = {
#         'items': items
#     }
#     return render(request, 'main.html', context)

from django.shortcuts import render

@login_required(login_url='/login')

def show_main(request):
    item_entries = Items.objects.filter(user=request.user)

    
    # default_items  = [
    #     {
    #         'name' : 'Lanvin Black Gold Pencil Cat Leather Shoulder Bag',
    #         'price': '54.500.000',
    #         'description': 'the Pencil Cat is embellished with a precious sculptural handle'
    #     },

    #     {
    #         'name' : 'Schiaparelli Saturn Bag',
    #         'price': '100.000.000',
    #         'description': 'Exclusively made'
    #     },

    #     {
    #         'name' : 'Dolce and Gabbana Heart School Backpack',
    #         'price': '250.000.000',
    #         'description': 'Absolutely stunning, 100% Authentic, brand new with tags Dolce & Gabbana Women’s Bag'
    #     }
    # ]
    
    context = {
        'items': item_entries,
        'name': request.user.username,
        'last_login': request.COOKIES['last_login'],
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
        Items = form.save(commit=False)
        Items.user = request.user
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_items_entry.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_items(request, id):
    # Get item entry berdasarkan id
    item = Items.objects.get(pk = id)

    # Set item entry sebagai instance dari form
    form = ItemsEntryForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_items.html", context)

def delete_items(request, id):
    # Get item berdasarkan id
    item = Items.objects.get(pk = id)
    # Hapus item
    item.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))


