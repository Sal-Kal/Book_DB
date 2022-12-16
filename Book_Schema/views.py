from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import author, book, publisher

# Create your views here.

@api_view(['POST'])
def addAuthor(request):
    try:
        newAuthor = author(
            name = request.data['name'],
            email = request.data['email'],
        )
        newAuthor.save()
        return JsonResponse({
            "status" : "success",
            "msg" : "Author Added Successfully"
        })

    except Exception as e:
        return JsonResponse({
            "status" : "error",
            "msg" : "Server Error"
        })

@api_view(['POST'])
def addPublisher(request):
    try:
        newPublisher = publisher(
            name = request.data['name'],
        )
        newPublisher.save()
        return JsonResponse({
            "status" : "success",
            "msg" : "Publisher Added Successfully"
        })

    except Exception as e:
        return JsonResponse({
            "status" : "error",
            "msg" : "Server Error"
        })

@api_view(['POST'])
def addBook(request):
    try:
        newBook = book(
            title = request.data['title'],
            author = request.data['author'],
            publisher = request.data['publisher'],
            rating = request.data['rating'],
            price = request.data['price'],
        )
        newBook.save()
        return JsonResponse({
            "status" : "success",
            "msg" : "Book Added Successfully"
        })

    except Exception as e:
        return JsonResponse({
            "status" : "error",
            "msg" : "Server Error"
        })

@api_view(['POST'])
def getAuthors(request):
    try:
        authors = author.objects.all()
        response = []

        i = 0
        # Creates a list of objects as response
        while i < authors.count():
            entry = {}
            entry["name"] = authors[i].name
            entry["email"] = authors[i].email
            response.append(entry)
            i += 1
        # Returns response dictionary
        return JsonResponse({"status": "success", "msg": response[::-1]})

    except Exception as e:
        return JsonResponse({"status": "error", "msg": "Server Error" })

@api_view(['POST'])
def getPublishers(request):
    try:
        publishers = publisher.objects.all()
        response = []

        i = 0
        # Creates a list of objects as response
        while i < publishers.count():
            entry = {}
            entry["name"] = publishers[i].name
            response.append(entry)
            i += 1
        # Returns response dictionary
        return JsonResponse({"status": "success", "msg": response[::-1]})

    except Exception as e:
        return JsonResponse({"status": "error", "msg": "Server Error" })

@api_view(['POST'])
def getBooks(request):
    try:
        books = book.objects.all()
        response = []

        i = 0
        # Creates a list of objects as response
        while i < books.count():
            entry = {}
            entry["title"] = books[i].title
            entry["author"] = books[i].author
            entry["publisher"] = books[i].publisher
            entry["rating"] = books[i].rating
            entry["price"] = books[i].price
            response.append(entry)
            i += 1
        # Returns response dictionary
        return JsonResponse({"status": "success", "msg": response[::-1]})

    except Exception as e:
        return JsonResponse({"status": "error", "msg": "Server Error" })

