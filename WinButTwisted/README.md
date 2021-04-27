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
