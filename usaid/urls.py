"""usaid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include
from django.conf.urls.static import static
from usaid.settings import STATIC_URL, STATIC_ROOT, MEDIA_ROOT, MEDIA_URL, DEBUG
from django.views.static import serve
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='admin:index')),
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls')),

    path("select2/", include("django_select2.urls")),
] + static(STATIC_URL, document_root=STATIC_ROOT) + static(MEDIA_URL, document_root=MEDIA_ROOT)

if DEBUG is False:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    ]
