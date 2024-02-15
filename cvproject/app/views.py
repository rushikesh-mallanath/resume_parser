from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib import messages
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
from docx import Document
from unidecode import unidecode
stop_words = set(stopwords.words('english'))


#upload files function
def fileupload(request):
    if request.method == 'POST':
        request_files = request.FILES.getlist('document')
        fs = FileSystemStorage()
        successflag = False
        if request_files:
            for request_file in request_files:
                if request_file.name.endswith(('.pdf', '.docx')):
                    successflag = True
                    fs.save(request_file.name, request_file)
                else:
                    messages.info(request, "Resumes not uploaded yet!")
            if successflag:
                return redirect('jd/')
    return render(request, 'app/main.html')

def jdview(request):
    return render(request, 'app/jd.html')

#take jd and experience as input
def jdinput(request):
    if request.method == 'POST':
        #for job discription
        jdtext = request.POST.get('jobdiscription')
        jdtext = word_tokenize(jdtext)
        jdtext = [w for w in jdtext if not w.lower() in stop_words]
        jdtext = ' '.join(jdtext)
        print('==', jdtext)

        #for required experience
        exp = request.POST.get('experience')

        if not jdtext:
            messages.info(request, "Provide job discription!")
        if not exp:
            messages.info(request, "Provide required experience!")
    return render(request, 'app/jd.html')

def output(request):
    return render(request, 'app/output.html')

#function for text extraction from .docx
def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
        text = unidecode(text)
    return text

#dir where uploaded resumes get stored
document_path = '/home/rushikeshmallanath/Downloads/Ve/resumep/cvproject/media/files/'

for filename in os.listdir(document_path):
    if filename.endswith(".docx"):
        print('file is=', filename)
        docx_path = os.path.join(document_path, filename)
        print('>>', docx_path)
        extracted_text = extract_text_from_docx(docx_path)
        