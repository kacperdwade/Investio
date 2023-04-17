from django import forms

class AddNewInvestment(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
    img = forms.ImageField(label='img', widget=forms.FileInput(attrs={'name':'images', 'multiple': True}), required=False)
    location = forms.CharField(label="Location", max_length=50)
    about = forms.CharField(label="Description", max_length=200)
    price = forms.FloatField(label="Price")
    ror = forms.IntegerField(label="RoR")
    tor = forms.IntegerField(label="ToR")

