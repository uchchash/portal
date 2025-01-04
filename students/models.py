from django.db import models
import os
import random
import string

# A basic student model

class Countries(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class University(models.Model):
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="univerisities/profile/")
    application_fee = models.IntegerField()
    enrollment_deposit = models.IntegerField()
    website = models.URLField()
    language_requirement = models.TextField()
    academic_requirement = models.TextField()

    def __str__(self):
        return self.name
    
class Subjects(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    email_password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    desired_country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    ssc_certificate = models.FileField(upload_to="students/ssc/certificate/", blank=True, null=True)
    ssc_transcript = models.FileField(upload_to="students/ssc/transcript/", blank=True, null=True)
    hsc_certificate = models.FileField(upload_to="students/hsc/certificate/", blank=True, null=True)
    hsc_transcript = models.FileField(upload_to="students/hsc/transcript/", blank=True, null=True)
    bachelor_certificate = models.FileField(upload_to="students/bachelor/certificate/", blank=True, null=True)
    bachelor_transcript = models.FileField(upload_to="students/bachelor/transcript/", blank=True, null=True)
    masters_certificate = models.FileField(upload_to="students/masters/certificate/", blank=True, null=True)
    masters_transcript = models.FileField(upload_to="students/masters/transcript/", blank=True, null=True)
    language_certificate = models.FileField(upload_to="students/language/", blank=False, null=True)
    bank_statement = models.FileField(upload_to="students/bank/", blank=True, null=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class PrimaryStatus(models.Model):
    status = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.status
    
class SecondaryStatus(models.Model):
    status = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.status

class Application(models.Model):
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    p_status = models.ForeignKey(PrimaryStatus, on_delete=models.CASCADE)
    s_status = models.ForeignKey(SecondaryStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.student


