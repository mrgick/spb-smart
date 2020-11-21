"""spb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from offer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rateoffer/', rate_offer, name='rate_offer'),
    path('top/', top_offers, name='top_offers_url'),
    path('inproc/', inproc_offers, name='inproc_offers_url'),
    path('archive/', archive_offers, name='archive_offers_url'),
    path('offer/create/', OfferCreate.as_view(), name='offer_create'),
    path('offer/<str:slug>/update/', OfferUpdate.as_view(), name='offer_update_url'),
    path('offer/<str:slug>/', OfferDetail.as_view(), name='offer_detail_url'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('', home, name='home'),

]
