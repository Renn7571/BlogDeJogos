from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('<slug:slug>/', views.post_details, name='post_details')

    # path('login/', views.user_login, name='login'),
]