from django.shortcuts import render, get_object_or_404, redirect
from bootstrap_modal_forms.mixins import PassRequestMixin
from .forms import *
from .models import *
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin
from django.urls import reverse_lazy
from django.views import generic


def post_file(request):
    data = {}
    get_base_menu(data)
    data["files"] = FilePost.objects.all()
    return render(request, 'file/post_file.html', data)


def get_base_menu(data):
    data["subjects"] = SubjectFiles.objects.all()


def subject_all(request):
    data = {}
    get_base_menu(data)
    data["subject"] = SubjectFiles.objects.all()
    return render(request, 'file/subject_all.html', data)


def subject_detail(request, fl):
    data = {}
    get_base_menu(data)
    data["posts"] = get_object_or_404(SubjectFiles, slug=fl)
    return render(request, 'file/subject_file.html', data)


'''def subject_detail(request, pk):
    post = get_object_or_404(SubjectFiles, pk=pk)
    return render(request, 'file/subject_file.html', {'posts': post})'''
'''def subject_all(request):
    posts = get_object_or_404(SubjectFiles, pk=1)
    return render(request, 'blog/subject_all.html', {'subject': posts})'''


def post_all(request):
    data = {}
    get_base_menu(data)
    data["subjects"] = SubjectFiles.objects.all()
    return render(request, 'file/file_all.html', data)


def file_detail(request, url_post):
    data = {}
    get_base_menu(data)
    data["post"] = get_object_or_404(FilePost, slug=url_post)
    return render(request, 'file/file_detail.html', data)


'''def file_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.published_date = timezone.now()
            post.save()
            return redirect('file_detail', url_post=post.url)
    else:
        form = PostForm()
    return render(request, 'file/file_edit.html', {'form': form})'''


class FileNew(PassRequestMixin, generic.CreateView):
    template_name = 'file/file_edit.html'
    form_class = PostForm
    success_url = reverse_lazy('post_file')


class SubjectNew(PassRequestMixin, generic.CreateView):
    template_name = 'file/subject_new.html'
    form_class = SubjectForm
    success_url = reverse_lazy('post_file')

'''
def file_edit(request, url_post):
    post = get_object_or_404(FilePost, url=url_post)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('file_detail', url_post=post.url)
    else:
        form = PostForm(instance=post)
        return render(request, 'file/file_edit.html', {'form': form})'''


class FileEdit(PassRequestMixin, generic.UpdateView):
    model = FilePost
    template_name = 'file/file_update.html'
    form_class = PostForm
    success_url = reverse_lazy('post_file')


class SubjectEdit(PassRequestMixin, generic.UpdateView):
    model = SubjectFiles
    template_name = 'file/subject_new.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subject_all')


class FileDelete(DeleteAjaxMixin, generic.DeleteView):
    model = FilePost
    context_object_name = 'post'
    template_name = 'file/file_delete.html'
    success_message = 'OK'
    success_url = reverse_lazy('post_file')


class SubjectDelete(DeleteAjaxMixin, generic.DeleteView):
    model = SubjectFiles
    context_object_name = 'subject'
    template_name = 'file/subject_delete.html'
    success_message = 'OK'
    success_url = reverse_lazy('subject_all')


class FileRead(generic.DetailView):
    model = FilePost
    context_object_name = 'post'
    template_name = 'file/file_read.html'


class SubjectRead(generic.DetailView):
    model = SubjectFiles
    context_object_name = 'subject'
    template_name = 'file/subject_read.html'


class PhoneEdit(PassRequestMixin, generic.UpdateView):
    model = Phone
    template_name = 'file/phone_update.html'
    form_class = PhoneForm
    success_url = reverse_lazy('post_file')


def post_phone(request):
    data = {}
    get_base_menu(data)
    data["files"] = Phone.objects.all()
    return render(request, 'file/post_phone.html', data)