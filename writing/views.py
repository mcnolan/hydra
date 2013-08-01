# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index page")

def view_book(request, book_id):
    return HttpResponse("View Book")

def read_book(request, entry_id, entry_start):
    return HttpResponse("Read Book")

def add_book(request):
    return HttpResponse("Add book")

def edit_book(request, book_id):
    return HttpResponse("Edit book")

def add_entry(request, book_id, entry_id):
    return HttpResponse("Add Entry")

def edit_entry(request, book_id, entry_id):
    return HttpResponse("Edit Entry")
