from django import forms
from mainapp.models import Contact, NewsLetter
from django.core.validators import MaxValueValidator


class NameForm(forms.Form):
    name = forms.CharField(max_length = 255)
    lastname = forms.CharField(max_length = 255)
    #email = forms.EmailField()
    phone = forms.CharField(max_length = 11)
    message = forms.CharField(widget = forms.Textarea)
    
    
class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = '__all__'
        
        
class NewsLetterForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = '__all__'