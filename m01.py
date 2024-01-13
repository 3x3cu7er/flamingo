nat = {
    "n1":{
        "name": "route1",
        "id":'0.1',
        "interface": "wlan1"
        },
    "n2":{
        "name": "route2",
        "id":'0.1.2',
        "interface": "wlan2"
        },
    "framework":{
        'os':'Linux',
        'proc-type':'x86_64',
        'system-user':'root',
        'physical memory':'12203',
        'version':'0.2.3.1'
    }
}
nlist = []
import sys
for n in nat:
    for element in nat[n]:
        if element=='interface':
            print(nat[n][element])
            for line in sys.stdin:
                if line.rstrip() =='q':
                    break
                else:
                    nlist.append(line)
            print("Stored info".center(30,'*'))
            for li in nlist:
                sys.stdout.write(li)
