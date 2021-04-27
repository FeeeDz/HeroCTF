f = open("output.txt",'r')
binary=''
for i in range(0,176):
    linea = f.readline()
    if linea == "PONG\n":
        binary+='0'
    elif linea == "PING\n":
        binary+='1'
print(binary)
# flag --> Hero{p1n6_p0n6_15_fun}
# https://gchq.github.io/CyberChef/#recipe=From_Binary('None',8)&input=MDEwMDEwMDAwMTEwMDEwMTAxMTEwMDEwMDExMDExMTEwMTExMTAxMTAxMTEwMDAwMDAxMTAwMDEwMTEwMTExMDAwMTEwMTEwMDEwMTExMTEwMTExMDAwMDAwMTEwMDAwMDExMDExMTAwMDExMDExMDAxMDExMTExMDAxMTAwMDEwMDExMDEwMTAxMDExMTExMDExMDAxMTAwMTExMDEwMTAxMTAxMTEwMDExMTExMDE
