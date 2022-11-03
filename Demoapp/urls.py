from django.urls import path

from Demoapp import views

urlpatterns=[
    path('',views.frontpg,name='frontpg'),
    path('add_todo',views.add_todo,name='add_todo'),
    path('viewf', views.viewf, name='viewf'),
    path('update/<int:id>/', views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')

]