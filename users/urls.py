from django.conf.urls import url
from django.contrib.auth import login
from . import views

app_name = "users"
urlpatterns = [
    url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^register/$', views.register, name="register"),
]
