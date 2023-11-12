from django import forms
from products.models import Product
from categories.models import Category


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Category'
    )

    class Meta:
        model = Product
        fields = ['title', 'image', 'price', 'instock', 'category']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError(
                "Title must be at least 3 characters long.")
        return title

    def clean_image(self):
        image = self.cleaned_data['image']
        if image.size > 2 * 1024 * 1024:
            raise forms.ValidationError(
                "Image size should be no larger than 2 MB.")
        return image

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price

    def clean_instock(self):
        instock = self.cleaned_data['instock']
        if instock < 0:
            raise forms.ValidationError(
                "In-stock quantity cannot be negative.")
        return instock
