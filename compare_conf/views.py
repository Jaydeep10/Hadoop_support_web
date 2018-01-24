# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
#from django.http import HttpResponse
from . import forms
from compare_conf.models import test
# Create your views here.
def cluster_list(request):
    return render (request,'compare_cluster/cluster.html')


def compare_cluster(request):
    form = forms.FormName()
    return render(request,'compare_cluster/forms.html',{'form':form})

def cluster_name(request):
    env_name = test.objects.order_by('env_name')
    env_dict = {'Env_name':env_name}
    return render(request,'compare_cluster/register.html',context=env_dict)
#    url_link = Clusters.objects.order_by('url_link')
