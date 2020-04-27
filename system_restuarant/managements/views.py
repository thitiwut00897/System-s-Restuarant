from builtins import object
from gc import get_objects

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

from classes.models import Food, Owner, Restaurant, Type, Order,Order_List
from managements.forms import AddFoodForm, AddRestaurantForm, EditRestaurantForm


def home(request):
    return render(request, template_name='base.html')


def management(request):
    return render(request, template_name='managementRestaurant.html')


def homepage(request):
    res = Restaurant.objects.all() 
    list=[]
    for check in res:
        dict = {
            'id': check.restaurant_id,
            'name': check.restaurant_name,
            'picture': check.picture_restaurant
        }
        list.append(dict)
    return render(request, 'homepage.html', 
        context={'check': list}
        )
    
def my_login(request):
    context = {}
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')

        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    return render(request, template_name='login.html', context=context)


def my_logout(request):
    logout(request)
    return redirect(to='login')


def addRestaurant(request):
    restaurant = Restaurant.objects.all()
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            typeRestaurant = Type.objects.create(
                type_name=request.POST.get('type_name'))
            restaurant = form.save(commit=False)
            restaurant.type_type_id = typeRestaurant
            print(restaurant.picture_restaurant)
            restaurant.save()
            return redirect('addRestaurant')
    else:
        form = AddRestaurantForm()
    return render(request, 'managementRestaurant.html', context={
        'form': form,
        'restaurant': restaurant
    })



# def editRestaurant(request, id):
#     restaurant = Restaurant.objects.get(restaurant_id=id)
#     print(restaurant)
#     if request.method == 'POST':
#         form = EditRestaurantForm(request.POST, request.FILES)
#         if form.is_valid():
#             typeRestaurant = Type.objects.get(type_name = request.POST.get('type_name'))
#             restaurant = form.save(commit=False)
#             restaurant.type_type_id = typeRestaurant
#             print(restaurant.picture_restaurant)
#             restaurant.save()
#             return redirect('editRestaurant')
#     else:
#         form = EditRestaurantForm()
#     return render(request, 'editRestaurant.html', context={
#         'form' : form,
#         'restaurant': restaurant
#     })



def deleteRestaurant(request, id):
    restaurant = Restaurant.objects.get(restaurant_id=id)
    restaurant.delete()
    return redirect(to='addRestaurant')


def addFood(request, id):
    fd = Food.objects.filter(restaurant_id=id)
    # print(fd)
    if request.method == 'POST':
        form = AddFoodForm(request.POST, request.FILES)
        if form.is_valid():
            # Food.objects.create(food_name = request.POST.get('food_name'), picture = request.POST.get('picture'), price = request.POST.get('price'), restaurant_restaurant_id_id = id )
            food = form.save(commit=False)
            food.restaurant_id = id
            food.save()
            # print(food.picture)
            return redirect('addFood', id=id)
    else:
        form = AddFoodForm()
    return render(request, 'managementFood.html', context={
        'form': form,
        'id': id,
        'food': fd

    })



# def editFood(request):
#     try:
#         food = Food.objects.get(pk=food_id)
#     except Food.DoesNotExist:
#         return redirect('addFood')
#     if request.method == 'POST':
#         food.food_name=request.POST.get('food_name')
#         food.picture=request.POST.get('picture')
#         food.price=request.POST.get('price')
#         food.save()
#     context = {
#         'food_name': Food.food_name,
#         'picture': Food.picture,
#         'price': Food.price
#     }
#     return render(request, 'editFood.html', context=context)

def manageOrder(request):
    order = Order.objects.all()
    order_list = Order_List.objects.all()
    list = []
    list2 = []
    for od in order:
        for ol in order_list:
            if od.order_id == ol.order_id:
                dict = {
                    'id': od.order_id,
                    'id_2': od.order_id,
                    'time': od.date_time,
                    'food': Food.objects.get(pk=ol.food_id).food_name,
                    'price': ol.price,
                    'unit': ol.unit

                }
                list.append(dict)

    return render(request, 'manageOrder.html', context={
        'orders': list
    })


def deleteFood(request, res_id, food_id):
    food = Food.objects.get(food_id=food_id)
    food.delete()
    return redirect(to='addFood', id=res_id)


def searchRestaurant(request):
    search = request.GET.get('inputSearch', '')
    filter = classes.object.filter(name__icontain=search)
    return render(request, template_name='base.html',
                  context={
                      'search': search,
                      'filter': filter})
