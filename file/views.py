from django.shortcuts import render, get_object_or_404, redirect
from bootstrap_modal_forms.mixins import PassRequestMixin
from .forms import *
from .models import *


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
    data["posts"] = get_object_or_404(SubjectFiles, subject_files=fl)
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
    return None


def file_detail(request, url_post):
    data = {}
    get_base_menu(data)
    data["post"] = get_object_or_404(FilePost, url=url_post)
    return render(request, 'file/file_detail.html', data)


'''class FileNew(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    template_name = 'file/file_edit.html',
    form_class = PostForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('index')'''


def file_new(request):
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
    return render(request, 'file/file_edit.html', {'form': form})


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
        return render(request, 'file/file_edit.html', {'form': form})