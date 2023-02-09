from django.db import models
from django.urls import reverse


# Create your models here.
class Branch(models.Model):
    place= models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    slug= models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.district

    def get_url(self):
        return reverse('bank:by_district',args=[self.slug])

    class Meta:
        ordering= ('place',)
        verbose_name = 'branch'
        verbose_name_plural = "branches"

class Customer(models.Model):
    #     'name','dob','gender', 'mobile','email','address','district','branch','type','materials'
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender_choice =[('M','MALE'),('F','FEMALE')]
    gender = models.CharField(max_length=1,choices=gender_choice)
    mobile = models.IntegerField(max_length=12)
    email = models.EmailField()
    address = models.TextField()
    district_list=[('EKM','ERNAKULAM'),('ALP','ALAPUZHA'),('KTM','KOTTAYAM')]
    district = models.CharField(max_length=5,choices=district_list)
    # branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    # type = models.Choices()
    # materials = models.Choices()


