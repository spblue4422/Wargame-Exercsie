// https://dreamhack.io/wargame/challenges/812
// Name: chall.c
// Compile Option: gcc chall.c -o chall -fno-stack-protector

#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

#define FLAG_SIZE 0x45

void init() {
    // stdin, stdout에 대해 버퍼링 설정을 하지 않겠다.
    // 2번째 인자 0: 별도의 버퍼를 지정해서 사용하지 않겠다
    // 3번째 인자 2: 버퍼링이 없는 mode를 선택, 입력과 출력이 바로바로 나옴
    // 4번째 인자 0: 버퍼의 크기, 버퍼링이 없으니 버퍼 크기는 무의미
	setvbuf(stdin, 0, 2, 0);
	setvbuf(stdout, 0, 2, 0);
}

int main(void) {
    int fd;
    char *flag;

    init();

    // read flag
    flag = (char *)malloc(FLAG_SIZE);
    // flag 파일을 읽어서 flag 값을 읽어온다. => flag 파일에 내가 접근이 가능하면 Dreamhack을 치지 않아도 가능할듯?
    fd = open("./flag", O_RDONLY);
    read(fd, flag, FLAG_SIZE);

    char cmp_str[10] = "Dreamhack";
    char inp_str[10];   
    printf("Enter \"Dreamhack\" : ");
    // 입력 받기
    scanf("%9s", inp_str);

    // 입력이 cmp_str과 동일한지 확인
    if(strcmp(cmp_str, inp_str) == 0){
        puts("Welcome Beginners!");
        // print flag
        puts(flag);
    }
    
    return 0;
}