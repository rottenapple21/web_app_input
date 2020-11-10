from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('kurasi/', include('kurasi.urls', namespace='blogs')),
    path('', views.welcome, name='home'),
    path('addlink/', views.addlink, name='addlink'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
