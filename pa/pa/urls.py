"""pa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from MyWebPage.views import Home, BrandView, Register, CheckoutView, BuyView




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Home.as_view(), name="home"),
    path('brand_type/<int:brand_type_id>/', BrandView.as_view(), name='brand_type'),
    path('registration/', Register.as_view(), name='registration'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('checkout/<int:product_id>/', CheckoutView.as_view(), name='checkout'),
    path('thanks/', BuyView.as_view(), name='buy')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
