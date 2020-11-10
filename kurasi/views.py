from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Kurasi


def handler404(request):
    return render(request, '404.html', status=404)

def index(request):
    kurasi = Kurasi.objects.all()
    return render(request, 'kurasi/index.html', {'kurasi' : kurasi})

def single(request, id):
    blog = get_object_or_404(Kurasi, pk=id)
    return render(request, 'kurasi/single.html', {'blog' : blog})

def comment(request, id):
    blog = get_object_or_404(Kurasi, pk=id)

    if request.method == 'POST':
        newDesc = request.POST['desc']

        if len(newDesc) < 10:
            return render(request, 'kurasi/single.html', {
                            'blog' : blog,
                            'errors' : 'Komentar Minimal 10 Karakter'
            })

        blog.comment_set.create(desc=newDesc)
        return HttpResponseRedirect('/kurasi')
