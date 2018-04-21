from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.utils.module_loading import import_string
from class_based_auth_views.views import LoginView, LogoutView
from rest_framework import routers
from .views import IndexView, UserHomeView
# from posts import viewsets

router=routers.DefaultRouter()
# router.register(r'posts', viewsets.PostViewSet )
# router.register(r'upload', viewsets.PicUploadViewSet )
# router.register(r'comment', viewsets.CommentViewSet )

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view( template_name="login.html", success_url="/" ), name="login"),
    # url(r'^logout/$', LogoutView.as_view( template_name="logout.html"), name="logout"),
    # url(r'^register/$', CreateView.as_view( template_name='register.html', form_class=UserCreationForm, success_url='/' ), name="register"),
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    url(r'^u/(?P<username>[\w-]+)/$', UserHomeView.as_view(), name="userhome"),
] + router.urls + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
