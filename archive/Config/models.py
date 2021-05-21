from django.db import models

# Create your models here.
CONTENT_CHOICE=(
    ('image','Image'),
    ('pdf','PDF'),
    ('file','Text File'),
    ('video','Video'),
    ('v-url','Video URL'),
    ('url','URL'),
)

class Category(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name='Category Name')

    class Meta:
        verbose_name_plural="Categories"

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name='Tag Name')

    class Meta:
        verbose_name_plural="Tags"

    def __str__(self):
        return self.name  

class Source(models.Model):
    name = models.CharField(max_length=200,unique=True,verbose_name='Source Name')

    class Meta:
        verbose_name_plural="Sources"

    def __str__(self):
        return self.name  


class Entry(models.Model):
    date=models.DateTimeField()
    content_type=models.CharField(max_length=100,choices=CONTENT_CHOICE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='entry_category')
    source=models.ForeignKey(Source,on_delete=models.CASCADE,related_name='entry_source')
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE,related_name='entry_tag',null=True,blank=True)
    title=models.CharField(max_length=200,null=True)
    content_file=models.FileField(upload_to='files/',null=True,blank=True)
    content_url=models.URLField(null=True,blank=True)


    class Meta:
        verbose_name="Data Entry"
        verbose_name_plural="Data Entries"

    def __str__(self):
        return self.content_type


