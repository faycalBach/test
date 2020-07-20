from django.shortcuts import render,redirect

from .form import EntryForm,UploadEntryForm
#from django_globals import globals 
#from . import namer
from django.http import JsonResponse,HttpResponse
from  . import  loaded

import json
import pandas as pd



import numpy as np
import cv2  
import requests
count=0
db=1
httpr=None

def post_to_marco(datajson):
 
 headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
 data=json.dumps({'key':'tim','data':datajson}) 
 url='https://robo-op.herokuapp.com/api'
 r = requests.post(url, data, headers=headers)
 print('post to marco is ......',r.ok)


# Create your views here.
def tim(request): 

  if request.method == 'POST' : 

        form=EntryForm(request.POST, request.FILES)  
        if form.is_valid():
            print('form is ok',form)
            st=upload_file(form.cleaned_data['file_upload']) 
            post_to_marco(st)
            return HttpResponse(st,  content_type="application/json") 
        
        else :
            HttpResponse('upload file error .....') 


  else :
    context={}
  
    form=EntryForm() 
    context['form'] = form
    return render(request,'tim.html',context)


def bnl(request):
	
  if request.method == 'POST' : 

        form=EntryForm(request.POST, request.FILES)  
        if form.is_valid():
            print('form is ok',form)
            st=upload_file(form.cleaned_data['file_upload'],client='bnl') 
            post_to_marco(st)
            return HttpResponse(st,  content_type="application/json") 
        
        else :
            HttpResponse('upload file error .....') 


  else :
    context={}
  
    form=EntryForm() 
    context['form'] = form
    return render(request,'bnl.html',context)
	
 
def sofia(request) :
  if request.method == 'POST':
    form=EntryForm(request.POST, request.FILES)
    if form.is_valid():
     print('form is ok',form)
     st=csv2json(form.cleaned_data['file_upload'],client='csv2json') 
     post_to_marco(st)
     return HttpResponse(st,  content_type="application/json") 
    else :  
      HttpResponse('upload file error .....') 
  else :
    context={}
    form=EntryForm() 
    context['form'] = form
    return render(request,'csv2json.html',context)
	



#sys.path.append(r'C:\\Users\\asus\\aise')
from . import matching as mtc
from . import stm_extrat2 as stm2
from .form import EntryForm

clients={'tim':'./ko2.png','bnl':'./ko.png'}





def return_resp(_json):
         
        
       # return json2html.convert(json =_json)
       print('...........................................................',_json)
       js=_json
      
       return js
    
def upload_file(file, client='tim'):
   
       template=clients[client] 
       print('----------------------------> template  is', template,' ....... ',client)
       img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
       
       # x=stm2.text_from_image_as_stream2(img,template)   
       x=stm2.text_from_image_as_stream3(img,template)   
       print('-------- upload file',type(x))
      
       loaded.res[client]=json.dumps(x[1])
       return return_resp(x[0])                                                    
      



def upload(request):
    context = {}
    print('start upload ......')
    
    if request.method == 'POST' :
        #uploaded_file = request.FILES['file']
        #fs = FileSystemStorage()
        #name = fs.save(uploaded_file.name, uploaded_file)
        #context['url'] = fs.url(name)
        print('start post ......')
        form=UploadEntryForm(request.POST, request.FILES)  
        if form.is_valid():
            print('form is ok',form)
            
            st=upload_file(form.cleaned_data['file_upload'],form.cleaned_data['client_name']) 
            post_to_marco(st)
            #return JsonResponse(st, safe=False)
            return HttpResponse(st,  content_type="application/json") 
        
        else :
            print('form is ko')
        
       # st=upload_file(uploaded_file)
        
    else :
         
         form=EntryForm() 
         
         
         
    context['form'] = form
    return render(request, 'upload.html', context)


def uploaded(request,num=1):

    '''

    print('start uploaded................................................')
    for key, value in request.GET.items():
     print('Key: %s' % (key) ) 
    # print(f'Key: {key}') in Python >= 3.7
     print('Value %s' % (value) )
    # print(f'Value: {value}') in Python >= 3.7
    print('end uploaded................................................')
    

    
    element='bnl'
    if num== 1 :
      element='tim'
    text_image = loaded.res[element]

   
    print('.........................................',element,'........keys res ',loaded.res.keys())
    return HttpResponse(text_image,  content_type="application/json") 
   '''
    element='csv2json'
    if num== 1 :
      element='tim'
    if num==2:
      element='bnl'
    text_image='upload before you can view '+ element 
    if element in loaded.res:  
      text_image = loaded.res[element]
    response = HttpResponse(text_image,  content_type="application/json") 
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response
  
from io import StringIO

  
def csv2json(file,client='csv2json'):
     
    
    csv_text = ''
    for line in file:
        csv_text = csv_text + line.decode()  # "str_text" will be of `str` type
    # do something
    print('-----------str text ------------->')
    #print(csv_text)
    print('-----------str text ------------->')
     
    csv_text=StringIO(csv_text)
    ef = pd.read_csv( csv_text,sep=";")
    sr = pd.DataFrame(ef)
    result=sr.to_json(orient='records')
    
    print(result)       
    loaded.res[client]=result
    
    return return_resp(result)                                                    
      


