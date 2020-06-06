from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('userPage',views.userPage,name="userPage"),
    path('insert_page',views.insert_page,name="insert_page"),
    path('insert',views.insert,name="insert"),
    path('update_page/<int:field_id>',views.update_page,name="update_page"),
    path('update/<int:field_id>',views.update,name="update"),
    path('delete/<int:field_id>',views.delete,name="delete")
]
