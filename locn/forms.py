from django import forms
from .models import AttLocnMast, AttMastGatTat, AttDetGatTat

class AttLocnMastForm(forms.ModelForm):
    class Meta:
        model = AttLocnMast
        fields = ['locn_code', 'locn_name']

class AttMastGatTatForm(forms.ModelForm):
    class Meta:
        model = AttMastGatTat
        fields = ['empno', 'locn_cd', 'zone', 'dept', 'status']

class AttDetGatTatForm(forms.ModelForm):
    class Meta:
        model = AttDetGatTat
        fields = ['empno', 'name', 'att_dt', 'att_typ']
        widgets = {
            'empno': forms.TextInput(attrs={'placeholder': 'Type empno'}),
        }



# class AttDetGatTatForm(forms.ModelForm):
#     class Meta:
#         model = AttDetGatTat
#         fields = ['empno', 'name', 'att_dt', 'att_typ']