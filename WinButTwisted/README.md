# Win, but twisted

![Screenshot_16](https://user-images.githubusercontent.com/67475596/116267591-d833f880-a77c-11eb-90da-a6fcc7751806.png)

In this challenge we were given a binary and a C file, let's analyze them.
```C
#include <stdio.h>

#include <stdlib.h>

#include <unistd.h>

#include <sys/types.h>



int UNLOCKED = 0;



void set_lock()

{

    printf("Setting lock !");

    UNLOCKED = 1;

}



void shell()

{

    printf("In shell function ! ");

    if (UNLOCKED == 1)

    {

        printf("Getting shell ! ");

        setreuid(geteuid(), geteuid());

        system("/bin/sh");

    }



    

}



void hello_hero(int hero)

{

    printf("It looks like that's something a Hero would say\n");

}



void look_like()

{

    printf("Please keep being one. :)\n");

}



int main()

{

    int (*look)() = look_like;

    int (*hello)() = hello_hero;

    char buffer[32];



    printf("What would a hero say ?\n>>> ");

    fgets(buffer, 44, stdin);

    hello();

    look();



}
```
Security:
```bash
checksec WinButTwisted
[*] '/home/kali/Desktop/CTF/HeroCTF/pwn/WinButTwisted'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```
Uhhm it seems crashed.. 
```bash
./WinButTwisted       
What would a hero say ?
>>> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
zsh: segmentation fault  ./WinButTwisted
```
Now let's find the exactly offset for our padding.
Create a cyclic string in python with the Pwntools library.
```bash
>>> cyclic_metasploit(40)
b'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2A'
```
Run the binary into GDB 
```gdb
gef➤  r
Starting program: /home/kali/Desktop/CTF/HeroCTF/pwn/WinButTwisted 
What would a hero say ?
>>> Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2A

Program received signal SIGSEGV, Segmentation fault.
0x31624130 in ?? ()
──────────────────────────────────────────────────────────────────────────────────── registers ────
$eax   : 0x31624130 ("0Ab1"?)
$ebx   : 0x080e9000  →  0x00000000
$ecx   : 0x080ecde9  →  0x00000000
$edx   : 0xfbad0088
$esp   : 0xffffd0bc  →  0x08049add  →  <main+118> mov eax, DWORD PTR [ebp-0xc]
$ebp   : 0xffffd0f8  →  0x00000800
$esi   : 0x080e900c  →  0x0806d190  →  <__strcpy_ssse3+0> endbr32 
$edi   : 0x0804823c  →  0x00000000
$eip   : 0x31624130 ("0Ab1"?)
$eflags: [zero carry PARITY adjust SIGN trap INTERRUPT direction overflow RESUME virtualx86 identification]
$cs: 0x0023 $ss: 0x002b $ds: 0x002b $es: 0x002b $fs: 0x0000 $gs: 0x0063 
──────────────────────────────────────────────────────────────────────────────────────── stack ────
0xffffd0bc│+0x0000: 0x08049add  →  <main+118> mov eax, DWORD PTR [ebp-0xc]       ← $esp
0xffffd0c0│+0x0004: 0x080e9094  →  0x080ea8c0  →  0x00000000
0xffffd0c4│+0x0008: 0x00000000
0xffffd0c8│+0x000c: "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2A\n"
0xffffd0cc│+0x0010: "a1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2A\n"
0xffffd0d0│+0x0014: "2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2A\n"
0xffffd0d4│+0x0018: "Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2A\n"
0xffffd0d8│+0x001c: "a5Aa6Aa7Aa8Aa9Ab0Ab1Ab2A\n"
────────────────────────────────────────────────────────────────────────────────── code:x86:32 ────
[!] Cannot disassemble from $PC
[!] Cannot access memory at address 0x31624130
────────────────────────────────────────────────────────────────────────────────────── threads ────
[#0] Id 1, Name: "WinButTwisted", stopped 0x31624130 in ?? (), reason: SIGSEGV
──────────────────────────────────────────────────────────────────────────────────────── trace ────
───────────────────────────────────────────────────────────────────────────────────────────────────
gef➤  
```
