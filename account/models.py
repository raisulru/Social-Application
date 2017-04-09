from django.db import models
from django.conf import settings

class ip(models.Model):
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateField(blank=True, null=True)
	photo = models.ImageField(upload_to='users/%Y/%m/%d',
								blank=True)
	def has_related_object(self):
		return 'Profile for user {}'.format(self.user.username)