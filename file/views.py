from django.shortcuts import render, get_object_or_404
from .models import FilePost, SubjectFiles


def post_file(request):
    posts = FilePost.objects.all()
    return render(request, 'file/post_file.html', {'posts': posts})


def subject_detail(request, pk):
    posts = get_object_or_404(SubjectFiles, pk=pk)
    return render(request, 'file/subject_file.html', {'posts': posts})


def subject_all(request):
    posts = SubjectFiles.objects.all()
    return render(request, 'file/subject_all.html', {'posts': posts})


'''def subject_all(request):
    posts = get_object_or_404(SubjectFiles, pk=1)
    return render(request, 'blog/subject_all.html', {'subject': posts})'''
