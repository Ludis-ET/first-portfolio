from django.db import models

class Me(models.Model):
    name = models.CharField(max_length=255,null=True)
    nick_name = models.CharField(max_length=255,null=True)
    github = models.URLField(max_length=2000,blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=255,null=True,blank=True)
    linkedin = models.URLField(max_length=2000,blank=True)
    insta = models.URLField(max_length=2000,blank=True)
    telegram = models.URLField(max_length=2000,blank=True)
    whatsup = models.URLField(max_length=2000,blank=True)
    
    def __str__(self):
        return self.name
    
    
class Skill(models.Model):
    person = models.ForeignKey(Me,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    time = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.name



class Project(models.Model):
    person = models.ForeignKey(Me,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(max_length=2000,blank=True)
    github = models.URLField(blank=True,max_length=200)
    disc = models.TextField(max_length=5000,null=True)
    
    def __str__(self):
        return self.name


class Experience(models.Model):
    person = models.ForeignKey(Me,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    discription = models.TextField(max_length=500)
    time = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.name


class Education(models.Model):
    person = models.ForeignKey(Me,on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    discription = models.TextField(max_length=500)
    time = models.CharField(max_length=255,null=True,blank=True)
    
    def __str__(self):
        return self.school



class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    discription = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


