from django.conf import settings 
from django.db import models 
from django.urls import reverse 


class Disruption(models.Model): 
    CATEGORY_CHOICES = [
        ('Maintenance Disruption', 'Maintenance Disruption'),
        ('Material Losses', 'Material Losses'),
        ('Supply Chain Delays', 'Supply Chain Delays'),
        ('Production Related Issues', 'Production Related Issues'),
        ('Quality Related Downtime', 'Quality Related Downtime'),
        ('Line Blockage', 'Line Blockage'),
        ('Line Starvation', 'Line Starvation'),
        ('Other', 'Other'),
    ]
    SECTION_CHOICES = [
        ('Bodyshop & Metal Finish','Bodyshop & Metal Finish'),
        ('Paintshop','Paintshop'),
        ('CV Trimline','CV Trimline'),
        ('Riveting','Riveting'),
        ('N-Series','N-Series'),
        ('F-Series','F-Series'),
        ('Material Handling','Material Handling'),
        ('LCV','LCV'),
        ('EOL','EOL'),
        ('Other','Other'),
    ]
    author = models.ForeignKey( 
    settings.AUTH_USER_MODEL, 
    on_delete=models.CASCADE, 
    ) 
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255) 
    category = models.CharField(
        max_length=255,
        choices=CATEGORY_CHOICES,
    )
    section = models.CharField(
        max_length=255,
        choices=SECTION_CHOICES,
                               ) 
    lotnum = models.CharField(max_length=255) 
    time = models.CharField(max_length=255) 
     
    
    def __str__(self): 
        return self.description 
    def get_absolute_url(self): 
        return reverse("disruption_detail", kwargs={"pk": self.pk}) 