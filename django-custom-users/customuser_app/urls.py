from django.urls import path
from customuser_app import admin

from . import views

urlpatterns = [
    path("", admin.site, name="admin"),
    path("", views.index, name="homepage"),
    path("adduser/", views.adduser_view, name="adduser"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout")
]
