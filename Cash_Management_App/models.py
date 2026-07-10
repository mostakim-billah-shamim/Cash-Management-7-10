from django.db import models
from django.contrib.auth.models import AbstractUser



class UserModel(AbstractUser):

    def __str__(self):
        return self.username
    



class AddCashModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    source = models.CharField(max_length=120, null=True)
    amount = models.FloatField(null=True)
    description = models.CharField(max_length=420, help_text='Write about your source', null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.source




class ExpenseModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)
    reason = models.CharField(max_length=120, null=True)
    amount = models.FloatField(null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.reason
