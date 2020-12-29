from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image


class Images(models.Model):
    """"Model Images"""
    title = models.CharField("Заголовок", max_length=300)
    image = models.ImageField("Изображение",
                              upload_to='images/',
                              blank=True,
                              width_field='image_width',
                              height_field='image_height'
                              )
    url = models.URLField(blank=True)
    created = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=400, db_index=True, unique=True)
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default='400')
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default='400')

    def get_absolute_url(self):
        return reverse("image_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображении'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, self.created)
        super(Images, self).save(*args, **kwargs)
