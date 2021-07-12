from django.test import TestCase
from .models import Profile,Image,Comment,Follow
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.carey = User(username = "carey", email = "carey@gmail.com", password = "12345")
        self.profile = Profile(bio='bio', user=self.carey)
        self.book = Image(image = 'imageurl', name ='book', caption = 'True', profile = self.profile)
        self.food = Image(image = 'imageurl', name ='chicken', caption = 'Delicious', profile = self.profile)

        self.carey.save()
        self.profile.save()
        self.food.save_image()

    def tearDown(self):
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.food, Image))

    def test_save_image_method(self):
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    def test_delete_image(self):
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.food.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    def test_update_caption(self):
        self.food.update_caption('Pasta')
        self.assertEqual(self.food.caption, 'Pasta')

    def test_get_profile_images(self):
        self.book.save_image()
        images = Image.get_profile_images(self.profile)
        self.assertEqual(len(images),2)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.carey = User(username = "carey", email = "carey@gmail.com",password = "12345")
        self.profile = Profile(bio='bio', user= self.carey)
        self.carey.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.carey, User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_search_user(self):
        user = Profile.search_user(self.carey)
        self.assertEqual(len(user), 1)

class CommentTestClass(TestCase):
    def setUp(self):
        self.carey = User(username = "carey", email = "carey@gmail.com",password = "1234")
        self.profile = Profile(bio='bio', user= self.carey)
        self.food = Image(image = 'imageurl', name ='food', caption = 'Chicken', profile = self.profile)
        self.comment = Comment(image=self.food, content= 'Looks delicious', user = self.carey)

        self.carey.save()
        self.profile.save()
        self.food.save_image()
        self.comment.save_comment()

    def tearDown(self):
        Image.objects.all().delete()
        Comment.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        comments = Comment.objects.all()
        self.assertTrue(len(comments)> 0)

    def test_delete_comment(self):
        comments1 = Comment.objects.all()
        self.assertEqual(len(comments1),1)
        self.comment.delete_comment()
        comments2 = Comment.objects.all()
        self.assertEqual(len(comments2),0)

    def test_get_image_comments(self):
        comments = Comment.get_image_comments(self.food)
        self.assertEqual(comments[0].content, 'Amazing')
        self.assertTrue(len(comments) > 0)

class FollowTestClass(TestCase):
    def setUp(self):
        self.carey = User(username = "carey", email = "carey@gmail.com",password = "1234")
        self.profile1 = Profile(bio='bio', user= self.carey)        
        self.mwaka = User(username = "mwaka", email = "mwaka@gmail.com",password = "1234")
        self.profile2 = Profile(bio='bio', user= self.mwaka) 
        self.carey.save()
        self.mwaka.save()
        self.follow = Follow (followed = self.profile1, follower = self.profile2 )
        
    def tearDown(self):
        Profile.objects.all().delete()        
        User.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.follow,Follow))