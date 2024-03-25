from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Release(models.Model):
	id = models.AutoField(primary_key=True)
	created_at = models.DateTimeField(auto_now=True)
	artist = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	catalog = models.CharField(max_length=12)
	info = CKEditor5Field('Text', config_name='extends')
	bandcamp_embed = models.TextField()
	active = models.BooleanField(default=True)
	release_date = models.DateField()

	class Meta:
		ordering = ['-id',]

	def __str__(self):
		return f'{self.catalog} - {self.artist}, {self.title}'
	
	
class ReleaseImage(models.Model):
    image = models.ImageField(upload_to='uploads/releases/')
    release = models.ForeignKey(Release, on_delete=models.CASCADE)