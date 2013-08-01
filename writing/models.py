from django.db import models

#Book Writing Models
# Standards:
#    Titles : 200 characters long
#    Descriptions : 500 characters long
#    

# The Author model describes the User doing the writing
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="avatarImages", null=True, blank=True)
    description = models.CharField(max_length=500, blank=True)
    joined = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.first_name + " " + self.last_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to="covers", null=True, blank=True)
    sub_title = models.CharField(max_length=500, blank=True)
    author = models.ForeignKey(Author)
    description = models.CharField(max_length=500, blank=True)
    private = models.BooleanField()
    created = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

# The Entry model describes the Entries that make up a particular book. 
# This could be anything from a single paragraph to an entire chapter    
class Entry(models.Model):
    book = models.ForeignKey(Book)
    author = models.ForeignKey(Author)
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    version = models.IntegerField(default=1)
    #This will be null if the Entry is the latest
    previous_version = models.ForeignKey("self", null=True, blank=True)
    content = models.TextField()
    # In theory this group should not contain the Entry in previous version
    entries = models.ManyToManyField("self", blank=True)
    
    def __unicode__(self):
        return self.name