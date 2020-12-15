from django.contrib import admin
from django.urls import path
from . import views 




urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.AddShowView.as_view(),name='addandshow'),
    path('deletedata/<int:id>/',views.UserDeleteView.as_view(),name='deletedata'),
    path('updatedata/<int:id>/',views.UpdateUserData.as_view(),name='updatedata'),

]