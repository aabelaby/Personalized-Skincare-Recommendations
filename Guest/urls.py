from django.urls import path,include
from Guest import views
app_name='Guest'

urlpatterns = [
   path('UserRegistration/',views.UserRegistration, name="UserRegistration"),
   path('Login/',views.Login, name="Login"),
   path('',views.Index, name="Index"),
   path('Logout',views.Logout, name="Logout"),


]
