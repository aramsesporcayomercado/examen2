from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.TodoListView.as_view(), name='list'),
    path('add/', views.TodoCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', views.TodoUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='delete'),

    # Filtros
    path('only-ids/', views.TodosOnlyIDs.as_view(), name='only_ids'),
    path('ids-titles/', views.TodosIDsAndTitles.as_view(), name='ids_titles'),
    path('pending/', views.TodosPending.as_view(), name='pending'),
    path('completed/', views.TodosCompleted.as_view(), name='completed'),
    path('ids-user/', views.TodosIDsAndUserID.as_view(), name='ids_user'),
    path('completed-user/', views.TodosCompletedWithUserID.as_view(), name='completed_user'),
    path('pending-user/', views.TodosPendingWithUserID.as_view(), name='pending_user'),
]
