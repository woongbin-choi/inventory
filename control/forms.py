from django import forms
from control.models import Takeout


class TakeoutForm(forms.ModelForm):
    class Meta:
        model = Takeout
        fields = ['carry_day', 'carry_team','author','receive_company','receive_tel','receive_user','material_name','material_info','purpose','pack_date','production_capacity','carry_capacity','residual_quantity','delivery','note']

        widgets = {
            'carry_day': forms.DateInput(attrs={'class': 'form-control'}),
            'carry_team': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'receive_company': forms.TextInput(attrs={'class': 'form-control'}),
            'receive_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'receive_user': forms.TextInput(attrs={'class': 'form-control'}),
            'material_name': forms.TextInput(attrs={'class': 'form-control'}),
            'material_info': forms.TextInput(attrs={'class': 'form-control'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'pack_date': forms.DateInput(attrs={'class': 'form-control'}),
            'production_capacity': forms.TextInput(attrs={'class': 'form-control'}),
            'carry_capacity': forms.TextInput(attrs={'class': 'form-control'}),
            'residual_quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'delivery': forms.TextInput(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }