from django.urls import path
from .views import dashboard_view, login_view, logout_view

app_name = "account"
urlpatterns = [
    path("", view=dashboard_view, name="dashboard"),
    path("login/", view=login_view, name="login"),
    path("logout/", view=logout_view, name="logout"),
]