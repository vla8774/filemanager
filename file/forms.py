from django import forms

from .models import FilePost, SubjectFiles, Phone
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class PostForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):

    class Meta:
        model = FilePost
        fields = ('title',
                  'description_file_post',
                  'subject_file',
                  'file')


class SubjectForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):

    class Meta:
        model = SubjectFiles
        fields = ('subject_files',
                  'description_subject')


class PhoneForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):

    class Meta:
        model = Phone
        fields = ('published_date',
                  'file')