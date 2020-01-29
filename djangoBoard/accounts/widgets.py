from django import forms
from django.forms import DateTimeInput

class DateInput(forms.DateInput):
    Input_type = 'date'
