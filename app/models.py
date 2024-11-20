from django.db import models
from django.db import models
# from django.utils import timezone
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    CATEGORY = (
        ('Donor', 'Donor'),
        ('Recipient', 'Recipient')
    )
    GROUP = (
        ('O+','O+'),
        ('O-','O-'),
        ('A+','A+'),
        ('A-','A-'),
    )
    # user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True)
    # salary = models.FloatField()
    details = models.TextField()
    # available = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    created_at = models.DateTimeField(default=now)
    # image = models.ImageField(default='default.jpg', upload_to='tuition/images')
    group = MultiSelectField(max_length=100,max_choices = 5, choices = GROUP)#default='Bangla')
    # subject = models.ManyToManyField(Subject,related_name='subject_set')
    # class_in = models.ManyToManyField(Class_in,related_name='class_set')