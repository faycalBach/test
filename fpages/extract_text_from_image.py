# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 09:58:11 2020

@author: asus
"""
#from wand.image import Image as WandImage
#from wand.color import Color
import numpy as np
import cv2
import pytesseract
import pandas as pd
import json
from pytesseract import Output
import time





#pytesseract.pytesseract.tesseract_cmd='c:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def array2json(line_index,rows_text):
    
    to_json={}
    for i  in line_index:
        if(rows_text[str(i)].__contains__('19')) &(rows_text[str(i)].__contains__('23')):
            elm={'19':rows_text[str(i)]['19'],'23':rows_text[str(i)]['23']}
            to_json[str(i)]=elm     
            print(i,'---->',rows_text[str(i)]['19'],' --->',rows_text[str(i)]['23'])

    return json.dumps(to_json)


def doc2json(rows_text):
    
        return json.dumps(rows_text)
        

'''
def extract_text(source_file):
#def extract_text(img_input):

    RESOLUTION=72

    img_buffer=None
    with WandImage(filename=source_file, resolution=(RESOLUTION,RESOLUTION)) as img:
        img.background_color = Color('white')
        img.format        = 'tif'
        img.alpha_channel = False
        # Fill image buffer with numpy array from blob
    
    #with WandImage.from_array(img_input) as img:
     #       img.background_color = Color('white')
      #      img.format        = 'tif'
       #     img.alpha_channel = False
    
        img_buffer=np.asarray(bytearray(img.make_blob()), dtype=np.uint8)

    if img_buffer is not None:
        retval = cv2.imdecode(img_buffer, cv2.IMREAD_UNCHANGED)
        img=retval
        boxes=pytesseract.image_to_data(retval)
        txt_l=list()
        for x,b in enumerate(boxes.splitlines()):
            if x!=0:
                b=b.split()
         
                if (len(b)==12)  :
            
                    #print(x,' -->', b[11])
                    txt_l.append(b)
                    x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
                df=pd.DataFrame(txt_l,columns=['level',	'page_num',	'block_num',	'par_num','line_num','word_num',
                                   'left',	'top',	'width',	'height',	'conf',	'text'])
    



    rows=df.groupby(df.top)


    lines={}
    for key,row in rows:
        
        lines[key]=row
    
    rows_text={}

    for key in lines.keys():
        bloc=lines[key].groupby(df.block_num)
        row_text={}
        for k,r in bloc:
            separator=' '
            row_text[k]= separator.join(r.text)                
        rows_text[key]=row_text
    
    line_index=rows_text.keys()
    line_index=[int(i) for i in line_index]

    return doc2json(rows_text)
    #for i  in line_index:
        #if(rows_text[str(i)].__contains__('19')) &(rows_text[str(i)].__contains__('23')):
            #print(i,'---->',rows_text[str(i)]['19'],' --->',rows_text[str(i)]['23'])




 
def extract_text_arrImg(img_input):

    RESOLUTION=72

    img_buffer=None
    with WandImage.from_array(img_input) as img:
            img.background_color = Color('white')
            img.format        = 'tif'
            img.alpha_channel = False    
            img_buffer=np.asarray(bytearray(img.make_blob()), dtype=np.uint8)

    if img_buffer is not None:
        retval = cv2.imdecode(img_buffer, cv2.IMREAD_UNCHANGED)
        img=retval
        boxes=pytesseract.image_to_data(retval)
        txt_l=list()
        for x,b in enumerate(boxes.splitlines()):
            if x!=0:
                print('----------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',b)
                b=b.split()
         
                if (len(b)==12)  :
            
                    #print(x,' -->', b[11])
                    txt_l.append(b)
                    x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
                    
        
        
        df=pd.DataFrame(txt_l,columns=['level',	'page_num',	'block_num',	'par_num','line_num','word_num',
                                   'left',	'top',	'width',	'height',	'conf',	'text'])
    



    rows=df.groupby(df.top)
    lines={}
    for key,row in rows:
        
        lines[key]=row
    
    rows_text={}

    for key in lines.keys():
        bloc=lines[key].groupby(df.block_num)
        row_text={}
        for k,r in bloc:
            separator=' '
            row_text[k]= separator.join(r.text)                
        rows_text[key]=row_text
    
    line_index=rows_text.keys()
    line_index=[int(i) for i in line_index]

    return doc2json(rows_text)
    #for i  in line_index:
        #if(rows_text[str(i)].__contains__('19')) &(rows_text[str(i)].__contains__('23')):
            #print(i,'---->',rows_text[str(i)]['19'],' --->',rows_text[str(i)]['23'])



def get_imBuffer(source_file):

    RESOLUTION=72

    img_buffer=None
    with WandImage(filename=source_file, resolution=(RESOLUTION,RESOLUTION)) as img:
        img.background_color = Color('white')
        img.format        = 'tif'
        img.alpha_channel = False
        # Fill image buffer with numpy array from blob
        img.alpha_channel = False
        img_buffer=np.asarray(bytearray(img.make_blob()), dtype=np.uint8)
    return img_buffer

def extract_text_arrImg_fay(img_input):

   
    
    
       
        img=img_input
        boxes=pytesseract.image_to_data(img)
        txt_l=list()
        for x,b in enumerate(boxes.splitlines()):
            if x!=0:
                b=b.split()
         
                if (len(b)==12)  :
                    #print(x,' -->', b[11])
                    txt_l.append(b)
                    
        
        df=pd.DataFrame(txt_l,columns=['level',	'page_num',	'block_num',	'par_num','line_num','word_num',
                                   'left',	'top',	'width',	'height',	'conf',	'text'])
    



        rows=df.groupby(df.top)
        rows_text={}    
        lines={}
        for key,row in rows:
          lines[key]=row
    
        

        for key in lines.keys():
            bloc=lines[key].groupby(df.block_num)
            row_text={}
            for k,r in bloc:
                separator=' '
                row_text[k]= separator.join(r.text)                
            rows_text[key]=row_text
    
        line_index=rows_text.keys()
        line_index=[int(i) for i in line_index]

        return rows_text
 '''
def extract_text_arrImg_fay_(img_input):

   
    
    
       
        img=img_input
        boxes=pytesseract.image_to_data(img)
        txt_l=list()
        for x,b in enumerate(boxes.splitlines()):
            if x!=0:
                b=b.split()
         
                if (len(b)==12)  :
                    #print(x,' -->', b[11])
                    txt_l.append(b)
                    
        
        df=pd.DataFrame(txt_l,columns=['level',	'page_num',	'block_num',	'par_num','line_num','word_num',
                                   'left',	'top',	'width',	'height',	'conf',	'text'])
    


        
        rows=df.groupby(df.top)
        rows_text={}    
        lines={}
        for key,row in rows:
          lines[key]=row
    
        

        for key in lines.keys():
            bloc=lines[key].groupby(df.block_num)
            row_text={}
            for k,r in bloc:
                separator=' '
                row_text[k]= separator.join(r.text)                
            rows_text[key]=row_text
    
        line_index=rows_text.keys()
        line_index=[int(i) for i in line_index]

        return rows_text
   




def extract_text_arrImg_fay2(img_input):

        img=img_input
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        d = pytesseract.image_to_data(gray, output_type=Output.DICT)
        df=pd.DataFrame.from_dict(d)
        fn='./temp/s'+str(time.time())+'.xlsx'
        df.to_excel(fn)
       
        text = pytesseract.image_to_string(gray, lang='eng', config='--psm 6')
        data = pytesseract.image_to_string(thresh, lang='eng',config='--psm 6')
       
        print(type(text))
        print('=============================================================0')
        print(data)
        
        return  d
   
    
def extract_text_arrImg_fay3(img_input):

        


        gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)
        boxes=pytesseract.image_to_data(gray)
        txt_l=list()
        for x,b in enumerate(boxes.splitlines()):
            if x!=0:
                b=b.split()
                
                 
                if (len(b)==12)  :
                     
                    txt_l.append(b[11])    
                 
                
        return  txt_l


