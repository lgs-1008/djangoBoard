from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView
from board.models import Board
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from board.form import CreateBoardForm
from django.http import Http404
from datetime import datetime
# Create your views here.
class BoardListView(generic.ListView):
    model = Board
    paginate_by = 20
    template_name = 'board/BoardList.html'

class BoardDetailView(generic.DetailView):
    model = Board
    template_name = 'board/BoardDetail.html'

@login_required
def BoardWriteView(request):
    if request.method == 'POST':
        form = CreateBoardForm(request.POST)
        if form.is_valid():
            reqUser = request.user
            reqProfile = Profile.objects.get(user=reqUser)

            item = form.save(commit=False)
            item.writer = reqProfile.nick
            item.save()

            return redirect(reverse_lazy('board:boardList'))

    else:
        form = CreateBoardForm()

    return render(request, 'board/BoardWrite.html', {'form' : form})

@login_required
def BoardEditView(request, pk):
    editBrd = get_object_or_404(Board, pk = pk)
    reqUser = request.user
    nick = Profile.objects.get(user=reqUser).nick

    if nick != editBrd.writer:
        raise Http404("permissions denied, It is not your writing. 당신의 글이 아닙니다.")

    if request.method == 'POST':
        form = CreateBoardForm(request.POST, instance=editBrd)


        if form.is_valid():
            editBrd = form.save(commit=False)
            editBrd.createTime = datetime.now()
            editBrd.save()
            return redirect(reverse_lazy('board:boardList'))

    else:
        title = editBrd.title
        content = editBrd.contents
        form = CreateBoardForm(initial={'title': title, 'contents':content})

    return render(request, 'board/BoardWrite.html', {'form' : form})

def BoardDeleteView(request, pk):
    reqUser = request.user
    nick = Profile.objects.get(user=reqUser).nick
    try:
        item = Board.objects.get(pk=pk)
        if item.writer == nick:
            item.delete()
        else:
            raise Http404("당신의 게시글이 아닙니다. Not your Post.")

    except Board.DoesNotExist:
        raise Http404("???")

    return redirect('board:boardList')
