import uuid

from django.db import models
# Create your models here.


class fileStorageSchema(models.Model):

    id = models.UUIDField(primary_key = True, default = uuid.uuid4)
    filePath = models.FileField(upload_to="F:/School/Summer2021/Independent Study/media/files", max_length = 255)
    #filePath = models.FileField(upload_to='F:\School\Summer2021\Independent Study\media\files')
    fileName = models.CharField(max_length=100, default='NAME')
    fileType = models.CharField('File Type', max_length=50, default='TYPE')
    fileNote = models.TextField('Add a file description', default='Extra Info')
    fileURL = models.CharField(max_length=150, default='OOPS')
    #displayed as a string but read in as a byte and converted to mb/gb/etc
    size = models.CharField(max_length=100, default='0')
    uploadDate = models.DateTimeField(auto_now_add=True, null=True)
    public = models.BooleanField('Create Link')
    groups = models.CharField(max_length=50, default='PRIVATE')
    uploadedBy = models.IntegerField(default=-1)
    #pathToFile = models.CharField(max_length = 100, default='PATH')
    
    def __str__(self):
        return self.fileName
    
  
