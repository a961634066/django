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
from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from appss.pruduct.views import TaskView, CacheView, LogView, ModelsView, Students, StudentsMixinGenerics, PdfView, \
    ExcelView, get_info, VerifierView

from appss.pruduct.views import StudentsViewsets, NewStudents

router = DefaultRouter()

# 配置students的url
router.register(r'students', StudentsViewsets, basename="test")
router.register(r'delete', NewStudents, basename="delete")

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
    url(r'^ver/',VerifierView.as_view()),

    # genricAPIView的路由
    url(r'^gen/', include(genric_patterns)),
    url(r'^info/', get_info),

    # drf文档，安装coreapi包，$符号一定不要
    url(r'^doc/', include_docs_urls(title='bbb')),

    # router的配置
    url(r'^', include(router.urls)),

    # apliay支付订单
    url(r'^order/', include("appss.aplay.urls")),


    # include测试,两种取参方式，路由正则
    url(r'^include/', include("appss.include_test.urls"))

]

# 两种方式，include或下面
# urlpatterns += router.urls