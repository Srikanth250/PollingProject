from django.db import models

# Create your models here.
class Poll(models.Model):
	question = models.CharField(max_length=60)
	option1 = models.CharField(max_length=30)
	option2 = models.CharField(max_length=40)
	option3 = models.CharField(max_length=30)
	option1_count = models.IntegerField(default=None)
	option2_count = models.IntegerField(default=None)
	option3_count = models.IntegerField(default=None)
	
	def __str__(self):
		return self.question