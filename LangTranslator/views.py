from django.shortcuts import render
from django.http import HttpResponse
from googletrans import Translator

# Create your views here.
def index(req):
	if req.method=="POST":
		txtEntered=req.POST['txtEntered']
		langChosen=req.POST['langChosen']
		translator=Translator()
		txtOutput = translator.translate(txtEntered,dest=langChosen)
		return render(req,"app/index.html",{"txtEntered":txtEntered,"txtOutput":txtOutput.text,"langChosen":langChosen})
	return render(req,"app/index.html")