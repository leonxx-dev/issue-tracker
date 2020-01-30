from django.urls import path
from .views import request_vote

urlpatterns = [
    path('<int:pk>/vote/', request_vote, name='request_vote'),
]