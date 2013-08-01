'''
Created on 21/07/2013

@author: John
'''
from django.conf.urls import patterns, url

from writing import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       #Goto book detail
                       url(r'^/Book/(?P<book_id>\d+)/$', views.view_book, name='view'),
                       #Read book at beginning to entry_id
                       url(r'^/Read/(?P<entry_id>\d+)/$', views.read_book, name='read'),
                       #Read book to entry_id from entry_start
                       url(r'^/Read/(?P<entry_id>\d+)/Page/(?P<entry_start>\d+/$', views.read_book, name='read'),
                       #Create book
                       url(r'^/Book/Add/$', views.add_book, name='add_book'),
                       #Edit book
                       url(r'^/Book/(?P<book_id>\d+)/Edit/$', views.edit_book, name='edit_book'),
                       #Add entry to first page of book_id
                       url(r'^/Write/(?P<book_id>\d+/$', views.add_entry, name='add_entry'),
                       #Add entry to book_id after entry_id
                       url(r'^/Write/(?P<book_id>\d+/After/(?P<entry_id>\d+/$', views.add_entry, name='add_entry'),
                       #Edit entry entry_id
                       url(r'^/Write/(?P<book_id>\d+/Edit/(?P<entry_id>\d+/$', views.edit_entry, name='edit_entry')
                       )