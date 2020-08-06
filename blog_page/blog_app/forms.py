from django import forms
from .models import Post, Category, Comment

# Hard-code category entries for dropdown
# cat_choices = [('Science','Science'), ('Arts','Arts'), ('Sports','Sports'), 
# ('Indian Economics','Indian Economics'), ('Popular Quotes','Popular Quotes')]

cat_choices = Category.objects.all().values_list('category_name','category_name')

choice_list = []

for each_item in cat_choices:
    choice_list.append(each_item)

# Including forms to add a new blog post.
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('blog_title','blog_page_header','blog_author', 'blog_category', 'blog_body', 'blog_image')

        widgets = {
            'blog_title' : forms.TextInput(attrs={'class': 'form-control'}),
            'blog_page_header' : forms.TextInput(attrs={'class': 'form-control'}),
            'blog_author' : forms.Select(attrs={'class': 'form-control'}),
            'blog_category' : forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'blog_body' : forms.Textarea(attrs={'class': 'form-control'}),
        }

# Including forms to update an existing blog post.
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('blog_title','blog_page_header','blog_author','blog_body')
        fields = ('blog_title','blog_page_header','blog_body')

        widgets = {
            'blog_title' : forms.TextInput(attrs={'class': 'form-control'}),
            'blog_page_header' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'blog_author' : forms.Select(attrs={'class': 'form-control'}),
            'blog_body' : forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user_name','comment_body')

        widgets = {
            'user_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'comment_body' : forms.Textarea(attrs={'class': 'form-control'}),
        }