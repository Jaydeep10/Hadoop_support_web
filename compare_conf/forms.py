from django import forms
from compare_conf.models import test

CLUSTER_CHOICES= [
    ('Radial_prod', 'RDL_PRD'),
    ('Radial_DR', 'RDL_DR'),
    ]
#CLUSTER_CHOICES = []
#for i in test.objects.order_by('env_name'):
#    CLUSTER_CHOICES.append(i.env_name)
class FormName(forms.Form):
    Cluster_First = forms.CharField(widget=forms.Select(choices=CLUSTER_CHOICES))
    Cluser_Second = forms.CharField(widget=forms.Select(choices=CLUSTER_CHOICES))

#class FormName(forms.Form):
#    name = forms.CharField()
#    email = forms.EmailField()
#    text = forms.CharField(widget=forms.Textarea)
