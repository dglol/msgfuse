from django import forms

dateChoices = ('InitialDate','EndDate')
ViewChoices = ('OpeningClicks','ClosingClicks')

class DateForm(forms.Form):
	dateType = forms.CharField(widget=forms.Select(choices=dateChoices))
	dateValue = forms.DateField()

class ViewForm(forms.Form):
	ViewType = forms.CharField(widget=forms.Select(choices=ViewChoices))
	ViewValue = forms.DateField()
	
class MessageForm(forms.Form):
	msgValue = forms.CharField(max_length=500)
