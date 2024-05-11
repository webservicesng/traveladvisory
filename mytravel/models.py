# travel/models.py
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Country(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='location_images/')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def short_location_description(self):
        return self.description[:200] + "..."


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    top_category = models.BooleanField(default=True)
    cat_image = models.ImageField(upload_to='cat_images/',blank=True, null=True)

    
    def __str__(self):
        return self.name

class TravelAdvice(models.Model):
    title = models.CharField(max_length=200)
    rich_description = RichTextField(null=True, blank=True)

    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='travel_advice_images/')

    categories = models.ManyToManyField(Category)  # many-to-many field
    advice_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)  # foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def shortened_description(self):
        return self.description[:200] + "..."
    
    
class TourService(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class JobListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    employer = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)