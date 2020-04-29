from django import forms
from django.forms import ModelForm
from classes.models import Customer, Food, Owner, Restaurant
from django.contrib.auth.models import User
# from crispy_forms.helper import FormHelper
# from django.validator import validate_slug


class AddRestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['restaurant_name', 'picture_restaurant',
                  'open_time', 'close_time']
        labels = {
            'restaurant_name': 'ชื่อร้านอาหาร',
            'open_time': 'เวลาเปิดร้าน',
            'close_time': 'เวลาปิดร้าน',
            'picture_restaurant': 'รูปภาพร้านอาหาร'
        }
        widgets = {
            'restaurant_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'ชื่อร้านอาหาร'
                }),
            'open_time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : '00:00'}),
            'close_time': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : '00:00'
            }),
            'picture_restaurant': forms.FileInput(attrs={'class': 'custom-file-input'})
        }

        # def clean(self):
        #     cleaned_data = super().clean()
        #     if(price.isdigit() == false):
        #         msg = "กรุณากรอกตัวเลข"
        #         self.add_error('price', msg)



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
            'food_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'ชื่อร้านอาหาร'}),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : '00.0'}),
            'picture': forms.FileInput(attrs={'class': 'custom-file-input'})
        }
        # def clean(self):
        #     cleaned_data = super().clean()
        #     price = cleaned_data.get('price')
        #     if(price.isdigit() == false):
        #         msg = "กรุณากรอกตัวเลข"
        #         self.add_error('price', msg)
        #


class UserForm(ModelForm):
    class Meta:
        model = User 
        fields  = ['username','password','first_name','last_name','email']
        labels = {
            'username': 'Username',
            'password': 'Password',
            'first_name': 'ชื่อ',
            'last_name': 'นามสกุล',
            'email': 'อีเมล'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields  = ['picture_owner']
        labels = {
            'picture_owner': 'รูปภาพ'
        }
        widgets = {
            'picture_owne': forms.FileInput(attrs={'class': 'custom-file-input'})
        }

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields  = ['faculty']
        labels = {
            'faculty': 'คณะ'
        }
        widgets = {
            'faculty': forms.TextInput(attrs={'class': 'form-control'})
        }