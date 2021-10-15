from django.contrib import admin
from django.urls import path
import app.views

urlpatterns = [
    path("", app.views.root, name="root"),
    path("birthday/", app.views.birthday, name="birthday"),
    path("food/", app.views.food, name="food"),
    path("hundred/", app.views.hundred, name="hundred"),
    path("string-splosion/", app.views.string_splosion, name="string-splosion"),
    path("cat-dog/", app.views.cat_dog, name="cat-dog"),
    path("lone-sum/", app.views.lone_sum, name="lone-sum")

]
