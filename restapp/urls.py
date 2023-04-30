from .views import *
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('todo-view-set', TodoViewSet, basename='todo')

urlpatterns = [

     path("", home),
     path("post-todo/", post_Todo),
     path("get-todo/", get_Todo),
     path("patch-todo/", patch_Todo),
     path('todo/', TodoView.as_view() )
    

]


urlpatterns += router.urls