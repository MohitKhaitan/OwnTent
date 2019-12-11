from django.db import models
from django import forms


class User(models.Model):
    """
    Owner model to store the owner's data
    """
    email = models.EmailField()
    phone = models.IntegerField()
    created_on = models.DateTimeField(auto_now=True)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    USER_TYPE = [
        ('O', 'Owner'),
        ('T', 'Tenant')
    ]
    user_type = models.CharField(default='O', max_length=10, choices=USER_TYPE)

    def __str__(self):
        """
        To display Owner's details
        """
        return self.email + " " + self.phone + " " + self.user_type


class UserReview(models.Model):
    """
    Review model to store the user's review
    """
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewer')
    reviewed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewed')
    rating = models.IntegerField()
    user_review = models.CharField(max_length=250)

    def __str__(self):
        """
        To display users details
        """
        return self.reviewer + " " + self.reviewed + " " + self.user_review
