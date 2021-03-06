"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from carts.views import cart_home
from accounts.views import LoginView, RegisterView, guest_register_view
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from carts.views import cart_detail_api_view
from .views import home_page, about_page, contact_page 


urlpatterns = [
    url(r'^$',home_page , name='home'),
    url(r'^about/$',about_page, name='about'),
    url(r'^contact/$',contact_page ,name='contact'),
    url(r'^login/$',LoginView.as_view(), name='login'),
    url(r'^checkout/address/create/$',checkout_address_create_view, name='checkout_address_create'),
    url(r'^checkout/address/reuse/$',checkout_address_reuse_view, name='checkout_address_reuse'),
    url(r'^register/guest/$',guest_register_view, name='guest_register'),
    url(r'^logout/$',LogoutView.as_view(), name='logout'),
    url(r'^api/cart/$',cart_detail_api_view, name='api-cart'),
    url(r'^cart/',include("carts.urls", namespace ='cart')),
    url(r'^register/$',RegisterView.as_view(), name='register'),
    url(r'^bootstrap/$',TemplateView.as_view(template_name='bootstrap/example.html')),
    url(r'^products/',include("products.urls",namespace='products')),
    ## Reference to product urls
    url(r'^search/',include("search.urls",namespace='search')),


    # url(r'^featured$',ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$',ProductFeaturedDetailView.as_view()),
    # url(r'^products/$',ProductListView.as_view()),
    # url(r'^products-fbv/$',product_list_view),
    # ## check for ids in routes
    # ## Breaking down re
    # ## ^  Caret. Matches a pattern at the start of the string.
    # ## $  Matches a pattern at the end of string.
    # ## ?  Checks for exactly zero or one character to its left.
    # ## () Groups
    # ## (?P<name>...)  Similar to regular parentheses, but the substring matched by the group is accessible via the symbolic group name name
    # ## \d Lowercase d. Matches decimal digit 0-9.
    # ## \w Matches Unicode word characters; this includes most characters that can be part of a word in any language, as well as numbers and the underscore.
    # ## [] Match in set
    # #url(r'^products/(?P<pk>\d+)/$',ProductDetailView.as_view()),
    # url(r'^products/(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view()),
    # #url(r'^products-fbv/(?P<pk>\d+)/$',product_detail_view),
    url(r'^admin/', admin.site.urls)
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
