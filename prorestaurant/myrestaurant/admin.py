from django.contrib import admin
from myrestaurant.models import Restaurant, Dish, RestaurantReview

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(RestaurantReview)

