from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

def index(request):
    fileStorage = [
        #image will be static relating to file type
        { 'fileName': 'File1', 'fileType': 'File', 'size': '10gb', 'image' : 'file', 'uploadDate' : '5/25/21' , 'modifyDate' : '5/27/21', 'visibility' : 'Public'},
        { 'fileName': 'Image1', 'fileType': 'Image', 'size': '10mb', 'image' : 'image', 'uploadDate' : '5/22/21' , 'modifyDate' : '5/23/21', 'visibility' : 'Private'}
    ]
    #returns the location of the index.html from the templates point of view
    return render(request, 'fileStorage/index.html', {
        'show_fileStorage': False,
        'fileStorage': fileStorage
    })