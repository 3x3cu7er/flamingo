import random
import threading
import concurrent.futures 
import base64
import time
import socket

def ciphing():
    word = 'letting'
    counter=0
    while counter <= len(word):
        counter +=1
        if counter > len(word):
            counter=1
        print(word[counter])
        

ciphing()