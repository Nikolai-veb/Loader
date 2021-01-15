from urllib.error import URLError, HTTPError

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

    def is_valid(self):
        image = super(ImageCreatedForm, self).is_valid()
        image_url = self.cleaned_data['url']
        image_image = self.cleaned_data['image']
        if image_url and image_image:
            raise forms.ValidationError("Don't allow input of utl and image fields at the same time !!!!!")
        elif image_url == '' and image_image is None:
            raise forms.ValidationError('Empty fields: enter a link or select a file !!!')
        else:
            return self.is_bound

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageCreatedForm, self).save(commit=False)
        image_url = self.cleaned_data['url']

        try:
            if image_url:
                image_name = '{}.{}'.format(slugify(image.title), image_url.split('.', 1)[1].lower())
                response = request.urlopen(image_url)
                image.image.save(image_name, ContentFile(response.read()), save=False)
                if commit:
                    image.save()
        except HTTPError:
            raise forms.ValidationError("This url don't correct")
        return image
