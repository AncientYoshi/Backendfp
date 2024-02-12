from django.urls import path
from . import views

#add following lines to urlpatterns list 
urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]


