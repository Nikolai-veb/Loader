from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import ImageCreatedForm, ResizingImageForm
from .models import Images
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.base import View


class ImagesListView(ListView):
    """ List Images"""
    model = Images
    template_name = 'gallery/image_list.html'
    context_object_name = 'images_list'


class ImageDetailView(DetailView):
    """Detail Image"""
    model = Images
    template_name = 'gallery/image_detail.html'
    id_field = 'pk'
    context_object_name = 'image_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ResizingImageForm()
        return context


class CreateImageView(CreateView):
    """Create image"""
    model = Images
    form_class = ImageCreatedForm
    template_name = 'gallery/create_image.html'
    success_url = reverse_lazy('image_list')


def resizing(request, slug):
    """Form Resizing"""
    form = ResizingImageForm
    image = get_object_or_404(Images, slug=slug)
    return render(request, "gallery/resizing_image.html", {"form": form, "image": image})


def resizing_handler(request, pk):
    """Resizing Image"""
    if request.method == 'POST':
        form = ResizingImageForm(request.POST)
        image = get_object_or_404(Images, id=pk)
        width = request.POST['width']
        height = request.POST['height']
        image.image_width = width
        image.image_height = height
    return render(request, 'gallery/image_detail.html', {'image_detail': image})


