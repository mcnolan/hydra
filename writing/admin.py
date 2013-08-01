'''
Created on 21/07/2013

@author: John
'''
from django.contrib import admin
from writing.models import Author, Book, Entry

#Standard administration
admin.site.register(Author)

#Customized Administration classes
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
                 (None, {'fields': ['title','sub_title','author','description','cover']})
                 ]
    list_display=('title','sub_title','author','created','private')
    search_fields=['author','title','sub_title']
    list_filter=['created']

admin.site.register(Book, BookAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display=('name','book','author','version','created','last_updated')
    search_fields=['book','author','name']
    list_filter=['created', 'last_updated']
    
admin.site.register(Entry, EntryAdmin)