from django.urls import path
from .import views
from django.contrib.auth import views as authentication_views

app_name='bank'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register, name='register'),
    path('kyc/',views.updatekyc, name='updatekyc'),
    path('login/', authentication_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('welcome/',views.welcome,name='welcome'),
    path('allbranch/',views.allbranch,name="allbranch"),
    path('<slug:c_slug>',views.allbranch, name='by_district'),

]