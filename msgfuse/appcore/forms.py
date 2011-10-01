from django import forms

dateChoices = ('InitialDate','EndDate')
ViewChoices = ('OpeningClicks','ClosingClicks')

class DateForm(forms.Form):
	dateType = forms.CharField(widget=forms.Select(choices=dateChoices))
	dateValue = forms.DateField()

class ViewForm(forms.Form):
	RequiredViews = forms.CharField(label="", max_length=8)
	ClosingViews = forms.CharField(label="", max_length=8)
	
class MessageForm(forms.Form):
	msgValue = forms.CharField(label="", widget=forms.Textarea, max_length=500)
