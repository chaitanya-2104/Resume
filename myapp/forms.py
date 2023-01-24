from  django import forms
from .models import Forms
from polls.models import Qualification
from polls.models import Qualification1
from polls.models import Qualification2
from polls.models import Qualification3

class StudentForms(forms.ModelForm):
    Upload_Documents = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model =Forms
        
        fields = ['Name','Address','Mobile_no','Email','Age','Education','Upload_Documents']

class QualificationForms(forms.ModelForm):

    class Meta:
        model = Qualification
        fields = ['Qualification','University','Institution','Year_of_passing','Percentag']


class QualificationForms1(forms.ModelForm):

    class Meta:
        model = Qualification1
        fields = ['Qualification1','University1','Institution1','Year_of_passing1','Percentag1']

class QualificationForms2(forms.ModelForm):

    class Meta:
        model = Qualification2
        fields = ['Qualification2','University2','Institution2','Year_of_passing2','Percentag2']

class QualificationForms3(forms.ModelForm):

    class Meta:
        model = Qualification3
        fields = ['Qualification3','University3','Institution3','Year_of_passing3','Percentag3']