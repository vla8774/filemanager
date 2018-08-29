from django.shortcuts import render, get_object_or_404
from .models import FilePost, SubjectFiles


def post_file(request):
    posts = FilePost.objects.all()
    return render(request, 'file/post_file.html', {'posts': posts})
    get_base_menu()

def subject_detail(request, pk):
    post = get_object_or_404(SubjectFiles, pk=pk)
    return render(request, 'file/subject_file.html', {'posts': post})


def get_base_menu(request):
    post = SubjectFiles.objects.all()
    return render(request, 'blog/base_menu.html', {'menu': post})


def subject_all(request):
    subject = SubjectFiles.objects.all()
    return render(request, 'file/subject_all.html', {'subject': subject})



'''def subject_all(request):
    posts = get_object_or_404(SubjectFiles, pk=1)
    return render(request, 'blog/subject_all.html', {'subject': posts})'''
