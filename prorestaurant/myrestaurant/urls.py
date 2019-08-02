from django.urls import path
from django.utils import timezone
from django.views.generic import DetailView, ListView
from myrestaurant.models import Restaurant, Dish
from myrestaurant.forms import RestaurantForm, DishForm
from myrestaurant.views import RestaurantCreate, DishCreate, RestaurantDetail, review, LoginRequiredCheckIsOwnerUpdateView

app_name = "myrestaurant"

urlpatterns = [
    # List latest 5 restaurants: /myrestaurant/
    path('',
        ListView.as_view(
            queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
            context_object_name='latest_restaurant_list',
            template_name='myrestaurant/restaurant_list.html'),
        name='restaurant_list'),

    # Restaurant details, ex.: /myrestaurant/restaurants/1/
    path('restaurants/<int:pk>',
        RestaurantDetail.as_view(),
        name='restaurant_detail'),

    # Restaurant dish details, ex: /myrestaurant/restaurants/1/dishes/1/
    path('restaurants/<int:pkr>/dishes/<int:pk>',
        DetailView.as_view(
            model=Dish,
            template_name='myrestaurant/dish_detail.html'),
        name='dish_detail'),

    # Create a restaurant, /myrestaurant/restaurants/create/
    path('restaurants/create',
        RestaurantCreate.as_view(),
        name='restaurant_create'),

    # Edit restaurant details, ex.: /myrestaurant/restaurants/1/edit/
    path('restaurants/<int:pk>/edit',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Restaurant,
            form_class=RestaurantForm),
        name='restaurant_edit'),

    # Create a restaurant dish, ex.: /myrestaurant/restaurants/1/dishes/create/
    path('restaurants/<int:pk>/dishes/create',
        DishCreate.as_view(),
        name='dish_create'),

    # Edit restaurant dish details, ex.: /myrestaurant/restaurants/1/dishes/1/edit/
    path('restaurants/<int:pkr>/dishes/<int:pk>/edit',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Dish,
            form_class=DishForm),
        name='dish_edit'),

    # Create a restaurant review, ex.: /myrestaurant/restaurants/1/reviews/create/
    path('restaurants/<int:pk>/reviews/create',
        review,
        name='review_create'),
]