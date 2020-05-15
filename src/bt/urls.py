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
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from .views import home_view

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html')),
    # path('', home_view, name='home'),
    path('', RedirectView.as_view(permanent=True, url='static/index.html')),
    # url重定向简化用户输入,以后增加其它功能模块全部要这样处理,优化用户体验
    # path('tab', RedirectView.as_view(permanent=True, url='static/ui/tab/tab.html')),
    # path('cmd', RedirectView.as_view(permanent=True, url='static/ui/cmd/cmd.html')),
    # path('', serve, {'path': 'ui/bt/vue.html'}),
    path('favicon.ico', serve, {'path': 'image/favicon.ico'}),
    # path('admin/', admin.site.urls),
    path('url/', include(('url.urls', 'url'), namespace='url')),
    path('cmd/', include(('cmd_tool.urls', 'cmd_tool'), namespace='cmd_tool')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
