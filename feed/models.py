from django.db import models
from user.models import *

# Create your models here.
class PostMedia(models.Model):
    image = models.ImageField(upload_to= 'post_images/', blank = True, null = True)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ForeignKey(PostMedia, on_delete = models.SET_NULL)
    content = models.TextField()
    timestamp = models.TimeField()
    reaction = models.ForeignKey('Reaction', on_delete = models.SET_NULL)
    comments = models.ForeignKey('Comment', on_delete = models.SET_NULL)
    share = models.IntegerField()
    is_business_post = models.BooleanField(default = False, verbose_name = 'Business Post')
    is_personal_post = models.BooleanField(default = True, verbose_name = 'Personal Post')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    content = models.TextField()
    reaction = models.ForeignKey('Reaction', on_delete = models.SET_NULL)
    timestamp = models.TimeField()


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE)
    content = models.TextField()
    reaction = models.ForeignKey('Reaction', on_delete = models.SET_NULL)
    
class Reaction(models.Model):
    is_like = models.BooleanField(default = False, verbose_name='Like', null= True, blank= True)
    is_dislike = models.BooleanField(default = False, verbose_name='Dislike', null = True, blank = True)
    is_love = models.BooleanField(default = False,verbose_name='Love', null = True, blank = True)
    is_sad = models.BooleanField(default = False,verbose_name='Sad', null = True, blank = True)
    is_angry = models.BooleanField(default = False,verbose_name='Angry', null = True, blank = True)
    is_haha = models.BooleanField(default = False,verbose_name='Haha', null = True, blank = True)
    is_wow = models.BooleanField(default = False,verbose_name='Wow', null = True, blank = True)
    is_others = models.BooleanField(default = False,verbose_name='Others', null = True, blank = True)


class Repost(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete = models.SET_NULL)
    timestamp = models.TimeField()
    reaction = models.ForeignKey('Reaction', on_delete = models.SET_NULL)
    comments = models.ForeignKey('Comment', on_delete = models.SET_NULL)
    
class SavedPost(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.SET_NULL)
    timestamp = models.TimeField()
    
    