from django import forms
from board.models import Board

class CreateBoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('title', 'contents',) 
