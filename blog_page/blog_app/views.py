from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, UpdateForm, CommentForm
from django.urls import reverse_lazy

# def home(request):
    # Rendering the home page for the django application.
    # return render(request, 'home.html', {})

# Creating specific classes for that perticular URL/webpage.

class Home(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-blog_pub_date']

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(Home, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

def CategoryMenuView(request):
    category_menu_list = Category.objects.all()
    return render(request, 'category_blog_list.html', {'category_menu_list':category_menu_list})

def CategoryView(request, ctg):
    posts_for_ctg = Post.objects.filter(blog_category=ctg)
    return render(request, 'category_blog.html', {'ctg':ctg.title(), 'posts_for_ctg': posts_for_ctg})

class Details(DetailView):
    model = Post
    template_name = 'blog_details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(Details, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context

class NewPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('blog_title', 'blog_author', 'blog_body')

class NewCategory(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'edit_post.html'
    # fields = ['blog_title', 'blog_page_header', 'blog_body']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class NewComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'new_comment.html'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')
    # fields = '__all__'

    
