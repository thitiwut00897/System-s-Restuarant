from builtins import object
from gc import get_objects
from urllib.request import Request

from django.conf.global_settings import LOGIN_URL
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db.models import Q

from classes.models import Customer, Food, Order, Order_List, Owner, Restaurant, Type
from managements.forms import AddFoodForm, AddRestaurantForm, CustomerForm, OwnerForm, UserForm


def home(request):
    return render(request, 'homepage.html')


@login_required(login_url='login')
def management(request):
    restaurant = Restaurant.objects.all()
    restaurant_owner_id = Restaurant.objects.filter(owner_id=request.user.id)
    # เอา pk owner_id ในตาราง Restaurant มาเช็คกับ id ของ  user
    return render(request, 'management.html', context={
        'restaurant': restaurant,
        'restaurant_owner_id': restaurant_owner_id
    })


def homepage(request):
    restaurant = Restaurant.objects.all()
    search = request.POST.get('search')
    list = []  # เก็บร้านอาหารทั้งหมด
    for check in restaurant:
        dict = {
            'restaurant_id': check.restaurant_id,
            'restaurant_name': check.restaurant_name,
            'picture_restaurant': check.picture_restaurant}
        list.append(dict)

    if request.method == "POST":
        list = []
        find = Restaurant.objects.filter(
            restaurant_name__icontains=search
        )  # filter เอาค่า query ของ restaurant_name
        print(find)
        for check in find:
            print(check)
            dict = {
                'restaurant_id': check.restaurant_id,
                'restaurant_name': check.restaurant_name,
                'picture_restaurant': check.picture_restaurant
            }
            list.append(dict)
        print(list)

        return render(request, 'homepage.html', context={
            # 'search': search,
            # 'restaurant': restaurant,
            # 'find': find,
            'check': list
        })
    return render(request, 'homepage.html', context={
        'check': list
    })


def detailRestaurant(request, id):
    # รับค่า id ของ primary key ของร้านอาหาร เพื่อนำไปแสดงหาร้านอาหารนั้นๆ
    res = Restaurant.objects.get(pk=id)

    # เช็คว่าค่าrestaurant_id = ค่าของ restaurant_id ที่เรารับมารึเปล่า
    food = Food.objects.filter(restaurant_id=res.restaurant_id)

    # get ค่า owner มาแล้วส่งค่า
    owner = Owner.objects.get(pk=res.owner_id)

    foods = []
    for f in food:
        dict = {
            'food_id': f.food_id,
            'food_name': f.food_name,
            'picture_food': f.picture,
            'price': f.price,
            'restaurant': f.restaurant_id
        }
        foods.append(dict)

    return render(request, 'detailRestaurant.html', context={
        'id': id,
        'foods': foods,
        'restaurant': res,
        'owner': owner
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


@login_required(login_url='login')
def profile(request):
    username = request.user.username  # ดูว่า user คนไหนอยู่ในระบบ

    # เทียบ username ใน database กับ username ที่ล็อคอิน
    user = User.objects.get(username=username)

    # เอา id user มาเช็ค id ว่าอยู่คณะไหน
    customer = Customer.objects.get(user_id=request.user.id)
    context = {
        'customer': customer,
        'user': user
    }

    return render(request, 'profile.html', context=context)


@login_required(login_url='login')
def editProfile(request):
    # ดูว่า user คนไหนอยู่ในระบบ
    username = request.user.username

    # เอา id มาเช็คว่าอยู่คณะไหน แล้วก็จะดึง query ของ id นั้นมาใช้
    customer = Customer.objects.get(user_id=request.user.id)

    # เทียบ username ใน db กับ username ที่ล็อคอินว่าใช่อันเดียวกันมั้ย
    user = User.objects.get(username=username)
    if request.method == "POST":
        user.first_name = request.POST.get(
            'first_name')  # update ชื่อของuser ที่ล็อคอิน
        user.last_name = request.POST.get('last_name')
        customer.faculty = request.POST.get('faculty')
        user.save()
        customer.save()
        return redirect('profile')

    return render(request, 'editProfile.html')


@login_required(login_url='login')
def changePassword(request):
    context = {}
    if request.method == "POST":
        oldPassword = request.POST.get('oldPassword')
        newPassword = request.POST.get('newPassword')
        confirmPassword = request.POST.get('confirmPassword')

        # เอา username ของ user ที่กำลัง login อยู่
        user_id = request.user.username

        # เช็คว่า user_id ตรงกับ username รึเปล่า password ตรงกัน oldpassword รึเปล่า
        check = authenticate(request, username=user_id, password=oldPassword)

        if check:
            if newPassword == confirmPassword:

                # เอา object ของ username ตัวนั้นมา
                changePassword = User.objects.get(username=user_id)

                changePassword.set_password(newPassword)
                changePassword.save()
                return redirect('profile')
            else:
                context['password'] = oldPassword
                context['error'] = 'Password doesn''t match!'
        else:
            context['password'] = oldPassword
            context['error'] = 'รหัสผ่านไม่ถูกต้อง!'

    return render(request, 'changePassword.html', context=context)


def registerOwner(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        owner_form = OwnerForm(request.POST, request.FILES)
        if user_form.is_valid() and owner_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            owner = owner_form.save()
            owner.user_id = user.id
            owner.save()
            my_group = Group.objects.get(name='OwnerGroup') 
            my_group.user_set.add(user)
            return redirect('login')
        else:
            print(user_form.errors, owner_form.errors)

    else:
        user_form = UserForm()
        owner_form = OwnerForm()
    return render(request, template_name='register.html', context={
        'user_form': user_form,
        'owner_form': owner_form,
        'owner': 'owner'
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
            my_group = Group.objects.get(name='CustomerGroup') 
            my_group.user_set.add(user)
            return redirect('login')
        else:
            print(user_form.errors, customer_form.errors)

    else:
        user_form = UserForm()
        customer_form = CustomerForm()
    return render(request, template_name='register.html', context={
        'user_form': user_form,
        'customer_form': customer_form,
        'customer': 'customer'
    })


@login_required(login_url='login')
def addRestaurant(request):
    add = Restaurant.objects.all()
    user = request.user

    if request.method == 'POST':
        form = AddRestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            typeRestaurant = Type.objects.create(
                type_name=request.POST.get('type_name'))
            restaurant = form.save(commit=False)
            restaurant.type_type_id = typeRestaurant
            restaurant.owner_id = user.id  # create owner_id  if error. so no queryset date
            # print(restaurant.picture_restaurant)
            restaurant.save()
            return redirect('management')
    else:
        form = AddRestaurantForm()
    return render(request, 'addRestaurant.html', context={
        'form': form
    })


@login_required(login_url='login')
def editRestaurant(request, id):
    restaurant = Restaurant.objects.get(restaurant_id=id)
    if request.method == 'POST':
        form = AddRestaurantForm(
            request.POST, request.FILES, instance=restaurant)
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


@login_required(login_url='login')
def deleteRestaurant(request, id):
    restaurant = Restaurant.objects.get(restaurant_id=id)
    restaurant.delete()
    return redirect('management')


@login_required(login_url='login')
def managementFood(request, id):
    food = Food.objects.filter(restaurant_id=id)
    return render(request, 'managementFood.html', context={
        'id': id,
        'food': food
    })


@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def manageOrder(request, id):
    order = Order.objects.filter(restaurant_id=id, state="SendRequest")
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


@login_required(login_url='login')
def manageStateOrder(request, id):
    order = Order.objects.filter(Q(state="Doing") | Q(
        state="Queuing") | Q(state="Done"), restaurant_id=id)
    order_list = Order_List.objects.all()
    list = []
    list2 = []
    for od in order:
        dict = {
            'id': od.order_id,
            'time': od.date_time,
            'total_price': od.total_price,
            'state': od.state
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


@login_required(login_url='login')
def changeStateToDoing(request, order_id, res_id):
    order = Order.objects.get(pk=order_id)
    order.state = "Doing"
    order.save()
    return redirect('manageStateOrder', id=res_id)


@login_required(login_url='login')
def changeStateToDone(request, order_id, res_id):
    order = Order.objects.get(pk=order_id)
    order.state = "Done"
    order.save()
    return redirect('manageStateOrder', id=res_id)


@login_required(login_url='login')
def deleteFood(request, res_id, food_id):
    food = Food.objects.get(food_id=food_id)
    food.delete()
    return redirect(to='managementFood', id=res_id)


@login_required(login_url='login')
def confirmOrder(request, order_id, res_id):
    order = Order.objects.get(pk=order_id)
    order.state = "Queuing"
    return redirect('manageOrder', id=res_id)


@login_required(login_url='login')
def cancelOrder(request, order_id, res_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    return redirect('manageOrder', id=res_id)


@login_required(login_url='login')
def selectFood(request, id, order_id):
    order = Order.objects.get(pk=order_id)
    order_list = Order_List.objects.filter(order_id=order_id)
    order_lists = []
    total_price = 0
    for ol in order_list:
        dict = {
            'id': ol.list_no,
            'food_name': Food.objects.get(pk=ol.food_id).food_name,
            'unit': ol.unit,
            'price': ol.price*ol.unit
        }
        total_price += ol.price*ol.unit
        order_lists.append(dict)

    order.total_price = total_price
    order.save()

    res = Restaurant.objects.get(pk=id)
    food = Food.objects.filter(restaurant_id=res.restaurant_id)
    foods = []
    for f in food:
        dict = {
            'food_id': f.food_id,
            'food_name': f.food_name,
            'picture_food': f.picture,
            'price': f.price,
            'restaurant': f.restaurant_id
        }
        foods.append(dict)

    return render(request, 'detailRestaurant.html', context={
        'id': id,
        'foods': foods,
        'restaurant': res,
        'order': order,
        'order_lists': order_lists
    })


@login_required(login_url='login')
def addNewOrder_List(request, user_id, res_id, food_id):
    unit = request.GET.get("unit")
    foodAdd = Food.objects.get(pk=food_id)
    order_list = Order_List(
        unit=unit, price=foodAdd.price, food_id=foodAdd.food_id)
    order_list.save()
    order = Order(total_price=order_list.price,
                  customer_id=user_id, restaurant_id=res_id)
    order.save()
    order_list.order_id = order.order_id
    order_list.save()
    return redirect('selectFood', id=res_id, order_id=order.order_id)


@login_required(login_url='login')
def addOrder_List(request, user_id, res_id, food_id, order_id):
    unit = request.GET.get("unit")
    foodAdd = Food.objects.get(pk=food_id)
    order_list = Order_List(unit=unit, price=foodAdd.price,
                            food_id=foodAdd.food_id, order_id=order_id)
    order_list.save()
    return redirect('selectFood', id=res_id, order_id=order_id)


@login_required(login_url='login')
def createOrder(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.state = 'SendRequest'
    order.save()
    return redirect('homepage')


@login_required(login_url='login')
def deleteOrder(request, order_id, res_id):
    order = Order.objects.get(pk=order_id)
    order_list = Order_List.objects.filter(order_id=order.order_id)
    for ol in order_list:
        ol.delete()
    order.delete()
    return redirect('detailRestaurant', id=res_id)


@login_required(login_url='login')
def deleteOrderList(request, id, order_id, list_no):
    order_list = Order_List.objects.filter(pk=list_no)
    order_list.delete()
    return redirect('selectFood', id=id, order_id=order_id)


# def searchRestaurant(request):
#     search = request.POST.get('search')
#     restaurant = Restaurant.objects.all()
#     if method.Request == POST:
#         find = Restaurant.objects.filter(
#             restaurant_name__icontain=search
#         )
#         print(find)
#         return render(request, 'homepage', context={
#             'restaurant': restaurant
#         })

#     print(search)

#     return render(request, template_name='homepage', context={
#         'search': search,
#         # 'restaurant': restaurant,
#         'find': find})
