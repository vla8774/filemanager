from django.shortcuts import render, get_object_or_404, redirect

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


def add_comment_to_post(request, url_post):
    post = get_object_or_404(FilePost, url=url_post)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('file_detail', url=url_post)
    else:
        form = CommentForm()
    return render(request, 'file/add_comment_to_post.html', {'form': form})