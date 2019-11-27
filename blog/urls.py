from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #Cette partie est plus compliquée. Cela signifie que Django attend une valeur entière et la transfèrera dans une vue sous forme de variable appelée pk.
    

]