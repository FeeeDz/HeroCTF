# Ping Pong

![Screenshot_8](https://user-images.githubusercontent.com/67475596/116263553-bf761380-a779-11eb-847c-e0bed7a2ca59.png)

The file given from the autor of the challenge is a long list of PING or PONG (here a small extract)
```
PONG
PING
PONG
PONG
PING
PONG
PONG
PONG
PONG
PING
PING
...
...
...
```
The idea is to convert the text in binary language.
So I started to replace PONG to 0 and PING to 1 by writing this easy script to obtain a binary string.

```Python3
f = open("out.txt",'r')
binary=''
for i in range(0,176):
    linea = f.readline()
    if linea == "PONG\n":
        binary+='0'
    elif linea == "PING\n":
        binary+='1'
print(binary)
```

Then we get this string
```
01001000011001010111001001101111011110110111000000110001011011100011011001011111011100000011000001101110001101100101111100110001001101010101111101100110011101010110111001111101
```
