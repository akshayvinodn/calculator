from django.urls import path
from calc import views
urlpatterns=[
    path('index/',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('home/',views.home,name="home"),
    path('login/',views.login,name="login"),
]