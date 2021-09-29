from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.RegisterView, name='register'),
    path('login/',views.LoginView , name='login'),
    path('logout/',views.LogoutView , name='logout'),
    path('dashboard/',views.DashboardView , name='dashboard'),
    path('',views.DashboardView , name='dashboard'),
    path('forgotpassword/',views.ForgotPasswordView , name='forgotpassword'),
    path('activate/<uidb64>/<token>',views.ActivateView , name='activate'),
    path('resetpassword_validate/<uidb64>/<token>',views.ResetPassword_ValidateView , name='resetpassword_validate'),
    path('resetpassword/',views.ResetPasswordView , name='resetpassword'),

]