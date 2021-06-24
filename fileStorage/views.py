from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.files.storage import FileSystemStorage
from django.utils.text import slugify
from .forms import fileForm
from .models import fileStorageSchema
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
from django.views.decorators.clickjacking import xframe_options_exempt

#from User.apps import UserConfig
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    #fileStorage = fileStorageSchema.objects.all()
    fileStorage = fileForm()
    return render(request, 'fileStorage/index.html', {
        #'show_fileStorage': False,
        'file': fileStorage
    })
     
    

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
            obj.fileURL = '/media/'+obj.fileName.replace(" ","%20")+"."+obj.fileType
            obj.filePath = 'F:/School/Summer2021/Independent Study'+context['url']
            setSize = round(uploaded_file.size/1048576, 2)
            setSize = str(setSize)
            setSize = setSize+'Mb'
            obj.size = setSize
            obj.uploadedBy = request.user.id
            obj.uploadDate = _datetime.strftime("%Y-%m-%d-%H-%M-%S")
            obj.save()
            return redirect('/fileStorage/')
    
    else:
        form = fileForm()
    return render(request, 'fileStorage/uploads.html', {
        'form': form
    })
    
@login_required
def file_list(request):
    files = fileStorageSchema.objects.all()
    return render(request, 'fileStorage/index.html', {
        'files': files
    })
    
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

@xframe_options_exempt
def pdf_view(request, pk):
    files = fileStorageSchema.objects.get(id=pk)
    context = {'item':files}

    return render(request, 'fileStorage/pdfview.html', context)


@login_required
def home_redirect(reqest):
    return redirect('file', permanent=True)