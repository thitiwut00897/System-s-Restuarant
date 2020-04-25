from django import forms
from django.forms import ModelForm
from classes.models import Restaurant, Food
# from crispy_forms.helper import FormHelper
# from django.validator import validate_slug


class AddRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['restaurant_name','picture_restaurant', 'working_hours']
        label = {
            'restaurant_name': 'ชื่อร้านอาหาร',
            'working_hours': 'เวลาเปิด/ปิดร้านอาหาร',
            'picture_restaurant': 'รูปภาพร้านอาหาร'
        }

class EditRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['restaurant_name','picture_restaurant', 'working_hours']
        label = {
            'restaurant_name': 'ชื่อร้านอาหาร',
            'working_hours': 'เวลาเปิด/ปิดร้านอาหาร',
            'picture_restaurant': 'รูปภาพร้านอาหาร'
        }

class AddFoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'picture', 'price']
        label = {
            'food_name': 'ชื่ออาหาร',
            'price': 'ราคา',
            'picture': 'รูปร้านอาหาร'
        }
