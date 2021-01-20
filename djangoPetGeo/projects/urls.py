from .views import ProjectListView, ProjectView, GeoPointView

from django.urls import path

urlpatterns = [
    path('projects/', ProjectListView.as_view()),
    path('projects/<int:pk>/', ProjectView.as_view()),
    path('points/', GeoPointView.as_view())
]