
import sys
import random
from colorama import Fore
import time
import os
import datetime



initial = datetime.datetime.now().second
userIn = input(Fore.BLUE+"Say something to ~Infinity $ ")
class devAI:


    def __init__(self, greetings, requests,memory):

        self.greeting = greetings
        self.request = requests
        self.memory = memory
    def addressing(self):
        greetings = [
                'hi','hello','hey','heya','hola'
            ]
        isLogic = False
        counter = 0

        
        if len(userIn) != 0:

            if userIn.lower() in greetings:

                response =Fore.GREEN + random.choice(greetings)
            else:
                ask = input(Fore.BLUE+"Is that a greeting $")
                if ask.lower() == 'yes' or ask.lower() == 'y':
                    doc = """Accepting the input as a new greeting to the greeting"""
                    isLogic = True

                    for timing in range(30):
                        if timing==0:
                            print(doc,end='')
                            time.sleep(1)
                        print(".", end="")
                        time.sleep(.5)
                        if timing == 29 and isLogic:
                            time.sleep(.5)
                            print("ok")
                    greetings.append(userIn)
                    response = Fore.GREEN + random.choice(greetings)
                elif ask.lower() == 'no' or ask.lower() == 'n':
                    doc="""Ignoring the new greeting to the greeting"""
                    print(doc)
                    response = Fore.GREEN + "hi !"
                else:
                    response = Fore.RED + "No response found for your input !!!!!!\nSorry buddy "
                    sys.exit(1)

            print(Fore.RED+"~Infinity: ",response,"")

    def credentials(self,request):
        self.memory = {
            'name':'Infinity',
            "whatsup":"I'm good",
            "from" : "Carlifornia, xxx-street",
            'created':"Unknown",
            'gender':" I'm a male",
            'uniqueResponse':':)'

        } 
        for elements in self.memory:
            if request == elements:
                return self.memory[request]

        
    
    def assist(self):
        self.addressing()
        elements =0
        request = input(Fore.RED +"~infinity:"+ Fore.BLUE+"Can I assist you >>")
        while request.lower() == 'yes' or request.lower() == 'y':
            term = input(Fore.GREEN+"command:"+Fore.BLUE+">>")
            if term =="q" or term =="quit":
                final = datetime.datetime.now().second
                timeSpent = final - initial
                print(f"time spent {timeSpent}sec")
                for elements in range(20):
                    if elements == 0:
                        print("System exiting",end='')
                    elif elements == 19:
                        print('done')
                    print('.',end='')
                    time.sleep(.6)

                sys.exit(0)
            print(Fore.RED+"~Infinity: ",Fore.BLUE +f"{self.credentials(term)}")


ai = devAI(userIn, None,None)
ai.assist()


