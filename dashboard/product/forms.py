from django import forms
from matjar.models import Category, Product


class ProductForm(forms.Form):
    name = forms.CharField(label='اسم المنتج', max_length=100)
    category = forms.ModelChoiceField(label='التصنيف', queryset=Category.objects.all(), empty_label='اختر من القائمة')
    description = forms.CharField(label='الوصف', max_length=500)
    price = forms.DecimalField(label='السعر', max_digits=10, decimal_places=2)
    published = forms.BooleanField(label='عرض المنتج في الموقع', required=False)
    show_on_homepage = forms.BooleanField(label='اعرض في الصفحة الرئيسية',required=False)
    image = forms.ImageField(label='صور للمنتج')

    class Meta:
        model = Product