from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm
from .generate import generate
from .handle_pdf import handle_uploaded_file
from django.core.files.storage import FileSystemStorage
from .handle_pdf import handle_uploaded_file
import requests
from bs4 import BeautifulSoup


def index(request):
    return render(request, 'home.html')



def text_summary(request):
    if request.method == 'POST':
            input_text = request.POST.getlist('text')
            data = generate(input_text)
            return render(request, 'text.html', {'data': data,'summary':data["choices"][0]["text"]})

    return HttpResponseRedirect('/')

def upload(request):
    
        if request.method == 'POST':
            input_text = request.POST.getlist('text')
            data = generate(input_text)     
            return render(request, 'upload.html', {'data': data,'summary':data["choices"][0]["text"],'real_text':input_text})

        return HttpResponseRedirect('/')
    
def pdf_input(request):
    if request.method == 'POST':
        uploaded_file = request.FILES["file"]
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        docs = handle_uploaded_file(uploaded_file.name) 
        docs= generate(docs)
        return render(request,'pdf_input.html',{'docs':docs,'name':uploaded_file.name,'summary':docs["choices"][0]["text"]})  

    return HttpResponseRedirect('/')


def article_summary(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
      
        if form.is_valid():
            # process the data in form.cleaned_data as required
            r1 = requests.get(form.cleaned_data['url_field'])
            coverpage = r1.content
            soup1 = BeautifulSoup(coverpage,  "lxml")
            text = ''
            for data in soup1.find_all("p"):
                text += data.get_text()
            docs= generate(text)
            return render(request, 'article.html', {'form': form,'text':docs,'summary':docs["choices"][0]["text"]})
    else:
        form = NameForm()

    return render(request, 'article.html', {'form': form})
    

