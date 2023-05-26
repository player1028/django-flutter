from django.urls import path
from . import views


urlpatterns = [
	path('', views.getRoutes),
	path('notes/', views.getNotes),
	path('notes/create/', views.createNote),
	path('notes/<int:id>/update/', views.updateNote),
	path('notes/<int:id>/delete/', views.deleteNote),
	path('notes/<int:id>/', views.getNote),

]