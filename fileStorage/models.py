from django.db import models

# Create your models here.

class fileStorage(models.Model):
    fileName = models.CharField(max_length=50)
    fileType = models.CharField(max_length=50)
    #store as int in bytes process return as gb mb etc
    size = models.IntegerField() #make custom field of int and char var
    uploadDate = models.DateField()
    modifyDate = models.DateField()
    visibility = models.BooleanField()
    #ptr to file location
    #text field without max length
    pathToFile = models.CharField(max_length = 100)
    
    
    
    #        { 'fileName': 'Image1', 'fileType': 'Image', 'size': '10mb', 'image' : 'file', 
    # 'uploadDate' : '5/22/21' , 'modifyDate' : '5/23/21', 'visibility' : 'Private'}
 