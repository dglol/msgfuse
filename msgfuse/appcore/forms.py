from django import forms
from django.core.exceptions import ValidationError
import re

dateChoices = ('InitialDate','EndDate')
ViewChoices = ('OpeningClicks','ClosingClicks')

def validate_int(value):
    if not re.match(r'^([0-9])*$',value):
        raise ValidationError(u'Please have an appropriate value for views')
    
class DateForm(forms.Form):
	dateType = forms.CharField(widget=forms.Select(choices=dateChoices))
	dateValue = forms.DateField()

class ViewForm(forms.Form):
	RequiredViews = forms.CharField(required=False, label="", max_length=8, validators = [validate_int])
	ClosingViews = forms.CharField(required=False, label="", max_length=8, validators = [validate_int])
	
class MessageForm(forms.Form):
	msgValue = forms.CharField(label="", widget=forms.Textarea, max_length=500, error_messages={'invalid': 'Please have a Message'})
