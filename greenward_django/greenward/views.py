from django.shortcuts import render, redirect
from .models import Local
from .forms import LocalForm
from django.http import JsonResponse
# Create your views here.

import json

def local_list(request):
    locals = Local.objects.all().values_list('id','name','city','state',)
    locals_list = list(locals)
    print(json.dumps( locals_list))
    return JsonResponse(locals_list, safe=False)

# def local_list(request):
#     locals = Local.objects.all()
#     return render(request, 'greenward/local_list.html',{'locals':locals})

def local_detail(request,pk):
    local = Local.objects.get(id=pk)
    return render(request, 'greenward/local_detail.html',{'local':local})


def local_create(request):
    if request.method == 'POST':
        form = LocalForm(request.POST)
        if form.is_valid():
            local = form.save()
            return redirect('local_detail', pk=local.pk)
    else:
        form = LocalForm()
    return render(request, 'greenward/local_form.html', {'form': form})


def local_edit(request, pk):
    artist = Local.objects.get(pk=pk)
    if request.method == "POST":
        form = LocalForm(request.POST, instance=artist)
        if form.is_valid():
            local = form.save()
            return redirect('local_detail', pk=local.pk)
    else:
        form = LocalForm(instance=artist)
    return render(request, 'greenward/local_form.html', {'form': form})


def local_delete(request, pk):
    Local.objects.get(id=pk).delete()
    return redirect('local_list')
