from django import forms





class EntryForm(forms.Form):
   
        print(forms.Form)
        file_upload=forms.FileField(label='file')
        
        
class UploadEntryForm(forms.Form):
   
        print(forms.Form)
        file_upload=forms.FileField(label='file')
        client_name = forms.CharField(max_length=4,label='client')
        
        
    