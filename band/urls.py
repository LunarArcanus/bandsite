from django.conf.urls import url
import views

urlpatterns = [
        url(r"^$", views.index, name="index"),
        url(r"^about", views.about, name="about"),
        url(r"^bands", views.bands, name="bands"),
        url(r"^submitted", views.submitted, name="submitted"),
        url(r"^form", views.form_handler, name="form"),
        url(r"^buy", views.merch, name="merchandise"),
        url(r"^cart", views.cart, name="cart"),
        ]
