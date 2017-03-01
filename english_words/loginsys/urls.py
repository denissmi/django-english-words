from django.conf.urls import url
from loginsys import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^login/$', views.log_in, name='log_in'),
    url('^logout/$', views.log_out, name='log_out'),
    url('^register/$', views.register, name='register'),
    url('^password_reset/$', auth_views.password_reset, name='password_reset'),
]