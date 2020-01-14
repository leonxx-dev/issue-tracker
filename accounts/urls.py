from django.urls import re_path, include
from .views import register, profile, logout, login
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^register/$', register, name='register'),
    re_path(r'^profile/$', profile, name='profile'),
    re_path(r'^logout/$', logout, name='logout'),
    re_path(r'^login/$', login, name='login'),
    re_path(r'^change-password/$', auth_views.PasswordChangeView.as_view()),
    re_path(r'^change-password/done/$', auth_views.PasswordChangeDoneView.as_view()),
    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
