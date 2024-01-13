import json
import  time 
def config(func):
    print("waiting for config")
    try:
        func()
    except Exception as e:
        
        print("the code is messing around.....")
        time.sleep(1)
@config
def varrify():
    dev = "{'ip':'129.122.16.32','port':'80','access':'auto'}"
    net = json.dumps(dev)

    request = input('querry fro ->')
    for conf in net:
        if request =='access':
            if request in net:
                print(dict(net))
        break
    


