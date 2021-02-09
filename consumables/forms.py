from django import forms
from consumables.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['item_code','product_name','manufacturer','storage_location','team_name','quantity','category','safety_stock','note']

        widgets = {
            'item_code': forms.TextInput(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'manufacturer': forms.TextInput(attrs={'class': 'form-control'}),
            'storage_location': forms.TextInput(attrs={'class': 'form-control'}),
            'team_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'safety_stock': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }

        labels = {
            'item_code': '품목코드',
            'product_name': '제품명',
            'manufacturer': '제조사',
            'storage_location': '보관위치',
            'team_name': '부서명',
            'quantity': '수량',
            'category': '카테고리',
            'safety_stock': '안전재고',
            'content': '비고',
        }