from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model=Laptop
        fields=('types','price','status','Issues')

class DesktopForm(forms.ModelForm):
    class Meta:
        model=Desktop
        fields=('types','price','status','Issues')


class MobilesForm(forms.ModelForm):
    class Meta:
        model=Mobile
        fields=('types','price','status','Issues')