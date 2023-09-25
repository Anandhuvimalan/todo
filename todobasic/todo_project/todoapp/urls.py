from django.urls import path
from . import views
urlpatterns=[
    path('',views.add_task,name='home'),
    path('delete/<int:id>/',views.delete_task,name='delete'),
    path('update/<int:id>/',views.update_task,name='update'),
    path('classhome/',views.TaskView.as_view(), name='classhome'),
    path('classdetail/<int:pk>/',views.TaskDetail.as_view(), name='classdetail'),
    path('classupdate/<int:pk>/',views.TaskUpdate.as_view(), name='classupdate'),
    path('classdelete/<int:pk>/',views.TaskDelete.as_view(), name='classdelete'),
]