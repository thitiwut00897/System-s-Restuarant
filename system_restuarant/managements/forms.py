from django import forms
from django.forms import ModelForm
from classes.models import Restaurant, Food

# from crispy_forms.helper import FormHelper
# from django.validator import validate_slug


class AddRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['restaurant_name','picture_restaurant', 'open_time','close_time']
        labels = {
            'restaurant_name': 'ชื่อร้านอาหาร',
            'open_time': 'เวลาเปิดร้าน',
            'close_time': 'เวลาเปิดร้าน',
            'picture_restaurant': 'รูปภาพร้านอาหาร'
        }
        widgets = {
            'restaurant_name': forms.TextInput(attrs={'class':'form-control'}),
            'open_time': forms.TextInput(attrs={'class':'form-control'}),
            'close_time': forms.TextInput(attrs={'class':'form-control'})
        }

class EditRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['restaurant_name','picture_restaurant', 'open_time','close_time']
        label = {
            'restaurant_name': 'ชื่อร้านอาหาร',
            'open_time': 'เวลาเปิดร้าน',
            'close_time': 'เวลาเปิดร้าน',
            'picture_restaurant': 'รูปภาพร้านอาหาร'
        }
        widgets = {
            'restaurant_name': forms.TextInput(attrs={'class':'form-control'}),
            'working_hours': forms.TextInput(attrs={'class':'form-control'}),
            'close_time': forms.TextInput(attrs={'class':'form-control'})
        }

class AddFoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'picture', 'price']
        labels = {
            'food_name': 'ชื่ออาหาร',
            'price': 'ราคา',
            'picture': 'รูปร้านอาหาร'
        }
        widgets = {
            'food_name': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'})
        }
