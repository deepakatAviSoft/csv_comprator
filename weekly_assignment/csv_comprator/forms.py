from django import forms

class UploadFileForm(forms.Form):
    file1 = forms.FileField(label='Select CSV File 1')
    file2 = forms.FileField(label='Select CSV File 2')
