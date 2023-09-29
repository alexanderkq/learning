from django import forms


class BuySellForm(forms.Form):
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'readonly': 'readonly'}))
    amount = forms.IntegerField()


class BuySellForm1(forms.Form):
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'readonly': 'readonly'}))
    amount = forms.IntegerField()