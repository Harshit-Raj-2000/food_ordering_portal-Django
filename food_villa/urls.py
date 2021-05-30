from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup_view, name="signup"),
    path('logout', views.logout_view, name="logout"),
    path('location', views.location, name="location"),
    path('menu', views.menu, name="menu"),
    path('cart', views.cart, name="cart"),
    path('order', views.order, name="order")
]