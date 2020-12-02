import threading 
from threading import*
import time

d={} 

def create(k,val,timeout=0):
    if k in d:
        print("error:this key already exists")
    else:
        if(k.isalpha()):
            if len(d)<(1024*1020*1024) and val<=(16*1024*1024):  
                if timeout==0:
                    n=[val,timeout]
                else:
                    n=[val,time.time()+timeout]
                if len(k)<=32: 
                    d[k]=n
            else:
                print("error:Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")
            
def read(k):
    if k not in d:
        print("error: given key does not exist in database. Please enter a valid key")
    else:
        a=d[k]
        if a[1]!=0:
            if time.time()<a[1]: 
                s=str(k)+":"+str(a[0])
                return s
            else:
                print("error: time-to-live of",k,"has expired")
        else:
            s=str(k)+":"+str(a[0])
            return s

def delete(k):
    if k not in d:
        print("error:given key does not exist in database. Please enter a valid key")
    else:
        a=d[k]
        if a[1]!=0:
            if time.time()<a[1]: 
                del d[k]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",k,"has expired") 
        else:
            del d[k]
            print("key is successfully deleted")

def modify(k,val):
    a=d[k]
    if a[1]!=0:
        if time.time()<a[1]:
            if k not in d:
                print("error: given key does not exist in database. Please enter a valid key")
            else:
                n=[]
                n.append(val)
                n.append(a[1])
                d[k]=n
        else:
            print("error: time-to-live of",k,"has expired")
    else:
        if k not in d:
            print("error: given key does not exist in database. Please enter a valid key")
        else:
            n=[]
            n.append(val)
            n.append(a[1])
            d[k]=n
#backend assignment
