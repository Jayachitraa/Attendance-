from django.urls import path
from .views import att_det_gat_tat_list,create_att_locn_mast,create_att_locn_mast, create_att_mast_gat_tat,create_att_det_gat_tat,index,att_mast_gat_tat_list,att_locn_mast_list,att_det_gat_tat_edit

urlpatterns = [
    path('index/', index, name='index'),
    path('att_det_gat_tat_list/', att_det_gat_tat_list, name='att_det_gat_tat_list'),
    path('att_mast_gat_tat_list/', att_mast_gat_tat_list, name='att_mast_gat_tat_list'),
    path('att_locn_mast_list/', att_locn_mast_list, name='att_locn_mast_list'),
    path('create_att_locn_mast/', create_att_locn_mast, name='create_att_locn_mast'),
    path('create_att_mast_gat_tat/', create_att_mast_gat_tat, name='create_att_mast_gat_tat'),
    path('create_att_det_gat_tat/', create_att_det_gat_tat, name='create_att_det_gat_tat'),
    path('att_det_gat_tat_edit/<int:empno>/', att_det_gat_tat_edit, name='att_det_gat_tat_edit'),
]

