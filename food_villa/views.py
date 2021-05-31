from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import json
from collections import Counter
from .models import Item, Order, Quantity


# Create your views here.

def login_view(request):
    if request.method == "POST":
        uname = request.POST["username"]
        pw = request.POST["password"]
        
        user = authenticate(request, username=uname, password=pw)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "food_villa/login.html", {
                "message": "User doesn't exist!"
            })
    return render(request, "food_villa/login.html")

def signup_view(request):
    if request.method == "POST":
        uname = request.POST["username"]
        email = request.POST["email_id"]
        pw = request.POST["password"]
        if uname == "" or email == "" or pw == "":
            return render(request, "food_villa/signup.html", {
                "message": "Something went wrong. Please try again!"
            }) 
        User.objects.create_user(uname, email, pw)
        return render(request, "food_villa/login.html", {
            "message": "Sign up successful!"
        })
    return render(request, "food_villa/signup.html")

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "food_villa/index.html")

def logout_view(request):
    logout(request)
    return render(request, "food_villa/login.html")

def location(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "food_villa/location.html")

def menu(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if "cartitems" not in request.session:
        request.session["cartitems"] = []
    return render(request, "food_villa/foodmenu.html", {
        "cartCount": len(request.session["cartitems"])
    })

def cart(request):
    if request.method == "POST":
        data = json.loads(request.body)
        request.session["cartitems"] += [data["id"]]
        print(request.session["cartitems"])
        return HttpResponse(status=200)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    items = Counter(request.session["cartitems"])
    item_objects = []
    total = 0
    i = 1
    for each in items:
        obj = Item.objects.get(id=int(each))
        item_objects.append((i,obj,items[each], obj.cost*items[each]))
        total += obj.cost*items[each]
        i += 1
    return render(request, "food_villa/cart.html", {
        "objects": item_objects,
        "total": total
    })

def order(request):
    if request.method == "POST":
        data = json.loads(request.body)
        items = Counter(request.session["cartitems"])
        new_order = Order.objects.create(user = request.user, address=data["address"], total=data["total"])
        for each in items:
            obj = Item.objects.get(id=int(each))
            q = Quantity(order = new_order, item = obj, count = items[each])
            q.save()
        request.session["cartitems"] = []
        print("order successful")
        return HttpResponse(status=200)

def view_orders(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    previous = Order.objects.filter(user = request.user)
    items_array = []
    dates_array = []
    count_array = []
    total_array = []
    id_array = []
    k=1
    for each in previous:
        i = Quantity.objects.filter(order = each)
        m = []
        for _ in i:
            m.append((_.item.name, _.count))
        items_array.append(m)
        dates_array.append(each.order_datetime.strftime("%d/%m/%Y"))
        total_array.append(each.total)
        id_array.append(each.id)
        count_array.append(k)
        k += 1
    return render(request, "food_villa/vieworders.html", {
        "data": list(zip(count_array, dates_array, items_array, total_array, id_array))
    })

def feedback(request):
    if request.method == "POST":
        data = json.loads(request.body)
        order_obj = Order.objects.get(id=data["id"])
        order_obj.feedback = data["feedback"]
        order_obj.save()
        return HttpResponse(status=200)

    




