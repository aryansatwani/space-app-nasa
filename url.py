from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "main"
urlpatterns = [
    path('', views.home, name="home"),
    path('discussion/', views.discussion, name="discussion"),
    path('register/', views.user_registration, name='register'),
]
urlpatterns += staticfiles_urlpatterns()
