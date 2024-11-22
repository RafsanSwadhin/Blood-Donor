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
    CITY = (
    ('Dhaka', 'Dhaka'),
    ('Faridpur', 'Faridpur'),
    ('Gazipur', 'Gazipur'),
    ('Gopalganj', 'Gopalganj'),
    ('Jamalpur', 'Jamalpur'),
    ('Kishoreganj', 'Kishoreganj'),
    ('Madaripur', 'Madaripur'),
    ('Manikganj', 'Manikganj'),
    ('Munshiganj', 'Munshiganj'),
    ('Mymensingh', 'Mymensingh'),
    ('Narayanganj', 'Narayanganj'),
    ('Narsingdi', 'Narsingdi'),
    ('Netrokona', 'Netrokona'),
    ('Rajbari', 'Rajbari'),
    ('Shariatpur', 'Shariatpur'),
    ('Sherpur', 'Sherpur'),
    ('Tangail', 'Tangail'),
    ('Bogra', 'Bogra'),
    ('Joypurhat', 'Joypurhat'),
    ('Naogaon', 'Naogaon'),
    ('Natore', 'Natore'),
    ('Nawabganj', 'Nawabganj'),
    ('Pabna', 'Pabna'),
    ('Rajshahi', 'Rajshahi'),
    ('Sirajgonj', 'Sirajgonj'),
    ('Dinajpur', 'Dinajpur'),
    ('Gaibandha', 'Gaibandha'),
    ('Kurigram', 'Kurigram'),
    ('Lalmonirhat', 'Lalmonirhat'),
    ('Nilphamari', 'Nilphamari'),
    ('Panchagarh', 'Panchagarh'),
    ('Rangpur', 'Rangpur'),
    ('Thakurgaon', 'Thakurgaon'),
    ('Barguna', 'Barguna'),
    ('Barisal', 'Barisal'),
    ('Bhola', 'Bhola'),
    ('Jhalokati', 'Jhalokati'),
    ('Patuakhali', 'Patuakhali'),
    ('Pirojpur', 'Pirojpur'),
    ('Bandarban', 'Bandarban'),
    ('Brahmanbaria', 'Brahmanbaria'),
    ('Chandpur', 'Chandpur'),
    ('Chittagong', 'Chittagong'),
    ('Comilla', 'Comilla'),
    ('Cox\'s Bazar', 'Cox\'s Bazar'),
    ('Feni', 'Feni'),
    ('Khagrachari', 'Khagrachari'),
    ('Lakshmipur', 'Lakshmipur'),
    ('Noakhali', 'Noakhali'),
    ('Rangamati', 'Rangamati'),
    ('Habiganj', 'Habiganj'),
    ('Maulvibazar', 'Maulvibazar'),
    ('Sunamganj', 'Sunamganj'),
    ('Sylhet', 'Sylhet'),
    ('Bagerhat', 'Bagerhat'),
    ('Chuadanga', 'Chuadanga'),
    ('Jessore', 'Jessore'),
    ('Jhenaidah', 'Jhenaidah'),
    ('Khulna', 'Khulna'),
    ('Kushtia', 'Kushtia'),
    ('Magura', 'Magura'),
    ('Meherpur', 'Meherpur'),
    ('Narail', 'Narail'),
    ('Satkhira', 'Satkhira'),
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
    city = models.CharField(max_length=100, choices=CITY)
    created_at = models.DateTimeField(default=now)
    # image = models.ImageField(default='default.jpg', upload_to='tuition/images')
    group = MultiSelectField(max_length=100,max_choices = 5, choices = GROUP)#default='Bangla')
    # subject = models.ManyToManyField(Subject,related_name='subject_set')
    # class_in = models.ManyToManyField(Class_in,related_name='class_set')

    def __str__(self) :
        return self.user.username.title()