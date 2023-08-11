from django.urls import path
from . import views


urlpatterns = [
   
    path('',views.add,name="add"),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('clvhome/',views.tasklistview.as_view(),name="clvhome"),
    path('cdvdetails/<int:pk>/', views.taskdetailview.as_view(), name="cdvdetails"),
    path('cbvupdate/<int:pk>/', views.taskupdateview.as_view(), name="cbvupdate"),
    path('cbvdelete/<int:pk>/', views.taskdeleteview.as_view(), name="cbvdelete"),


    




]