from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


# class WishList(models.Model):
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, unique=True, blank=True)
#     description = models.TextField(blank=True, null=True)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wishlists')
#     wishes = models.ManyToManyField('Wish', related_name='wishlists', blank=True)
#     is_public = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = ['-created_at']
#         verbose_name = 'Wish List'
#         verbose_name_plural = 'Wish Lists'
#
#     def __str__(self):
#         return self.name
#
#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super().save(*args, **kwargs)
#
#     def get_absolute_url(self):
#         return reverse('wishlist_detail', kwargs={'slug': self.slug})

class CustomUser(AbstractUser):
    pass



class Wish(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='wish_images/', blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='wishes')


    def __str__(self):
        return self.title

