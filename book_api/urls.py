
from django.contrib import admin
from django.urls import path
from book_api.views import book_list,book_create,book


urlpatterns = [
    path('',book_create),
    path('<int:pk>',book),
    path('list/', book_list),
]
