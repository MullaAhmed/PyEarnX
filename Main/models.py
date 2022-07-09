from django.db import models
from datetime import date
from django.utils.timezone import datetime

# Create your models here.
class UserProfile(models.Model):
    wallet_address = models.CharField("Wallet Address",max_length=1000,unique=True,primary_key=True)
    display_name = models.CharField("Name",max_length=100)
    watch_history=models.JSONField("Watch History")

    def __str__(self):
        return (self.wallet_address)

class ProjectForm(models.Model):
    wallet_address =  models.ForeignKey(to=UserProfile,on_delete=models.CASCADE)
    project_name = models.CharField("Project Name",max_length=200,unique=True,primary_key=True)
    description=models.TextField("Description")
    project_category = models.CharField("Project Category",max_length=200)
    token_name = models.CharField("Token Name",max_length=200)
    token_symbol = models.CharField("Token symbol",max_length=200)
    project_url = models.CharField("Project URL",max_length=1000)
    project_address = models.CharField("Project Address",max_length=1000)
    tokenomics = models.CharField("Tokenomics",max_length=200)
    soft_cap = models.CharField("Soft Cap",max_length=200)
    hard_cap = models.CharField("Hard Cap",max_length=200)
    total_token_supply=models.IntegerField("Total Token Supply")
    total_market_cap=models.FloatField("Total Market Cap")
    taxes=models.FloatField("Taxes")
    liquidity_percentage=models.FloatField("Liquidity Percentage")
    lockup_time=models.CharField("LockUp Time",max_length=200)
    project_to_launch=models.CharField("LockUp Time",max_length=200)
    project_launch_platform=models.URLField()

    def __str__(self):
        return (self.project_name)


class Video(models.Model):
    video_name =  models.CharField("Video Name",max_length=200,unique=True,primary_key=True)
    display_video_name=  models.CharField("Video Name",max_length=200)
    project_name = models.ForeignKey(to=ProjectForm,on_delete=models.CASCADE)
    likes=models.IntegerField("No. of Likes")
    views=models.IntegerField("No. of Views")
    votes=models.IntegerField("No. of Votes")
    video=models.FileField(upload_to="",blank=True)

    def __str__(self):
        return (self.video_name)
