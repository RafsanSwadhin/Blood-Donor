from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.utils.timezone import now
from django.utils.text import slugify
from django.core.validators import RegexValidator  # Import RegexValidator

class Post(models.Model):
    CATEGORY = (
        ('Donor', 'Donor'),
        ('Recipient', 'Recipient')
    )
    GROUP = (
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
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
        ("Cox's Bazar", "Cox's Bazar"),
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

    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, blank=True)
    details = models.TextField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    city = models.CharField(max_length=100, choices=CITY, default='Dhaka')

    created_at = models.DateTimeField(default=now)
    group = MultiSelectField(max_length=100, max_choices=5, choices=GROUP)

    # New fields
    sex = models.CharField(max_length=10, choices=SEX, default='Male')  # Sex field with choices
    phone_number = models.CharField(
        max_length=14, 
        validators=[RegexValidator(r'^\+8801[3-9]\d{8}$', 'Enter a valid Bangladeshi phone number.')],
        help_text="Enter phone number in the format: +8801XXXXXXXXX",
        default='+8801000000000',  #  default value
    )

    def __str__(self):
        return self.user.username.title() if self.user else self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
