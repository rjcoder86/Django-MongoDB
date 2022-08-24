from django.urls import path
from . import views

urlpatterns=[
    # path('',views.allblogs,name='allblogs'),
    # path('create',views.create,name='create'),
    # path('update',views.update,name='update'),
    # path('delete',views.delete,name='delete'),

    path('',views.BlogsList.as_view(),name='home'),
    path('create',views.BlogCreate.as_view(),name='create'),
    path('update/<int:pk>',views.BlogUpdate.as_view(),name='update'),
    path('delete/<int:pk>',views.BlogDelete.as_view(),name='delete'),
    path('get/<int:pk>',views.GetBlog.as_view(),name='getblog'),
]