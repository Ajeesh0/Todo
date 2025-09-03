from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('addtask/',views.addtask,name='addtask'),
    path('Mark_as_done/<int:pk>/',views.Mark_as_done,name='Mark_as_done'),
    path('Mark_as_Undo/<int:pk>/',views.Mark_as_Undo,name='Mark_as_Undo'),

    path('edit_task/<int:pk>/',views.Edit_task,name='edit_task'),

    path('delete_task/<int:pk>/',views.Delete_task, name='delete_task')

]
