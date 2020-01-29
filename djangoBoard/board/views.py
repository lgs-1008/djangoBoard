from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from board.models import Board
# Create your views here.
class BoardListView(generic.ListView):
    model = Board
    paginate_by = 20
    template_name = 'board/BoardList.html'

class BoardDetailView(generic.DetailView):
    model = Board
    template_name = 'board/BoardDetail.html'
