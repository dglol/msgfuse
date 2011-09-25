from django import forms

dateChoices = ('InitialDate','EndDate')
ViewChoices = ('OpeningClicks','ClosingClicks')

class DateForm(forms.Forms)
	dateType = forms.CharField(widget=forms.Select(choices=dateChoices))
	dateValue = forum.DateField()

class ViewForm(forms.Forms)
	ViewType = forms.CharField(widget=forms.Select(choices=ViewChoices))
	ViewValue = forum.DateField()
	
class MessageForm(forms.Forms)
	msgValue = forum.CharField()