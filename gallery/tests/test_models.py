from django.test import TestCase

from gallery.models import Images


class ImageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Images.objects.create(title='TestImage')

    def test_title_label(self):
        image = Images.objects.get(id=1)
        image_label = image._meta.get_field('title').verbose_name
        self.assertEqual(image_label, 'Заголовок')

    def test_title_max_length(self):
        image = Images.objects.get(id=1)
        max_length = image._meta.get_field('title').max_length
        self.assertEquals(max_length, 300)

    def test_object_name_is_title(self):
        image = Images.objects.get(id=1)
        expected_object_name = f'{image.title}'
        self.assertEquals(expected_object_name, str(image))

    def test_get_absolute_url(self):
        image = Images.objects.get(id=1)
        self.assertEquals(image.get_absolute_url(), '/1/')