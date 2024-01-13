
import threading
import time
import concurrent.futures


class sysAutoConfig:
    
	# <-------------------------------  nitial(default)  procedure
  	# API handler
	def proc_0(*args,**kwargs):
		if True:
			print('ready to proceed...')
		
	# <-------------------------------  first procedure
	# administrator established connection handler
	def proc_1(*args,**kwargs):
		pass

	# <-------------------------------  second procedure
	# packets forwarding method: virtual circuit network
	def proc_2(*args,**kwargs):
		pass	
		
	# <-------------------------------  third procedure
	# packets forwarding method: source routing virtual  network

	def proc_3(*args,**kwargs):
		pass
	# <-------------------------------  forth procedure
	# packets forwarding method: datagram network
	def proc_4(*args,**kwargs):
		pass

	# <-------------------------------  fifth procedure
	#connecting verifier
	def proc_5(*args,**kwargs):
     	 pass

	

    
s = sysAutoConfig()



# procedure specification checking
try:
	_procedure = input("Enter the procedure  0,1,2,3,4,5  or  q{ quit} #")
	_quit = "quit"

	_proc = {
		'0': 'proc_0', # API handler 
		'1': 'proc_1', # administrator established connection handler
		'2': 'proc_2',	# packets forwarding method: virtual circuit network
		'3': 'proc_3',	# packets forwarding method: source routing virtual  network
		'4': 'proc_4',	# packets forwarding method: datagram network
		'5': 'proc_5'	 #connecting verifier
	}

	
except KeyError as kerr:
	err_msg = print(f"No value found for the procedure, error@{kerr}")


# handles terminating processes

def controller():
    while _procedure.lower()!="quit" or _procedure.lower()!='q':
					if _procedure not in _proc:
						print("Quitting~",end='')

						for speed in range(100):
							print('.',end='')
							if speed== 99:
								print('done!')
								print("~LAZY MAN~")

							time.sleep(.05)
						break
					else:
						print(f"Command awaits @{_proc[_procedure]}"
            							"\n\n")
						if _procedure=='0':
				   			s.proc_0()
						elif _procedure=='1':
							s.proc_1()
						elif _procedure=='2':
							s.proc_2()
						elif _procedure=='3':
							s.proc_3()
						elif _procedure=='4':
							s.proc_4()
						elif _procedure=='5':
							s.proc_5()
						break

'''man = threading.Thread(target=controller)
man.start()'''

with concurrent.futures.ThreadPoolExecutor() as ex:
	ex.submit(controller)