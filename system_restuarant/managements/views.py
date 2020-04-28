from builtins import object
from gc import get_objects

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

from classes.models import Food, Owner, Restaurant, Type, Order, Order_List
from managements.forms import AddFoodForm, AddRestaurantForm


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
    res_id = Restaurant.objects.get(restaurant_id=id)
    list = []
    dict = {
        'restaurant_id': res_id.restaurant_id,
        'restaurant_name': res_id.restaurant_name,
        'open_time': res_id.open_time,
        'close_time': res_id.close_time,
        'types': res_id.types,
        'owner': res_id.owner,
        'picture_restaurant': res_id.picture_restaurant,
    }
    list.append(dict)
    return render(request, 'detailRestaurant.html', context={
        'id': id,
        'res_id': list
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


def addRestaurant(request):
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST, request.FILES)
        
        if form.is_valid():
            typeRestaurant = Type.objects.create(
                type_name=request.POST.get('type_name'))
            restaurant = form.save(commit=False)
            restaurant.type_type_id = typeRestaurant
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
        form = AddRestaurantForm(request.POST, instance=restaurant)
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
    return redirect(to='management')


def managementFood(request, id):
    food = Food.objects.filter(restaurant_id=id)
    return render(request, 'managementFood.html', context={
        'id': id,
        'food': food
    })


def addFood(request, res_id):
    if request.method == 'POST':
        form = AddFoodForm(request.POST, request.FILES)
        msg = 'เพิ่มรายการอาหาร'
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
            form = AddFoodForm(request.POST, instance=food)
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
