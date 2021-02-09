from django import forms
from inventory.models import Management


class ManagementForm(forms.ModelForm):
    class Meta:
        model = Management
        fields = ['product_name', 'purity','quantity','residual_quantity','manufacturer','storage_location','category','partname','division','author','registration_date','xpiration_date','comment','msds','modify_date']