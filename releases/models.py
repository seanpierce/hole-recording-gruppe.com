from django.db import models
from ckeditor.fields import RichTextField


class Release(models.Model):
	id = models.AutoField(primary_key=True)
	created_at = models.DateTimeField(auto_now=True)
	artist = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	catalog = models.CharField(max_length=12)
	info = RichTextField()
	bandcamp_embed = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)
	release_date = models.DateField()
	preorder_date = models.DateField(null=True)

	class Meta:
		ordering = ['-id',]

	def __str__(self):
		return f'{self.catalog} - {self.artist}, {self.title}'
	
	
class Image(models.Model):
	image = models.ImageField(upload_to='uploads/releases/')
	alt_text = models.CharField(max_length=255, null=True, blank=True)
	release = models.ForeignKey(Release, on_delete=models.CASCADE)