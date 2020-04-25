from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from classes.models import Restaurant, Account, Owner, Type, Food
from managements.forms import AddRestaurantForm, AddFoodForm, EditRestaurantForm

def management(request):
    return render(request, template_name='managementRestaurant.html')

    
def addRestaurant(request):
    restaurant = Restaurant.objects.all()    
    if request.method == 'POST':
        form = AddRestaurantForm(request.POST, request.FILES)  
        if form.is_valid():
            typeRestaurant = Type.objects.create(type_name = request.POST.get('type_name'))
            restaurant = form.save(commit=False)
            restaurant.type_type_id = typeRestaurant
            print(restaurant.picture_restaurant)
            restaurant.save()
            return redirect('addRestaurant')       
    else:        
        form = AddRestaurantForm()       
    return render(request, 'managementRestaurant.html', context={        
        'form' : form,
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
    fd = Food.objects.filter(restaurant_restaurant_id_id = id)  
    if request.method == 'POST':
        # food = Food.objects.get(pk = id)
        # print(food)
        form = AddFoodForm(request.POST, request.FILES)  
        if form.is_valid():       
            Food.objects.create(food_name = request.POST.get('food_name'), picture = request.POST.get('picture'), price = request.POST.get('price'), restaurant_restaurant_id_id = id ) 
            food = form.save(commit=False)     
            return redirect('addFood', id=id)       
    else:        
        form = AddFoodForm()       
    return render(request, 'managementFood.html', context={        
        'form' : form,
        'id': id,
        'food' : fd

    })


# def editMenu(request):
#     try:
#         food = Food.objects.get(pk=food_id)

#     except Food.DoesNotExist:
#         return redirect('MenuList')

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

#     return render(request, 'editMenu.html', context=context)


def deleteFood(request, id):
    food = Food.objects.get(food_id=id)
    food.delete()
    return redirect(to='addFood')
