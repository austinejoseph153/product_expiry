from django import forms
from .models import Batch

class AddBatchForm(forms.Form):
    name = forms.CharField(label="Batch Name",widget=forms.TextInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(label='Quantity', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    manufacturing_date = forms.DateField(label="Manufacturing Date", widget=forms.DateInput(attrs={"type":"date","class":"form-control"}))
    expiry_date = forms.DateField(label="Expiry Date",widget=forms.DateInput(attrs={"type":"date","class":"form-control"}))
    description = forms.CharField(label="Batch Description",required=False, widget=forms.Textarea(attrs={"class":"form-control"}))

class AddProductForm(forms.Form):
    name = forms.CharField(label="Product Name", widget=forms.TextInput(attrs={"class":"form-control"}))
    manufacturer = forms.CharField(label="Manufacturer Name", widget=forms.TextInput(attrs={"class":"form-control"}))
    category = forms.CharField(label="Product Category", widget=forms.TextInput(attrs={"class":"form-control"}))
    quantity = forms.IntegerField(label="Quantity in Stock", widget=forms.NumberInput(attrs={"class":"form-control"}))
    price = forms.DecimalField(label="Product Price", widget=forms.NumberInput(attrs={"class":"form-control"}))
    maufacturing_date = forms.DateField(label="Product Manufacturing Date", widget=forms.DateInput(attrs={"type":"date","class":"form-control"}))
    expiry_date = forms.DateField(label="Product Expiry Date", widget=forms.DateInput(attrs={"type":"date","class":"form-control"}))
    image = forms.ImageField()
    batch = forms.ModelChoiceField(empty_label="Select product batch", queryset=Batch.objects.all(), widget=forms.Select(attrs={"class": "form-select"}))
    description = forms.CharField(label="Product Description", widget=forms.TextInput(attrs={"class":"form-control"}))

class AddNewUserForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class":"form-control"}))