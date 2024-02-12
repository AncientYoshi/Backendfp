from django.urls import path
from . import views
#import obtain_auth_token view
from rest_framework.authtoken.views import ObtainAuthToken 


#add following lines to urlpatterns list 
urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', ObtainAuthToken.as_view()),
    path('secured/', views.MySecuredView.as_view(), name='secured-view'),

]


