from django.db import models

# Create your models here.

class fileStorageSchema(models.Model):

    filePath = models.FileField(upload_to="F:/School/Summer2021/Independent Study/media/files")
    #filePath = models.FileField(upload_to='F:\School\Summer2021\Independent Study\media\files')
    fileName = models.CharField(max_length=50, default='NAME')
    fileType = models.CharField(max_length=50, default='TYPE')
    fileNote = models.TextField(default='Extra Info')
    fileURL = models.CharField(max_length=50, default='OOPS')
    #displayed as a string but read in as a byte and converted to mb/gb/etc
    size = models.CharField(max_length=50, default='0')
    uploadDate = models.CharField(max_length=50, default='DATE')
    public = models.BooleanField()
    uploadedBy = models.IntegerField(default=-1)
    #pathToFile = models.CharField(max_length = 100, default='PATH')
    
    def __str__(self):
        return self.filePath
 
    def delete(self, *args, **kwargs):
        self.filePath.delete()
        super().delete(*args, **kwargs)