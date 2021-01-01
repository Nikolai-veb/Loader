from django.http import HttpResponse
from django.shortcuts import render
from django.test import TestCase
from gallery.models import Images
from django.urls import reverse
from gallery.forms import ImageCreatedForm, ResizingImageForm


class ImageListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create 13 authors for pagination tests
        number_of_image = 13
        for image_num in range(number_of_image):
            Images.objects.create(title=f'Image {image_num}')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'gallery/image_list.html')

    def test_view_url_accessible_by_name(self):
        image = Images.objects.get(id=1)
        resp = self.client.get(reverse('detail_image', kwargs={"pk": image.id}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'gallery/image_detail.html')

    def test_view_uses_correct_template_resizing(self):
        image = Images.objects.get(id=1)
        resp = self.client.get(reverse('resizing_image', kwargs={'slug': image.slug}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'gallery/resizing_image.html')
