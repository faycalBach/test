from . import matching as mtc
from . import extract_text_from_image as ex
import os
     
debug=0
 



obj_tim=('hug30200','hug30166','verm1e04',
     'RM1-BCK-NW-ESE-02 telecomitalia.local',
     'GRFMIRO02B0009', 'asese3','esmval2',
     'dwhtradbadm01 griffon.local',
     'CompdealETL1 .telecomitalia.local',
     'gristo001rm001')   

objs={}
objs['./ko2.png']=obj_tim

def text_from_image(file_name):
    arrays_img=mtc.immatch_asarray(image_file_name=file_name)
    text=list()
    for img in arrays_img :
     text.append(ex.extract_text_arrImg_fay(img))
     count =0    
    
    list_objects={}
    for txt in text:
         print(txt)
         for ob in obj:
             for k in txt.keys():
                 if type( txt[k])==dict:
                     for kk in txt[k].keys():
                         count+=1
                         if ob in txt[k][kk]:  
                             if debug:
                                 print(ob,'---->',kk,'---->', txt[k][kk] )
                                 list_objects[ob]=txt
    return list_objects ,text,arrays_img    

#this fonction called from web application
def text_from_image_as_stream(stream,temp_file_name='./ko2.png'):
    
    
    
    #print('<----file name tempale-stm -----',temp_file_name) 
    l_arrays_img=mtc.immatch_asarray_fromStream(stream,temp_file_name)
    
    text=list()
    
    list_objects=()
    for img in l_arrays_img :
     #text.append(ex.extract_text_arrImg_fay(img))
     text.append(ex.extract_text_arrImg_fay2(img))
     count =0    
   
    
    obj=None
    key=temp_file_name
    if key in objs.keys(): 
        obj=objs[temp_file_name]
    
    list_objects= trasform_fay(text,obj)
        
    '''
    for txt in text:
         for ob in obj:
             for k in txt.keys():
                 if type( txt[k])==dict:
                     for kk in txt[k].keys():
                         count+=1
                         if ob in txt[k][kk]:  
                             if debug:
                                 print(ob,'---->',kk,'---->', txt[k][kk] )
                                 list_objects[ob]=txt
    '''
    return  list_objects ,text  




def text_from_image_as_stream2(stream,temp_file_name='./ko2.png'):
    
    
    
    #print('<----file name tempale-stm -----',temp_file_name) 
    l_arrays_img=mtc.immatch_asarray_fromStream(stream,temp_file_name)
    
    text=list()
    
    list_objects=()
    for img in l_arrays_img :
     #text.append(ex.extract_text_arrImg_fay(img))
     text.append(ex.extract_text_arrImg_fay2(img))
     count =0    
   
    
    list_objects=visualizza_text2(text)
    print('  --->   list len', len(list_objects))
    return  list_objects ,text

def text_from_image_as_stream3(stream,temp_file_name='./ko2.png'):
    
    
    
    #print('<----file name tempale-stm -----',temp_file_name) 
    l_arrays_img=mtc.immatch_asarray_fromStream(stream,temp_file_name)
    
    text=list()
    
    list_objects=()
    for img in l_arrays_img :
     #text.append(ex.extract_text_arrImg_fay(img))
     text.append(ex.extract_text_arrImg_fay3(img))
     count =0    
   
    
    
    return  text,text



def trasform(text):
   
   
       obj=('hug30200','hug30166','verm1e04',
     'RM1-BCK-NW-ESE-02 telecomitalia.local',
     'GRFMIRO02B0009', 'asese3','esmval2',
     'dwhtradbadm01 griffon.local',
     'CompdealETL1 .telecomitalia.local',
     'gristo001rm001')  
   
       l_objects={}
       count=0
       for txt in text:
                count+=1
                #print('--element visited ------------------------------>' ,count)
                for ob in obj:
                    for k in txt.keys():
                        if type( txt[k])==dict:
                            for kk in txt[k].keys():
                                
                                if ob in txt[k][kk]:  
                                    if debug:
                                        #print(ob,'---->',kk,'---->', txt[k][kk] )
                                        l_objects[ob]=txt
                        else:
                            print('--><---',txt[k])
       return l_objects
   
    
   
    
   
def trasform_fay(text,obj):
   
       if obj==None:
           return {}
   
   
       l_objects={}
       count=0
       for txt in text:
                count+=1
                print('--element visited ------------------------------>' ,count)
                txt_s=str(txt)
                for ob in obj:
                    if(txt_s.find(ob)):
                        l_objects[ob]=txt
                        #print(ob,'---->', txt )
                    
       return l_objects
     
   
    
def visualizza_text2(list_dict):
    
    print('-------- start ')
    #print(list_dict)
    print('---------end -------')
    
    objs=list()
    for i in range(len(list_dict)):
      separator=' '
      start=separator.join(list_dict[i]['text'][4:7])
      separator=' '
      end=separator.join(list_dict[i]['text'][7:10])
      separator=' '
      objname=separator.join(list_dict[i]['text'][11:13])
      separator=' '
      des=separator.join(list_dict[i]['text'][13:30])
      objs.append( {objname:{'start':start,'end':end, 'des':des}})
      #print(i,start,end,objs[i],des)
    return objs  
      
      #print( start,end, objname, des)   

def visualizza_text(list_dict):
    objs=list()
    
    
    
    for i in range(len(list_dict)):
     
          #if (list_dict[i]['level']==5)  :
          print(type(list_dict),'  list_dict')
          #print(list_dict[i]['text'])
          separator=' '
          start=separator.join(list_dict[i]['text'][4:7])
          separator=' '
          end=separator.join(list_dict[i]['text'][7:10])
          separator=' '
          objname=separator.join(list_dict[i]['text'][11:13])
          separator=' '
          des=separator.join(list_dict[i]['text'][13:-1])
          #print(  i,objname,'<------->', des) 
          objs.append( {'obj':objname,'start':start,'end':end, 'des':des})
      
    return objs




def visualizza_text3(list_dict):
    
    print('-------- start ')
    #print(list_dict)
    print('---------end -------')
    
    objs=list()
    
    ress=list()
    for i in range(len(list_dict)):
      
      res=[] 
      for item in list_dict[i]['text']:
          if(len(item) > 1):
             res.append(item)
        
               
      
      separator=' '
      #print(res)
      ress.append(res)
      start=separator.join(res[0:3])
      separator=' '
      end=separator.join(res[3:6])
      separator=' '
      objname=separator.join(res[7:8])
      separator=' '
      des=separator.join(res[8:-1])
      objs.append( {objname:{'start':start,'end':end, 'des':des}})
      #print(i,start,end,objs[i],des)
    return objs  ,ress
      
      #print( start,end, objname, des)   
   