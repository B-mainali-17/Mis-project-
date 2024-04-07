"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# import statistics
# from django.conf import settings
# from django.contrib import admin
# from django.urls import path
# from testapp import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('' ,views.index,name='index'),
#     path( 'contact/',views.contact,name='contact'),
#     path('about.html',views.about,name='aboutus'),
# ]
from django.contrib import admin
from django.urls import path
# from testapp import views
from cart import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cart'
urlpatterns = [
    path('admin', admin.site.urls),
    # path('', views.index, name='index'),
    # path('contact.html', views.contact, name='contact'),
    # path('about.html', views.about, name='about'),
    # path('products.html', views.products, name='products'),
    # path('single-product.html', views.single_product, name='single-product'),
    # path('index.html', views.index, name='index'),

    path('', views.product_list, name='product_list'),
    path('/home', views.home, name='home'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)