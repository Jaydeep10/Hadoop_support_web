from django.conf.urls import url
from compare_conf import views

app_name = 'compare_cluster'

urlpatterns = [
    url(r'^lists/$',views.cluster_list,name='home'),
    url(r'^compare/',views.compare_cluster,name='compare'),
    url(r'^user/',views.cluster_name,name='cluster_name'),
]
