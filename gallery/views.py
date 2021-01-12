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


class ResizingImageView(DetailView):
    """Resizing Image Form"""
    model = Images
    context_object_name = "image"
    slug_field = "slug"
    template_name = "gallery/resizing_image.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ResizingImageForm()
        return context


class ResizingImageHandlerView(View):
    """Handler Resizing Image"""

    def post(self, request, pk):
        """Resizing Image"""
        form = ResizingImageForm(request.POST)
        image = get_object_or_404(Images, id=pk)
        if form.is_valid():
            image.image_width = form.cleaned_data['width']
            image.image_height = form.cleaned_data['height']
        return render(request, 'gallery/image_detail.html', {"image_detail": image})


