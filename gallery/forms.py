from urllib.error import URLError

from django import forms
from .models import Images
from django.core.files.base import ContentFile
from django.utils.text import slugify
from urllib import request


class ResizingImageForm(forms.Form):
    """Resizing Image """
    height = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "form-control border"}))
    width = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "form-control border"}))


class ImageCreatedForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ("title", "url", "image")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control border"}),
            "url": forms.URLInput(attrs={"class": "form-control border"}),
            "image": forms.FileInput(attrs={"class": ""}),
        }

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageCreatedForm, self).save(commit=False)
        image_url = self.cleaned_data['url']

        if image_url:
            image_name = '{}.{}'.format(slugify(image.title), image_url.split('.', 1)[1].lower())
            response = request.urlopen(image_url)
            image.image.save(image_name, ContentFile(response.read()), save=False)

        if commit:
            image.save()
        return image
