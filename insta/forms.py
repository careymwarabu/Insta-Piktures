from django import forms
from .models import Image,Profile,Comment,Follow 
from django.forms import ModelForm

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['created', 'account_holder', 'user', 'followers', 'following']
        
class UploadImageForm(ModelForm):
    class Meta :
        model = Image
        exclude = ['profile', 'post_date', 'likes']

class EditBioForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class FollowForm(ModelForm):
    class Meta:
        model = Follow
        exclude = ['followed', 'follower']

class UnfollowForm(ModelForm):
    class Meta:
        model = Follow
        exclude = ['followed', 'follower']