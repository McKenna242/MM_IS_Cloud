from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from .forms import fileForm
from .models import fileStorageSchema
from datetime import datetime
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
            obj.fileURL = '/media/'+uploaded_file.name
            obj.fileName, obj.fileType = uploaded_file.name.split(".")
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

def file_list(request):
    files = fileStorageSchema.objects.all()
    return render(request, 'fileStorage/index.html', {
        'files': files
    })
    
def delete_file(request, pk):
    if request.method == 'POST':
        file = fileStorageSchema.objects.get(pk=pk)
        file.delete()
    return redirect('/fileStorage/')
