"""operation URL Configuration

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
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from appss.pruduct.views import TaskView, CacheView, LogView, ModelsView, Students, StudentsMixinGenerics, PdfView, \
    ExcelView

from appss.pruduct.views import StudentsViewsets

router = DefaultRouter()

# 配置students的url
router.register(r'students', StudentsViewsets)

test_patterns = [
    url(r'test/$', TaskView.as_view()),
    url(r'cache/$', CacheView.as_view()),
    url(r'log/$', LogView.as_view()),
    url(r'models/$', ModelsView.as_view()),
]


genric_patterns = [
    url(r'goods/$', Students.as_view(), name="goods-list"),
    url(r'pdf/$', PdfView.as_view(), name="goods-list"),
    url(r'excel/$', ExcelView.as_view(), name="goods-list"),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/',include(test_patterns)),

    # genricAPIView的路由
    url(r'^gen/', include(genric_patterns)),

    # drf文档，安装coreapi包，$符号一定不要
    url(r'^doc/', include_docs_urls(title='bbb')),


    # router的配置
    url(r'^', include(router.urls))
]
