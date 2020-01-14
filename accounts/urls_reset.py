from django.urls import re_path
from django.contrib.auth.views import PasswordResetView

urlpatterns = [
    re_path(r'^$', PasswordResetView.as_view(), name='password_reset')
]
