from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # new
from django.urls import reverse_lazy # new
from .models import Post
from django.core.exceptions import PermissionDenied
from django.http import Http404
import logging


class BlogCreateView(CreateView):
	model = Post
	template_name = "post_new.html"
	fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
	model = Post
	template_name = "post_edit.html"
	fields = ["title", "body"]

class BlogDeleteView(DeleteView): # new
	model = Post
	template_name = "post_delete.html"
	success_url = reverse_lazy("home")




logger = logging.getLogger(__name__)

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error in BlogListView: {str(e)}")
            raise

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            logger.error(f"Error in BlogDetailView: {str(e)}")
            raise