"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from home import views
from django.conf import settings
from django.conf.urls.static import static
from home.views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeletelView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.home,name='home'),
    path('post/',PostListView.as_view(),name='post'),
    path('profile/',views.profile,name='profile'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',PostDeletelView.as_view(),name='post-delete'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('homepage/',views.homepage,name='homepage'),
    path('register/',views.register,name='register'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name = 'password-reset.html'),name='password_reset'), 
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name = 'password-reset-done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'password-reset-confirm.html'),name='password_reset_confirm'),
    path('login/',views.login,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)