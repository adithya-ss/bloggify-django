from django.urls import path
# from . import views
from .views import Home, Details, NewPost, UpdatePost, DeletePost, NewCategory, CategoryView, CategoryMenuView, NewComment

urlpatterns = [
    # Adding different URL paths for proper navigation.
    # path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('blog/<int:pk>', Details.as_view(), name="blog_detail"),
    path('new_post/', NewPost.as_view(), name="new_post"),
    path('blog/edit/<int:pk>', UpdatePost.as_view(), name="edit_post"),
    path('blog/<int:pk>/delete', DeletePost.as_view(), name="delete_post"),
    path('new_category/', NewCategory.as_view(), name="new_category"),
    path('category/<str:ctg>/', CategoryView, name="blog_category"),
    path('category_list/', CategoryMenuView, name="category_list"),
    path('blog/<int:pk>/comment/', NewComment.as_view(), name="new_comment"),
]