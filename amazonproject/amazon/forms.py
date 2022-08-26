from django import forms

from amazon.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','desc','mrp','price','image']