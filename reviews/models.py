from django.db import models
from django.conf import settings
import os

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=80)
    content = models.CharField(max_length=80)
    movie = models.CharField(max_length=80)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def image_path(instance, filename):
        return f'profiles/{instance.user.username}/{filename}'
    image = models.ImageField(upload_to=image_path, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kargs):
      if self.image:
          os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
      super(Review, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_post = Review.objects.get(id=self.id)
            if self.image != old_post.image:
                if old_post.image:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_post.image.path))
        super(Review, self).save(*args, **kwargs)