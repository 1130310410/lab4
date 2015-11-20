from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from library.models import Book,Author
from django.template import RequestContext
import datetime,json
# Create your views here.
#here is a change
def main(request):
	books = Book.objects.all()
	urls = {} 
	for book in books:
		urls[book.Title] = ("/show/"+book.ISBN,book.AuthorID.Name,"/updateinterface/"+book.ISBN,"/delete/"+book.ISBN)
	return render_to_response('main.html',locals(),context_instance=RequestContext(request))

def addinterface(request):
	return render_to_response('addinterface.html',context_instance=RequestContext(request))

def addoperation(request):
	isbn = request.POST["isbn"]
	title = request.POST["title"]
	publisher = request.POST["publisher"]
	year = request.POST["year"]
	month = request.POST["month"]
	day = request.POST["day"]
	price = request.POST["price"] 
	author = request.POST["author"]
	age = request.POST["age"]
	country = request.POST["country"]
	booklist = Book.objects.filter(ISBN=isbn)
	if booklist:
		books = Book.objects.all()
		urls = {} 
		for book in books:
			urls[book.Title] = ("/show/"+book.ISBN,book.AuthorID.Name,"/updateinterface/"+book.ISBN,"/delete/"+book.ISBN)
		return render_to_response('main.html',{'urls':urls,'already':True},context_instance=RequestContext(request))
	authorlist = Author.objects.filter(Name=author,Age=age,Country=country)
	if not authorlist:
		oneauthor = Author(Name=author,Age=age,Country=country)
		oneauthor.save()
	else:
		oneauthor = Author.objects.get(Name=author,Age=age,Country=country)
	onebook = Book(ISBN=isbn,Title=title,AuthorID=oneauthor,Publisher=publisher,PublishDate=datetime.date(int(year),int(month),int(day)),Price=float(price))
	onebook.save()
	books = Book.objects.all()
	urls = {} 
	for book in books:
		urls[book.Title] = ("/show/"+book.ISBN,book.AuthorID.Name,"/updateinterface/"+book.ISBN,"/delete/"+book.ISBN)
	return render_to_response('main.html',{'urls':urls,'add':True},context_instance=RequestContext(request))

def updateinterface(request,num):
	num = int(num)
	book = Book.objects.get(ISBN=num)
	return render_to_response('updateinterface.html',{'book':book},context_instance=RequestContext(request))

def updateoperation(request):
	isbn = request.POST["isbn"]
	title = request.POST["title"]
	publisher = request.POST["publisher"]
	year = request.POST["year"]
	month = request.POST["month"]
	day = request.POST["day"]
	price = request.POST["price"] 
	author = request.POST["author"]
	age = request.POST["age"]
	country = request.POST["country"]
	authorlist = Author.objects.filter(Name=author,Age=age,Country=country)
	if not authorlist:
		oneauthor = Author(Name=author,Age=age,Country=country)
		oneauthor.save()
	else:
		oneauthor = Author.objects.get(Name=author,Age=age,Country=country)
	book = Book.objects.get(ISBN=isbn)	
	book.Title = title
	book.Publisher = publisher
	book.AuthorID = oneauthor
	book.PublishDate = datetime.date(int(year),int(month),int(day))
	book.Price = float(price)
	book.save()
	books = Book.objects.all()
	urls = {} 
	for book in books:
		urls[book.Title] = ("/show/"+book.ISBN,book.AuthorID.Name,"/updateinterface/"+book.ISBN,"/delete/"+book.ISBN)
	return render_to_response('main.html',{'urls':urls,'update':True},context_instance=RequestContext(request))

def delete(request,num):
	num = int(num)
	book = Book.objects.get(ISBN=num)
	book.delete()
	books = Book.objects.all()
	urls = {} 
	for book in books:
		urls[book.Title] = ("/show/"+book.ISBN,book.AuthorID.Name,"/updateinterface/"+book.ISBN,"/delete/"+book.ISBN)
	return render_to_response('main.html',{'urls':urls,'delete':True},context_instance=RequestContext(request))

def search(request):
	author = request.POST["search"]
	books = Book.objects.all()
	result = []
	for book in books:
		if (book.AuthorID.Name == author):
			result.append(book)
	if result:
		return render_to_response('searchresult.html',{'result':result},context_instance=RequestContext(request))
	else:
		return render_to_response('searchresult.html',{'result':result,'none':True},context_instance=RequestContext(request))

def show(request,num):
	num = int(num)
	book = Book.objects.get(ISBN=num)
	return render_to_response('show.html',{'book':book},context_instance=RequestContext(request))

