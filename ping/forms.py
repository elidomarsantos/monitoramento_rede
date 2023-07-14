from django import forms

from .models import Equipamentos

class DateInput(forms.DateInput):
    input_type = 'date'
    

class Form_Equipamentos(forms.ModelForm):

    class Meta:
        model = Equipamentos
        fields = '__all__'
       



          

