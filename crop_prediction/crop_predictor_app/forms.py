from django import forms

class CropDetailsForm(forms.Form):
    name = forms.CharField(max_length=200, label="Name of Crop")
    nitrogen_content = forms.IntegerField(label="Nitrogen Content")
    phosphorus_content = forms.IntegerField(label="Phosphorus Content")
    potassium_content = forms.IntegerField(label="Potassium Content")
    temperature = forms.IntegerField(label="Temperature")
    humidity = forms.IntegerField(label="Humidity")
    ph = forms.IntegerField(label="PH Value")
    rainfall = forms.IntegerField(label="Rainfall")
    