from django.forms import ModelForm
from myrestaurant.models import Restaurant, Dish

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('user', 'date',)

class DishForm(ModelForm):
    class Meta:
        model = Dish
        exclude = ('user', 'date', 'restaurant',)