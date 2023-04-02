from django.urls import path
from . import views

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbviewhome/', views.Tasklistview.as_view(), name='cbviewhome'),
    path('cbviewdetail/<int:pk>/', views.Taskdetailview.as_view(), name='cbviewdetail'),
    path('cbviewupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbviewupdate'),
    path('cbviewdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbviewdelete'),
]
