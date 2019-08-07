from django.urls import path
from . import views

app_name = 'bloag'

urlpatterns = [
    path('api/get_friends', views.getFriends, name='getFriends'),
    path('api/get_head_list', views.getHeaderList, name='getHeaderList'),
    path('api/push_artical', views.pushArtical, name='pushArtical'),
    path('api/get_artical_list', views.getArticalList, name='getArticalList'),
    path('api/get_artical_type_list', views.getArticalTypeList, name='getArticalTypeList'),
    path('api/get_all_artical', views.getAllArtical, name='getAllArtical'),
    path('api/delete_artical', views.deleatArtical, name='deleatArtical'),
    path('api/get_draft_artical', views.getDraftArtical, name='getDraftArtical'),
    path('api/get_artical_id', views.getArticalId, name='getArticalId')
]