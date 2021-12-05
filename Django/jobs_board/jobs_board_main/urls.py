from django.urls import path
from .views import get_jobs, get_single_job, subscribe

urlpatterns = [
    path('jobs/', get_jobs, name='jobs_view'),
    path('jobs/view/<int:id>/', get_single_job, name='jobs_details'),
    path('jobs/view/<int:id>/subscribe/', subscribe, name='subscribe_view'),
    
]
