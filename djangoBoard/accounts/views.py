from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from accounts.form import UserCreationMultiForm
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.http import Http404
# Create your views here.
class SingUp(generic.CreateView):
    form_class = UserCreationMultiForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        user = form['user'].save()
        profile = form['profile'].save(commit=False)
        profile.user = user
        profile.save()
        return redirect(reverse('login'))

@login_required
def userinfo(request):
    reqUser = request.user
    try:
        reqProfile = Profile.objects.get(user=reqUser)
        context = {
            'id' : reqUser.username,
            'nick' : reqProfile.nick,
            'birth_date' : reqProfile.birth_date,
            'aboutMe' : reqProfile.aboutMe,
            }
    except Profile.DoesNotExist:
        raise Http404("프로필 정보를 확인할 수 없는 관리자 계정 Can't verify profile information for manager account")

    return render(request, 'mypage.html', context=context)
