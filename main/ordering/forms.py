from .models import Product
from django.forms import ModelForm 

class add_productform(ModelForm):
    class Meta:
        model=Product
        fields= "__all__"

    def __init__(self,*args,**kwargs):
        super(add_productform, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields['name'].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['price'].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields['category'].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields["description"].widget.attrs.update({
                    "class":"form-control"
            })
            self.fields['image'].widget.attrs.update({
                'class': 'form-control'
            })
