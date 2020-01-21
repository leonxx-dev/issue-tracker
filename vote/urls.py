from django.urls import path
from .views import results, vote

urlpatterns = [
    path('<int:ticket_id>/results/', results, name='results'),
    path('<int:ticket_id>/vote/', vote, name='vote'),
]