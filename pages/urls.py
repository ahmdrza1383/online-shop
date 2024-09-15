from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('aboutus/', views.AboutUsView.as_view(), name='about_us'),
]
