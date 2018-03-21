from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
import json
from rest_framework.decorators import api_view,parser_classes
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser,MultiPartParser,FormParser
import requests

def home(request):
	return render(request, 'index.html')

@api_view(['GET'])
def essay(request):
	essay = str(request.GET.get('essay'))
	essay2 = essay.replace(' ', '+')
	RUN_URL = u'https://api.textgears.com/check.php?'
	# text= 'I+is+an+engeneer!'
	url = RUN_URL+'text='+essay2+'&key=DEMO_KEY'
	r = requests.post(url)
	x = r.json()
	return Response({'result':x})
