from django.conf.urls import url 
from employee import views 
from django.urls import path,include
urlpatterns = [ 
    path('', views.employee_list,name="employee_list"),
    path('detail/<str:pk>', views.employee_detail,name="detail"),
    path('create', views.employee_create,name="create"),
    path('update/<str:pk>', views.employee_update,name="update"),
    path('delete/<str:pk>', views.employee_delete,name="delete"),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #url(r'^api/tutorials/published$', views.tutorial_list_published)
]
