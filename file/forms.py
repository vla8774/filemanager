from django import forms

from .models import FilePost


class PostForm(forms.ModelForm):

    class Meta:
        model = FilePost
        fields = ('title',
                  'description_file_post',
                  'subject_file',
                  'file')
