from builtins import object
from gc import get_objects

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

from classes.models import Food, Owner, Restaurant, Type, Order, Order_List
from managements.forms import AddFoodForm, AddRestaurantForm,UserForm,OwnerForm,CustomerForm
from django.contrib.auth.models import User

def home(request):
    return render(request, 'homepage.html')


def management(request):
    restaurant = Restaurant.objects.all()
    return render(request, 'management.html', context={
        'restaurant': restaurant
    })


def homepage(request):
    restaurant = Restaurant.objects.all()
    list = []
    for check in restaurant:
        dict = {
            'restaurant_id': check.restaurant_id,
            'restaurant_name': check.restaurant_name,
            'picture_restaurant': check.picture_restaurant}
        list.append(dict)
    return render(request, 'homepage.html',
                  context={'check': list}
                  )


def detailRestaurant(request, id):
    res_id = Restaurant.objects.get(pk=id)
    food_id = Food.objects.filter(food_id=res_id.restaurant_id)
    list_food = []
    for food_id in food_id:
        dict_food = {
            'food_id': food_id.food_id,
            'food_name': food_id.food_name,
            'picture_food': food_id.picture,
            'price': food_id.price,
            'restaurant': food_id.restaurant_id
        }
        list_food.append(dict_food)

    return render(request, 'detailRestaurant.html', context={
        'id': id,
        'food_id': list_food,
        'res_id': res_id
    })


def my_login(request):
    context = {}
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('homepage')

        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    return render(request, template_name='login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect(to='login')

def registerOwner(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        owner_form = OwnerForm(request.POST,request.FILES)
        if user_form.is_valid() and owner_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            owner = owner_form.save()
            owner.user_id = user.id
            owner.save()
            return redirect('login')
        else:
            print(user_form.errors,owner_form.errors)
        
    else:
        user_form = UserForm()
        owner_form = OwnerForm()
    return render(request,template_name='register.html',context={
        'user_form':user_form,
        'owner_form':owner_form,
        'owner':'owner'
    })
def registerCustomer(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        customer_form = CustomerForm(data=request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            customer = customer_form.save()
            customer.user_id = user.id
            customer.save()
            return redirect('login')
        else:
            print(user_form.errors,customer_form.errors)
        
    else:
        user_form = UserForm()
        customer_form = CustomerForm()
    return render(request,template_name='register.html',context={
        'user_form':user_form,
        'customer_form':customer_form,
        'customer':'customer'
    })


def addRestaurant(request):
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            typeRestaurant = Type.objects.create(
                type_name=request.POST.get('type_name'))
            restaurant = form.save(commit=False)
            restaurant.type_type_id = typeRestaurant
            # print(restaurant.picture_restaurant)
            restaurant.save()
            return redirect('management')
    else:
        form = AddRestaurantForm()
    return render(request, 'addRestaurant.html', context={
        'form': form
    })


def editRestaurant(request, id):
    restaurant = Restaurant.objects.get(restaurant_id=id)
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST, request.FILES, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect(to='management')
    else:
        form = AddRestaurantForm(instance=restaurant)

    return render(request, 'editRestaurant.html', context={
        'form': form,
        'restaurant': restaurant,
        'id': id
    })


def deleteRestaurant(request, id):
    restaurant = Restaurant.objects.get(restaurant_id=id)
    restaurant.delete()
    return redirect('management')


def managementFood(request, id):
    food = Food.objects.filter(restaurant_id=id)
    return render(request, 'managementFood.html', context={
        'id': id,
        'food': food
    })


def addFood(request, res_id):
    if request.method == 'POST':
        form = AddFoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            food.restaurant_id = res_id
            food.save()
            return redirect('managementFood', id=res_id)
    else:
        form = AddFoodForm()
    return render(request, 'addFood.html', context={
        'form': form,
        'id1': res_id
    })


def editFood(request, res_id, food_id):
    food = Food.objects.get(food_id=food_id)
    if request.method == 'POST':
        if food.restaurant_id == res_id:
            form = AddFoodForm(request.POST, request.FILES, instance=food)
            if form.is_valid():
                form.save()
                return redirect('managementFood', id=res_id)
    else:
        form = AddFoodForm(instance=food)
    return render(request, 'editFood.html', context={
        'form': form,
        'id': food_id,
        'id1': res_id
    })


def manageOrder(request):
    order = Order.objects.all()
    order_list = Order_List.objects.all()
    list = []
    list2 = []
    for od in order:
        dict = {
            'id': od.order_id,
            'time': od.date_time,
            'total_price': od.total_price
        }
        list.append(dict)

    for ol in order_list:
        dict2 = {
            'id': ol.order_id,
            'food': Food.objects.get(pk=ol.food_id).food_name,
            'price': ol.price,
            'unit': ol.unit
        }
        list2.append(dict2)

    return render(request, 'manageOrder.html', context={
        'orders': list,
        'foods': list2
    })

def manageStateOrder(request):
    order = Order.objects.filter(state__isnull=False)
    order_list = Order_List.objects.all()
    list = []
    list2 = []
    for od in order:
        dict = {
            'id': od.order_id,
            'time': od.date_time,
            'total_price': od.total_price,
            'state':od.state
        }
        list.append(dict)

    for ol in order_list:
        dict2 = {
            'id': ol.order_id,
            'food': Food.objects.get(pk=ol.food_id).food_name,
            'price': ol.price,
            'unit': ol.unit
        }
        list2.append(dict2)

    return render(request, 'manageStateOrder.html', context={
        'orders': list,
        'foods': list2
    })

def changeStateToDoing(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.state = "Doing"
    order.save()
    return redirect(to='manageStateOrder')

def changeStateToDone(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.state = "Done"
    order.save()
    return redirect(to='manageStateOrder')


def deleteFood(request, res_id, food_id):
    food = Food.objects.get(food_id=food_id)
    food.delete()
    return redirect(to='managementFood', id=res_id)


def confirmOrder(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.state = "Queuing"
    return redirect(to='manageOrder')


def cancelOrder(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    return redirect(to='manageOrder')


def searchRestaurant(request):
    search = request.GET.get('search', '')
    restaurant = Restaurant.objects.all()
    findres = Restaurant.objects.filter(
        name__icontain=search
    )
    return render(request, '.html', context={
        'search': search,
        'restaurant': restaurant,
        'findres': findres})
