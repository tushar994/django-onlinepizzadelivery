from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Item,Cart,ItemInCart
# Create your views here.
def index(request):
    username = request.user.username
    try:
        cur_cart = Cart.objects.get(user = username)
    except:
        cur_cart = Cart(user = username)
        cur_cart.save()
        cur_cart.items.clear()
    context = {
        'list_of_items' : Item.objects.all(),
    }
    return render(request,'browse.html',context)

def add_to_cart(request, item):
    print((item))
    username = request.user.username
    current_cart = Cart.objects.get(user=username)
    print(current_cart)
    item = Item.objects.get(id = item)
    name = item.name
    try:
        print('1')
        cur_item = current_cart.items.get(name= name)
    except:
        print('2')
        cur_item = ItemInCart(name = item.name, price = item.price, frequency = 1)
        cur_item.save()
        current_cart.items.add(cur_item)
    else:
        print('3')
        cur_item = current_cart.items.get(name= name)
        cur_item2 = ItemInCart(name = item.name, price = item.price, frequency = cur_item.frequency+1)
        cur_item2.save()
        cur_item.delete()
        print(current_cart.items.all())
        current_cart.items.add(cur_item2)
    
    objects = current_cart.items.all()
    sum =0 
    for stuff in objects:
        sum+= stuff.price*stuff.frequency
    
    context = {
        'objects' : current_cart.items.all(),
        'total' : sum,
    }

    return render(request, "cart.html", context)

def Order(request):
    username = request.user.username
    cur_cart = Cart.objects.get(user = username)
    cur_cart.items.clear()  
    context = {
        'objects' : cur_cart.items.all(),
        'ordered' : "Ordered Successfully!"
    }

    return render(request, "cart.html", context)

def delete_object(request,item):
    username = request.user.username
    current_cart = Cart.objects.get(user=username)
    cur_item = current_cart.items.get(id= item)
    if cur_item.frequency==1:
        cur_item.delete()
    else:
        cur_item2 = ItemInCart(name = cur_item.name, price = cur_item.price, frequency = cur_item.frequency-1)
        cur_item2.save()
        cur_item.delete()
        print(current_cart.items.all())
        current_cart.items.add(cur_item2)
    objects = current_cart.items.all()
    sum =0 
    for stuff in objects:
        sum+= stuff.price*stuff.frequency
    
    context = {
        'objects' : current_cart.items.all(),
        'total' : sum,
    }

    return render(request, "cart.html", context)

