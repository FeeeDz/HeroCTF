f = open("out.txt",'r')
#print(f.read())
bin=''
for i in range(0,176):
    linea = f.readline()
    #print("Linea---> "+linea)
    if linea == "PONG\n":
        bin+='0'
    elif linea == "PING\n":
        bin+='1'
print(bin)
# flag --> Hero{p1n6_p0n6_15_fun}
# https://gchq.github.io/CyberChef/#recipe=From_Binary('None',8)&input=MDEwMDEwMDAwMTEwMDEwMTAxMTEwMDEwMDExMDExMTEwMTExMTAxMTAxMTEwMDAwMDAxMTAwMDEwMTEwMTExMDAwMTEwMTEwMDEwMTExMTEwMTExMDAwMDAwMTEwMDAwMDExMDExMTAwMDExMDExMDAxMDExMTExMDAxMTAwMDEwMDExMDEwMTAxMDExMTExMDExMDAxMTAwMTExMDEwMTAxMTAxMTEwMDExMTExMDE
