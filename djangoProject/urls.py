
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    url('signup/', views.signup_view, name="signup"),
    url('login/', views.login_view, name="login"),
    url('logout/', views.logout_view, name="logout"),
    url('drzave/', views.drzave_view, name="drzave")
]

