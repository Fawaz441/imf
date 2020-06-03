from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Challenger

CATEGORIES = (
    ('S','Join as a Student'),
    ('F','Join as a Farmer'),
    ('C','Join as a Company')
)


class SignUpForm(UserCreationForm):
    category = forms.ChoiceField(choices=CATEGORIES,widget=forms.RadioSelect)

    class Meta:
        fields = ("first_name","last_name","username","email","password1","password2")
        model = get_user_model()

class StudentForm(forms.Form):
    phone_number = forms.CharField(max_length=20)
    location = forms.CharField(max_length=20)


CROP_VARIETIES = (
    ('Tubers','Tubers'),
    ('Grains','Grains'),
    ('Vegetables','Vegetables'),
    ('Fruits','Fruits'),
)
class FarmerForm(forms.Form):
    farm_name = forms.CharField(label="Farm Name")
    location = forms.CharField()
    land_size = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'1/2 acre'}))
    major_products = forms.ChoiceField(choices=CROP_VARIETIES,help_text='Choose the varieties you mostly deal with')
    phone_number = forms.CharField(max_length=20)
    does_livestock = forms.BooleanField(label='Do you deal with livestock?')
    

class CompanyForm(forms.Form):
    company_name = forms.CharField()
    location = forms.CharField()
    phone_number = forms.CharField()



class DeliveryForm(forms.Form):
    location = forms.CharField()
    state = forms.CharField()



class ChallengerForm(forms.ModelForm):
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'placeholder':'Your email'}))
    class Meta:
        model = Challenger
        fields = '__all__'