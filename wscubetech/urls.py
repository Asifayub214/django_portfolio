"""
URL configuration for wscubetech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from wscubetech import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.homePage, name = "home"),      #default url this will be open first    
    path('course/', views.course),
    path('blog_details/', views.blog_details, name = "blog_details"), 
    path('services/', views.servicesData),
    # path('portfolio_details/', views.portfolio_details, name = "portfolio_details"),
    path('blog/', views.blog,  name = "blog"), 
    path('userform/', views.userform,  name = "userform"), 
    path('calculator/', views.calculator,  name = "calculator"), 
    path('newsdetails/<slug>', views.newsDetails),
    path('contact/', views.contact, name='contact'),
    
    
    path('course/<int:courseid>', views.courseDetails),  #dynamic url  int str and slug these three types are used in dynamic urls
    path('course/<str:courseid>', views.courseDetails),  # str type
    path('course/<slug:courseid>', views.courseDetails), # slug type
    path('course/<courseid>', views.courseDetails),      # if you did not know value type than dont use any type
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)