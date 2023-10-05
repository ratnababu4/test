from django.urls import path 
from .views import Booklist
from .views import post_Book
from .views import update_Book
from .views import delete_Book

urlpatterns = [
    path("",Booklist),
    path("add/",post_Book),
    path("update/<int:id>/",update_Book),
     path("delete/<int:id>/",delete_Book),
     
]