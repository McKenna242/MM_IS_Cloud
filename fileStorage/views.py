from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
from .forms import fileForm
from .models import fileStorageSchema
from .filters import fileFilter
from .lists import audioExtensionList, videoExtensionList
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.models import User
from urllib.parse import urlencode

import urllib.parse
import os

# Create your views here.

@login_required
def index(request):
    #fileStorage = fileStorageSchema.objects.all()
    fileStorage = fileForm()
    myFilter = fileFilter()
    
    context = {'file': fileStorage, 'myFilter':myFilter}
    
    return render(request, 'fileStorage/index.html', context) #{
        #'show_fileStorage': False,
        #'file': fileStorage
    #})
     
    
@login_required
def uploads(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'uploads.html', context)

@login_required
def upload_file(request):
    context = {}
    if request.method == 'POST':
        
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(uploaded_file.name)
        form = fileForm(request.POST, request.FILES) 
        if form.is_valid():
            _datetime = datetime.now()
            obj = form.save(commit=True)
            obj.fileName, obj.fileType = uploaded_file.name.rsplit(".", 1) #rsplit splits at the last instance of 1 dot
            #obj.fileURL = '/media/'+obj.fileName.replace(" ","%20")+"."+obj.fileType
            obj.fileURL = '/media/'+urllib.parse.quote(obj.fileName+"."+obj.fileType)
            obj.filePath = 'F:/School/Summer2021/Independent Study'+context['url']
            
            #size needs to be a function
            setSize = round(uploaded_file.size/1048576, 2)
            setSize = str(setSize)
            setSize = setSize+'Mb'
            
            obj.size = setSize
            obj.uploadedBy = request.user.id
            obj.uploadDate = datetime.now()#_datetime.strftime("%Y-%m-%d-%H-%M-%S")
            obj.save()
            return redirect('/fileStorage/')
    
    else:
        form = fileForm()

    context = {
        'form': form
    }

    return render(request, 'fileStorage/uploads.html', context)

#file list display
@login_required
def file_list(request):
    
    #grabbing all files in database 
    files = fileStorageSchema.objects.all()
    #filter files according to filter bar
    myFilter = fileFilter(request.GET, queryset=files)
    #returns a new list of files
    files = myFilter.qs
    audioList = audioExtensionList
    videoList = videoExtensionList
    context = {'files': files, 'myFilter':myFilter, 'vidList': videoList, 'audList': audioList}
    
    return render(request, 'fileStorage/index.html', context)
    
def delete_file(request, pk):
    file = fileStorageSchema.objects.get(id=pk)
    if request.method == "POST":
        file.delete()
        return redirect('/fileStorage/')
    
    context = {'item':file}
    return render(request, 'fileStorage/delete.html', context)

def video_play(request, pk):
    files = fileStorageSchema.objects.get(id=pk)
    context = {'item':files}

    return render(request, 'fileStorage/videoplay.html', context)

def image_view(request, pk):
    files = fileStorageSchema.objects.get(id=pk)
    context = {'item':files}

    return render(request, 'fileStorage/imageview.html', context)

def text_view(request, pk):
    files = fileStorageSchema.objects.get(id=pk)
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, "elifexample.py")
    #with open(file_path,"r") as f:
    #    content = f.read()
    context = {'item':files}

    return render(request, 'fileStorage/textview.html', context)#, content)

@xframe_options_exempt
def pdf_view(request, pk):
    files = fileStorageSchema.objects.get(id=pk)
    context = {'item':files}

    return render(request, 'fileStorage/pdfview.html', context)


@login_required
def home_redirect(reqest):
    return redirect('file', permanent=True)