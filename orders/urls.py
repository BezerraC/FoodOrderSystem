from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_request, name="login"),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("Pizzas", views.pizza, name="pizza"),
    path("Massas", views.pasta, name="pasta"),
    path("Saladas", views.salad, name="salad"),
    path("Sanduiches", views.subs, name="subs"),
    path("Pratos", views.dinner_platters, name="dinner_platters"),
    path("directions", views.directions, name="directions"),
    path("hours", views.hours, name="hours"),
    path("contact", views.contact, name="contact"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("view-orders", views.view_orders, name="view_orders"),
    path("mark_order_as_delivered", views.mark_order_as_delivered, name="mark_order_as_delivered"),
    path("save_cart", views.save_cart, name="save_cart"),
    path("retrieve_saved_cart", views.retrieve_saved_cart, name="retrieve_saved_cart"),
    path("check_superuser", views.check_superuser, name="check_superuser"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

