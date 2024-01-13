from jinja2 import Environment, FileSystemLoader
ENV = Environment(loader=FileSystemLoader('.'))
template = ENV.get_template("template.j2")
interfaces = [
{
"name": "GigabitEthernet0/1",
"desc": "uplink port",
"uplink": True
},
{
"name": "GigabitEthernet0/2",
"desc": "Server port number one",
"vlan": 10
},
{
"name": "GigabitEthernet0/3",
"desc": "Server port number two",
"vlan": 10
}
]


    
for ind in range(len(interfaces)):
    for sep in range(20):
     print('*',end='')
    print('\n' + template.render(interface = interfaces[ind]))

    ind +=1