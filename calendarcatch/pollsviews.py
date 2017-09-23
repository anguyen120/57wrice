from django.http import HttpResponse

def index(request):
	return HttpsResponse("Hello, world. You're at the polls index.")
