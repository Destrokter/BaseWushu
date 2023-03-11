from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

# from django.contrib.auth.views import (
#     LogoutView, 
#     PasswordResetView, 
#     PasswordResetDoneView, 
#     PasswordResetConfirmView,
#     PasswordResetCompleteView
# )

urlpatterns = [
    path('logout/', views.logout_user,  name='logout'),
    path('login/', views.LoginUser. as_view(),  name='login'),
    path('register/', views.RegisterFormView. as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
#     # path('password-reset/', PasswordResetView.as_view(template_name='login/password_reset.html'),name='password-reset'),
#     # path('password-reset/done/', PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'),name='password_reset_done'),
#     # path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='ogin/password_reset_confirm.html'),name='password_reset_confirm'),
#     # path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'),name='password_reset_complete'),
#     # path('password-reset/', 
#     #  PasswordResetView.as_view(
#     #     template_name='login/password_reset.html',
#     #     html_email_template_name='login/password_reset_email.html'
#     # ),
#     # name='password-reset'
# )
]