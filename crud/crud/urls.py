
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.stdisplay,name="stdisplay"),
    path('Create',views.stinsert,name="stinsert"),
    path('Edit/<int:id>',views.stedit,name="stedit"),
    path('Update/<int:id>',views.stupdate,name="stupdate"),
    path('Delete/<int:id>',views.stdel,name="stdel")
]






