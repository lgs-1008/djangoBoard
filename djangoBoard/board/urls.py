from django.urls import path
from board import views
from board.views import BoardListView, BoardDetailView

app_name = 'board'
urlpatterns = [
    path('', views.BoardListView.as_view(), name = 'boardList'),
    path('<int:pk>/', views.BoardDetailView.as_view(), name = 'boardDetail'),
    #path('write/', views.BoardWriteView, name = 'boardWrite'),
    #path('write/<int:id>/', views.BoardEditView, name = 'boardEdit'),
]
