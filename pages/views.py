from django.shortcuts import render,redirect
from django.views.generic import TemplateView


def home_page_view(request):
    return redirect("products_list")


# class HomePageView(TemplateView):
# template_name = 'home.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'
