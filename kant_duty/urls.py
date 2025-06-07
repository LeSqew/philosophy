from django.urls import path
from . import views

app_name = 'kant_duty'

urlpatterns = [
    path('', views.ConceptListView.as_view(), name='concept_list'),
    path('concept/<int:pk>/', views.ConceptDetailView.as_view(), name='concept_detail'),
] 