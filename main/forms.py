from django import forms
from .models import Post
from tinymce.widgets import TinyMCE
    
class PostForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    status = forms.CharField()
    class Meta:
        model = Post
        fields = (
            'title', 'category', 'body', 'snippets', 'slug', 'image', 'status')
        error_messages = {
            'slug': {
                'unique': "This url already exists!",
            }
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control ftitle ttest', 'placeholder':'Enter your title here'}),
            'body': TinyMCE(attrs={'class':'tbody', 'placeholder':'Start Writing Your Post Here...'}),
            'snippets': forms.Textarea(attrs={'class':'form-control tsnippet'}),
            'category': forms.Select(attrs={'class':'form-control form-select text-capitalize', 'placeholder':'Select Category'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control m-image-f'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'snippets', 'body', 'slug', 'image', 'status')
        error_messages = {
            'slug': {
                'unique': "This url already exists!",
            }
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control ftitle', 'placeholder':'Enter your title here'}),
            'snippets': forms.Textarea(attrs={'class':'form-control tsnippet'}),
            'category': forms.Select(attrs={'class':'form-control form-select text-capitalize', 'selected':'here'}),
            'body': TinyMCE(attrs={'class':'tbody', 'placeholder':'Start Writing Your Post Here...'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
        }
        
        
