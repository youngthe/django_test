"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from article import views
from study import views as study_views
from django.contrib.auth import views as auth_views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index_view ,name="index"),
    path('', views.ArticleListView.as_view() ,name="index"),
    path('create/', views.ArticleCreateView.as_view() ,name="create"),
    path('detail/<int:pk>', views.ArticleDetailView.as_view() ,name="detail"),
    path('update/<int:pk>', views.ArticleUpdateView.as_view() ,name="update"),
    path('delete/<int:pk>',views.ArticleDeleteView.as_view() ,name="delete"),
    
    path('study/', include('study.urls')),

]