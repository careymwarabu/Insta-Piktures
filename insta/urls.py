from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "insta"

urlpatterns = [
   path('',views.index,name = 'index'),
   path('create_profile/',views.create_profile,name = 'create_profile'),
   path('profile/<profile_id>/',views.profile,name = 'profile'),
   path('email/',views.email, name = 'email'),
   path('upload/image', views.upload_image, name = "upload_image"),
   path('search/',views.search,name ='search'),
   path('like/<image_id>/', views.like_image, name = 'like_image'), 
   path('comment/<image_id>/', views.comment,name = "comment"),
   path('profile/edit', views.profile_edit,name = 'profile_edit'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)