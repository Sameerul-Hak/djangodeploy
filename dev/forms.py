from dev.models import Comments
from django.forms import ModelForm

class Form(ModelForm):
    
    class Meta:
        model = Comments
        fields =['message']
