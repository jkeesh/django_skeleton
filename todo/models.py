from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    Extension of the basic Django User
    """
    user            =       models.OneToOneField(User)
    bio             =       models.CharField(max_length=255, blank=True, null=True, default="")

    def __unicode__(self):
        return "%s" % self.user