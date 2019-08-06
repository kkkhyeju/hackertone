"""hakertone URL Configuration

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
from django.urls import path
from hakertoneapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginhome,name='loginhome'),
    path('login/',views.login,name='login'),
    path('index',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('maketeam/',views.maketeam,name='maketeam'),
    path('findteam/',views.findteam,name='findteam'),
    path('ad_page/',views.ad_page,name='ad_page'),
    path('create/',views.create,name='create'),

]
