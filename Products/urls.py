## Product App URLS

from . import views
from django.urls import path


urlpatterns = [
    path("", views.home),
    path("stock/",views.stock),
    path("sales/",views.sales)
]
