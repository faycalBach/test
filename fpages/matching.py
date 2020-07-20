import numpy as np
import cv2
#from matplotlib import pyplot as plt

#import sys
import os
#import PIL 
dir='p30'
if not os.path.exists('p30'):
    os.makedirs('p30')


def match_image( image_file_name= './tim.jpg',temp_file_name='./ko2.png'):
    img_rgb = cv2.imread(image_file_name)
    template = cv2.imread(temp_file_name)
    w, h,x = template.shape[::-1]
    W, H,X =img_rgb.shape[::-1]
    res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.89
    loc = np.where( res >= threshold)
    count=0
    allfile=list()
    for pt in zip(*loc[::-1]):
        count+=1
        print(count,'---',pt)
        cv2.rectangle(img_rgb, (0,pt[1]), (H, pt[1] + x), (0,0,255), 2)
        roi = img_rgb[pt[1]:pt[1]+x,:]
        txt=''+str(pt[0])+'-'+str(pt[1])
        #cv2.putText(img_rgb,txt,  )
        allfile.append(dir+'/patch_'+str(count)+str(count)+".jpg")
        cv2.imwrite(dir+'/patch_'+str(count)+str(count)+".jpg", roi)
    return allfile   
    #cv2.imwrite('res30.png',img_rgb)
    
def immatch_asarray( image_file_name= './tim.jpg',temp_file_name='./ko.png'):
    img_rgb = cv2.imread(image_file_name)
    template = cv2.imread(temp_file_name)
    w, h,x = template.shape[::-1]
    W, H,X =img_rgb.shape[::-1]
    res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.89
    loc = np.where( res >= threshold)
    count=0
    #allfile=list()
    images_found=list()
    for pt in zip(*loc[::-1]):
        count+=1
        print(count,'---',pt)
        cv2.rectangle(img_rgb, (0,pt[1]), (H, pt[1] + x), (0,0,255), 2)
        roi = img_rgb[pt[1]:pt[1]+x,:]
        #txt=''+str(pt[0])+'-'+str(pt[1])
        #cv2.putText(img_rgb,txt,  )
        #allfile.append(dir+'/patch_'+str(count)+str(count)+".jpg")
        #cv2.imwrite(dir+'/patch_'+str(count)+str(count)+".jpg", roi)
        images_found.append(roi)
    return images_found   


    #cv2.imwrite('res30.png',img_rgb)
    
    
    
def immatch_asarray_fromStream( stream,temp_file_name='./ko2.png'):
    
    
  
    img = stream
    
    #img = PIL.Image.open(stream)
    img_buffer=None
    img_buffer=stream
    if img_buffer is not None:
        #retval = cv2.imdecode(img_buffer, cv2.IMREAD_UNCHANGED)
        img_rgb=img_buffer
        template = cv2.imread(temp_file_name)
        w, h,x = template.shape[::-1]
        W, H,X =img_rgb.shape[::-1]
        res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
        
        threshold = 0.96
        
        loc = np.where( res >= threshold)
        count=0
        images_found=list()
        for pt in zip(*loc[::-1]):
            count+=1
            print(count,'- location of template point  -',pt)
            #cv2.rectangle(img_rgb, (0,pt[1]), (H, pt[1] + x), (0,0,255), 2)
            roi = img_rgb[pt[1]:pt[1]+x,:]
            images_found.append(roi)
   
        return images_found   