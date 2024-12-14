from django.urls import path
from .views import registration_view ,post,postview,post_detail_view,filtered_post_view,post_delete_view,post_edit_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('post/',post , name = 'post'),
    path('postview/',postview , name = 'postview'),
    path('posts/<int:pk>/', post_detail_view, name='post_detail_view'),
    path('post/filter/', filtered_post_view, name='filtered_post_view'),
    path('post/<int:pk>/edit/', post_edit_view, name='post_edit_view'),
    path('post/<int:pk>/delete/', post_delete_view, name='post_delete_view'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('registration/', registration_view, name='registration'),
    
]