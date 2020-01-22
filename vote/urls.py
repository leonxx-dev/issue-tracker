from django.urls import path
from .views import results, request_vote

urlpatterns = [
    path('<int:pk>/results/', results, name='results'),
    path('<int:pk>/vote/', request_vote, name='vote'),
]