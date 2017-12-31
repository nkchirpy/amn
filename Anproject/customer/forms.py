from django import forms
from .models import Contactform

class Contact_form(forms.ModelForm):




    class Meta:
        model = Contactform
        fields = ['name','email_address','organization_name','contact_number','comments']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control is-valid oval_border','placeholder':'Enter your name','id':'form-name','name':'person_name'}),

            'email_address':forms.TextInput(attrs={'class':'form-control is-valid oval_border','type':'email','placeholder':'example@domain.com','id':'form-email'}),

            'organization_name':forms.TextInput(attrs={'class':'form-control is-valid oval_border','placeholder':'Enter your organization name','id':'form-organize'}),

            'contact_number':forms.TextInput(attrs={'class':'form-control is-valid oval_border','type':'None','id':'form-contact'}),

            'comments':forms.Textarea(attrs={'class':'form-control is-valid oval_border1','id':'form-comments',}),

        }
