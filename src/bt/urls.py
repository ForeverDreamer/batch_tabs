"""bt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.conf import settings
# from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve

from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('favicon.ico', serve, {'path': 'image/favicon.ico'}),
    path('admin/', admin.site.urls),
    path('url/', include(('url.urls', 'url'), namespace='url')),
    path('cmd/', include(('cmd_tool.urls', 'cmd_tool'), namespace='cmd_tool')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
