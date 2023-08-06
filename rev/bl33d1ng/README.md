# Reverse Engineering (Advanced)

**We are presented with the following:**

![Screen Shot 2020-10-13 at 11 07 41 am](https://user-images.githubusercontent.com/45506405/95810766-55999d80-0d44-11eb-83b0-91982b4d0973.png)

## Basic Static Analysis (BSA) - Step 1

**Downloading the file and running the "file" command shows that it is a linux executable**

![Screen Shot 2020-10-13 at 11 16 21 am](https://user-images.githubusercontent.com/45506405/95811304-8f1ed880-0d45-11eb-9f5d-3368e80e8a52.png)

## BSA - Step 2

**Executing the binary gives us the following output**

![Screen Shot 2020-10-13 at 11 24 42 am](https://user-images.githubusercontent.com/45506405/95811855-b924ca80-0d46-11eb-8f1e-fb17937bb07e.png)

The program will keep printing out the same output indefintely. Looks like we might have to conduct some further analysis.

## BSA - Step 3

**Open the binary using a disassembler/debugger**

```
root@kali:~/Desktop/stuff# r2 -w bl33d1ng
[0x00001060]> aaaa
[Cannot analyze at 0x00001050g with sym. and entry0 (aa)
[x] Analyze all flags starting with sym. and entry0 (aa)
[Cannot analyze at 0x00001050ac)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Check for objc references
[x] Check for vtables
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information
[x] Use -AA or aaaa to perform additional experimental analysis.
[x] Finding function preludes
[x] Enable constraint types analysis for variables
[0x00001060]> afl
0x00001060    1 42           entry0
0x00001090    4 41   -> 34   sym.deregister_tm_clones
0x000010c0    4 57   -> 51   sym.register_tm_clones
0x00001100    5 57   -> 50   entry.fini0
0x00001140    1 5            entry.init0
0x00001000    3 23           sym._init
0x00001470    1 1            sym.__libc_csu_fini
0x00001474    1 9            sym._fini
0x00001410    4 93           sym.__libc_csu_init
0x00001145    9 714          main
0x00001030    1 6            sym.imp.puts
0x00001040    1 6            sym.imp.sleep
[0x00001060]> s main
[0x00001145]> pdf
/ (fcn) main 714
|   int main (int argc, char **argv, char **envp);
|           ; var char *s @ rbp-0x30
|           ; var int32_t var_28h @ rbp-0x28
|           ; var int32_t var_20h @ rbp-0x20
|           ; var int32_t var_18h @ rbp-0x18
|           ; var int32_t var_10h @ rbp-0x10
|           ; var int32_t var_9h @ rbp-0x9
|           ; var uint32_t var_8h @ rbp-0x8
|           ; var uint32_t var_4h @ rbp-0x4
|           ; DATA XREF from entry0 @ 0x107d
|           0x00001145      55             push rbp                    ; bleeding.c:6 {
|           0x00001146      4889e5         mov rbp, rsp
|           0x00001149      4883ec30       sub rsp, 0x30
|           0x0000114d      488d3db00e00.  lea rdi, qword str.help_me  ; bleeding.c:8  printf("help me\n"); ; 0x2004 ; "help me" ; const char *s
|           0x00001154      e8d7feffff     call sym.imp.puts           ; int puts(const char *s)
|           0x00001159      bf02000000     mov edi, 2                  ; bleeding.c:9  sleep(2); ; int s
|           0x0000115e      e8ddfeffff     call sym.imp.sleep          ; int sleep(int s)
|           0x00001163      488d3da20e00.  lea rdi, qword str.i_am_bleeding ; bleeding.c:10  printf("i am bleeding\n"); ; 0x200c ; "i am bleeding" ; const char *s
|           0x0000116a      e8c1feffff     call sym.imp.puts           ; int puts(const char *s)
|           0x0000116f      bf02000000     mov edi, 2                  ; bleeding.c:11  sleep(2); ; int s
|           0x00001174      e8c7feffff     call sym.imp.sleep          ; int sleep(int s)
|           0x00001179      488d3d9a0e00.  lea rdi, qword str.before_its_too_late... ; bleeding.c:12  printf("before its too late...\n"); ; 0x201a ; "before its too late..." ; const char *s
|           0x00001180      e8abfeffff     call sym.imp.puts           ; int puts(const char *s)
|           0x00001185      c745f8010000.  mov dword [var_8h], 1       ; bleeding.c:14  int leak =  1;
|           0x0000118c      bf02000000     mov edi, 2                  ; bleeding.c:16  sleep(2); ; int s
|           0x00001191      e8aafeffff     call sym.imp.sleep          ; int sleep(int s)
|       ,=< 0x00001196      eb2c           jmp 0x11c4
|      .--> 0x00001198      488d3d920e00.  lea rdi, qword str.too_late ; bleeding.c:21   printf("too late!\n"); ; 0x2031 ; "too late!" ; const char *s
|      :|   0x0000119f      e88cfeffff     call sym.imp.puts           ; int puts(const char *s)
|      :|   0x000011a4      bf01000000     mov edi, 1                  ; bleeding.c:22   sleep(1); ; int s
|      :|   0x000011a9      e892feffff     call sym.imp.sleep          ; int sleep(int s)
|      :|   0x000011ae      488d3d860e00.  lea rdi, qword str.i_died_: ; bleeding.c:23   printf("i died :( \n"); ; 0x203b ; "i died :( " ; const char *s
|      :|   0x000011b5      e876feffff     call sym.imp.puts           ; int puts(const char *s)
|      :|   0x000011ba      bf01000000     mov edi, 1                  ; bleeding.c:24   sleep(1); ; int s
|      :|   0x000011bf      e87cfeffff     call sym.imp.sleep          ; int sleep(int s)
|      :|   ; CODE XREF from main @ 0x1196
|      :`-> 0x000011c4      837df801       cmp dword [var_8h], 1       ; bleeding.c:19  while (leak == 1)
|      `==< 0x000011c8      74ce           je 0x1198
|           0x000011ca      837df801       cmp dword [var_8h], 1       ; bleeding.c:28  if (leak != 1)
|       ,=< 0x000011ce      0f8434020000   je 0x1408
|       |   0x000011d4      488d3d6b0e00.  lea rdi, qword str.thank_you ; bleeding.c:30   printf("thank you\n"); ; 0x2046 ; "thank you" ; const char *s
|       |   0x000011db      e850feffff     call sym.imp.puts           ; int puts(const char *s)
|       |   0x000011e0      bf01000000     mov edi, 1                  ; bleeding.c:31   sleep(1); ; int s
|       |   0x000011e5      e856feffff     call sym.imp.sleep          ; int sleep(int s)
|       |   0x000011ea      488d3d5f0e00.  lea rdi, qword str.you_patched_me ; bleeding.c:32   printf("you patched me\n"); ; 0x2050 ; "you patched me" ; const char *s
|       |   0x000011f1      e83afeffff     call sym.imp.puts           ; int puts(const char *s)
|       |   0x000011f6      bf01000000     mov edi, 1                  ; bleeding.c:33   sleep(1); ; int s
|       |   0x000011fb      e840feffff     call sym.imp.sleep          ; int sleep(int s)
|       |   0x00001200      48b88a86878a.  movabs rax, 0x8086d0d58a87868a ; bleeding.c:37   unsigned char s[] =
|       |   0x0000120a      48ba82d28384.  movabs rdx, 0x8580818a8483d282
|       |   0x00001214      488945d0       mov qword [s], rax
|       |   0x00001218      488955d8       mov qword [var_28h], rdx
|       |   0x0000121c      48b886d28b82.  movabs rax, 0x848b8287828bd286
|       |   0x00001226      48ba8587d586.  movabs rdx, 0xd586d18286d58785
|       |   0x00001230      488945e0       mov qword [var_20h], rax
|       |   0x00001234      488955e8       mov qword [var_18h], rdx
|       |   0x00001238      c645f0b3       mov byte [var_10h], 0xb3
|       |   0x0000123c      c745fc000000.  mov dword [var_4h], 0       ; bleeding.c:47   for (unsigned int m = 0; m < sizeof(s); ++m)
|      ,==< 0x00001243      e9aa010000     jmp 0x13f2
|      ||   ; CODE XREF from main @ 0x13f6
|     .---> 0x00001248      8b45fc         mov eax, dword [var_4h]     ; bleeding.c:49       unsigned char c = s[m];
|     :||   0x0000124b      0fb64405d0     movzx eax, byte [rbp + rax - 0x30]
|     :||   0x00001250      8845f7         mov byte [var_9h], al
|     :||   0x00001253      8075f721       xor byte [var_9h], 0x21     ; bleeding.c:50       c ^= 0x21; ; [0x21:1]=0
|     :||   0x00001257      8075f7cb       xor byte [var_9h], 0xcb     ; bleeding.c:51       c ^= 0xcb; ; [0xcb:1]=0
|     :||   0x0000125b      8075f736       xor byte [var_9h], 0x36     ; bleeding.c:52       c ^= 0x36; ; [0x36:1]=56
|     :||   0x0000125f      8075f72f       xor byte [var_9h], 0x2f     ; bleeding.c:53       c ^= 0x2f; ; [0x2f:1]=0
|     :||   0x00001263      8075f75f       xor byte [var_9h], 0x5f     ; bleeding.c:54       c ^= 0x5f; ; [0x5f:1]=0
|     :||   0x00001267      8075f748       xor byte [var_9h], 0x48     ; bleeding.c:55       c ^= 0x48; ; [0x48:1]=64
|     :||   0x0000126b      8075f7f6       xor byte [var_9h], 0xf6     ; bleeding.c:56       c ^= 0xf6; ; [0xf6:1]=0
|     :||   0x0000126f      8075f7c2       xor byte [var_9h], 0xc2     ; bleeding.c:57       c ^= 0xc2; ; [0xc2:1]=0
|     :||   0x00001273      8075f70a       xor byte [var_9h], 0xa      ; bleeding.c:58       c ^= 0xa;
|     :||   0x00001277      8075f73a       xor byte [var_9h], 0x3a     ; bleeding.c:59       c ^= 0x3a; ; [0x3a:1]=64
|     :||   0x0000127b      8075f702       xor byte [var_9h], 2        ; bleeding.c:60       c ^= 0x2;
|     :||   0x0000127f      8075f7bc       xor byte [var_9h], 0xbc     ; bleeding.c:61       c ^= 0xbc; ; [0xbc:1]=0
|     :||   0x00001283      8075f740       xor byte [var_9h], 0x40     ; bleeding.c:62       c ^= 0x40; ; segment.PHDR
|     :||                                                              ; [0x40:1]=6
|     :||   0x00001287      8075f75d       xor byte [var_9h], 0x5d     ; bleeding.c:63       c ^= 0x5d; ; [0x5d:1]=0
|     :||   0x0000128b      8075f78f       xor byte [var_9h], 0x8f     ; bleeding.c:64       c ^= 0x8f; ; [0x8f:1]=0
|     :||   0x0000128f      8075f7e6       xor byte [var_9h], 0xe6     ; bleeding.c:65       c ^= 0xe6; ; [0xe6:1]=0
|     :||   0x00001293      8075f714       xor byte [var_9h], 0x14     ; bleeding.c:66       c ^= 0x14; ; [0x14:1]=1
|     :||   0x00001297      8075f74f       xor byte [var_9h], 0x4f     ; bleeding.c:67       c ^= 0x4f; ; [0x4f:1]=0
|     :||   0x0000129b      8075f7ac       xor byte [var_9h], 0xac     ; bleeding.c:68       c ^= 0xac; ; [0xac:1]=0
|     :||   0x0000129f      8075f75f       xor byte [var_9h], 0x5f     ; bleeding.c:69       c ^= 0x5f; ; [0x5f:1]=0
|     :||   0x000012a3      8075f7c0       xor byte [var_9h], 0xc0     ; bleeding.c:70       c ^= 0xc0; ; [0xc0:1]=0
|     :||   0x000012a7      8075f766       xor byte [var_9h], 0x66     ; bleeding.c:71       c ^= 0x66; ; [0x66:1]=0
|     :||   0x000012ab      8075f720       xor byte [var_9h], 0x20     ; bleeding.c:72       c ^= 0x20; ; [0x20:1]=64 ; "@"
|     :||   0x000012af      8075f7b0       xor byte [var_9h], 0xb0     ; bleeding.c:73       c ^= 0xb0; ; [0xb0:1]=1
|     :||   0x000012b3      8075f7e2       xor byte [var_9h], 0xe2     ; bleeding.c:74       c ^= 0xe2; ; [0xe2:1]=0
|     :||   0x000012b7      8075f746       xor byte [var_9h], 0x46     ; bleeding.c:75       c ^= 0x46; ; [0x46:1]=0
|     :||   0x000012bb      8075f726       xor byte [var_9h], 0x26     ; bleeding.c:76       c ^= 0x26; ; [0x26:1]=0
|     :||   0x000012bf      8075f780       xor byte [var_9h], 0x80     ; bleeding.c:77       c ^= 0x80; ; [0x80:1]=168
|     :||   0x000012c3      8075f754       xor byte [var_9h], 0x54     ; bleeding.c:78       c ^= 0x54; ; [0x54:1]=0
|     :||   0x000012c7      8075f7c8       xor byte [var_9h], 0xc8     ; bleeding.c:79       c ^= 0xc8; ; [0xc8:1]=0
|     :||   0x000012cb      8075f759       xor byte [var_9h], 0x59     ; bleeding.c:80       c ^= 0x59; ; [0x59:1]=0
|     :||   0x000012cf      8075f7c2       xor byte [var_9h], 0xc2     ; bleeding.c:81       c ^= 0xc2; ; [0xc2:1]=0
|     :||   0x000012d3      8075f7ae       xor byte [var_9h], 0xae     ; bleeding.c:82       c ^= 0xae; ; [0xae:1]=0
|     :||   0x000012d7      8075f7a5       xor byte [var_9h], 0xa5     ; bleeding.c:83       c ^= 0xa5; ; [0xa5:1]=0
|     :||   0x000012db      8075f7f1       xor byte [var_9h], 0xf1     ; bleeding.c:84       c ^= 0xf1; ; [0xf1:1]=16
|     :||   0x000012df      8075f75b       xor byte [var_9h], 0x5b     ; bleeding.c:85       c ^= 0x5b; ; [0x5b:1]=0
|     :||   0x000012e3      8075f7ae       xor byte [var_9h], 0xae     ; bleeding.c:86       c ^= 0xae; ; [0xae:1]=0
|     :||   0x000012e7      8075f79e       xor byte [var_9h], 0x9e     ; bleeding.c:87       c ^= 0x9e; ; [0x9e:1]=0
|     :||   0x000012eb      8075f7d8       xor byte [var_9h], 0xd8     ; bleeding.c:88       c ^= 0xd8; ; [0xd8:1]=152
|     :||   0x000012ef      8075f7d6       xor byte [var_9h], 0xd6     ; bleeding.c:89       c ^= 0xd6; ; [0xd6:1]=0
|     :||   0x000012f3      8075f734       xor byte [var_9h], 0x34     ; bleeding.c:90       c ^= 0x34; ; [0x34:1]=64
|     :||   0x000012f7      8075f709       xor byte [var_9h], 9        ; bleeding.c:91       c ^= 0x9;
|     :||   0x000012fb      8075f705       xor byte [var_9h], 5        ; bleeding.c:92       c ^= 0x5;
|     :||   0x000012ff      8075f76a       xor byte [var_9h], 0x6a     ; bleeding.c:93       c ^= 0x6a; ; [0x6a:1]=0
|     :||   0x00001303      8075f7f7       xor byte [var_9h], 0xf7     ; bleeding.c:94       c ^= 0xf7; ; [0xf7:1]=0
|     :||   0x00001307      8075f758       xor byte [var_9h], 0x58     ; bleeding.c:95       c ^= 0x58; ; [0x58:1]=64
|     :||   0x0000130b      8075f71c       xor byte [var_9h], 0x1c     ; bleeding.c:96       c ^= 0x1c; ; [0x1c:1]=0
|     :||   0x0000130f      8075f749       xor byte [var_9h], 0x49     ; bleeding.c:97       c ^= 0x49; ; [0x49:1]=0
|     :||   0x00001313      8075f7b1       xor byte [var_9h], 0xb1     ; bleeding.c:98       c ^= 0xb1; ; [0xb1:1]=0
|     :||   0x00001317      8075f713       xor byte [var_9h], 0x13     ; bleeding.c:99       c ^= 0x13; ; [0x13:1]=0
|     :||   0x0000131b      8075f771       xor byte [var_9h], 0x71     ; bleeding.c:100       c ^= 0x71; ; [0x71:1]=0
|     :||   0x0000131f      8075f776       xor byte [var_9h], 0x76     ; bleeding.c:101       c ^= 0x76; ; [0x76:1]=0
|     :||   0x00001323      8075f705       xor byte [var_9h], 5        ; bleeding.c:102       c ^= 0x5;
|     :||   0x00001327      8075f75d       xor byte [var_9h], 0x5d     ; bleeding.c:103       c ^= 0x5d; ; [0x5d:1]=0
|     :||   0x0000132b      8075f730       xor byte [var_9h], 0x30     ; bleeding.c:104       c ^= 0x30; ; [0x30:1]=0
|     :||   0x0000132f      8075f781       xor byte [var_9h], 0x81     ; bleeding.c:105       c ^= 0x81; ; [0x81:1]=2
|     :||   0x00001333      8075f722       xor byte [var_9h], 0x22     ; bleeding.c:106       c ^= 0x22; ; [0x22:1]=0
|     :||   0x00001337      8075f7a3       xor byte [var_9h], 0xa3     ; bleeding.c:107       c ^= 0xa3; ; [0xa3:1]=0
|     :||   0x0000133b      8075f792       xor byte [var_9h], 0x92     ; bleeding.c:108       c ^= 0x92; ; [0x92:1]=0
|     :||   0x0000133f      8075f70f       xor byte [var_9h], 0xf      ; bleeding.c:109       c ^= 0xf; ; [0xf:1]=0
|     :||   0x00001343      8075f7dc       xor byte [var_9h], 0xdc     ; bleeding.c:110       c ^= 0xdc; ; [0xdc:1]=0
|     :||   0x00001347      8075f72b       xor byte [var_9h], 0x2b     ; bleeding.c:111       c ^= 0x2b; ; [0x2b:1]=0
|     :||   0x0000134b      8075f796       xor byte [var_9h], 0x96     ; bleeding.c:112       c ^= 0x96; ; [0x96:1]=0
|     :||   0x0000134f      8075f79a       xor byte [var_9h], 0x9a     ; bleeding.c:113       c ^= 0x9a; ; [0x9a:1]=0
|     :||   0x00001353      8075f718       xor byte [var_9h], 0x18     ; bleeding.c:114       c ^= 0x18; ; [0x18:1]=96
|     :||   0x00001357      8075f73f       xor byte [var_9h], 0x3f     ; bleeding.c:115       c ^= 0x3f; ; [0x3f:1]=0
|     :||   0x0000135b      8075f7f1       xor byte [var_9h], 0xf1     ; bleeding.c:116       c ^= 0xf1; ; [0xf1:1]=16
|     :||   0x0000135f      8075f7aa       xor byte [var_9h], 0xaa     ; bleeding.c:117       c ^= 0xaa; ; [0xaa:1]=0
|     :||   0x00001363      8075f75e       xor byte [var_9h], 0x5e     ; bleeding.c:118       c ^= 0x5e; ; [0x5e:1]=0
|     :||   0x00001367      8075f79c       xor byte [var_9h], 0x9c     ; bleeding.c:119       c ^= 0x9c; ; [0x9c:1]=0
|     :||   0x0000136b      8075f758       xor byte [var_9h], 0x58     ; bleeding.c:120       c ^= 0x58; ; [0x58:1]=64
|     :||   0x0000136f      8075f727       xor byte [var_9h], 0x27     ; bleeding.c:121       c ^= 0x27; ; [0x27:1]=0
|     :||   0x00001373      8075f7ae       xor byte [var_9h], 0xae     ; bleeding.c:122       c ^= 0xae; ; [0xae:1]=0
|     :||   0x00001377      8075f798       xor byte [var_9h], 0x98     ; bleeding.c:123       c ^= 0x98; ; [0x98:1]=28
|     :||   0x0000137b      8075f7c2       xor byte [var_9h], 0xc2     ; bleeding.c:124       c ^= 0xc2; ; [0xc2:1]=0
|     :||   0x0000137f      8075f7cd       xor byte [var_9h], 0xcd     ; bleeding.c:125       c ^= 0xcd; ; [0xcd:1]=0
|     :||   0x00001383      8075f77f       xor byte [var_9h], 0x7f     ; bleeding.c:126       c ^= 0x7f; ; [0x7f:1]=0
|     :||   0x00001387      8075f733       xor byte [var_9h], 0x33     ; bleeding.c:127       c ^= 0x33; ; [0x33:1]=0
|     :||   0x0000138b      8075f72d       xor byte [var_9h], 0x2d     ; bleeding.c:128       c ^= 0x2d; ; [0x2d:1]=0
|     :||   0x0000138f      8075f738       xor byte [var_9h], 0x38     ; bleeding.c:129       c ^= 0x38; ; [0x38:1]=11
|     :||   0x00001393      8075f716       xor byte [var_9h], 0x16     ; bleeding.c:130       c ^= 0x16; ; [0x16:1]=0
|     :||   0x00001397      8075f7a4       xor byte [var_9h], 0xa4     ; bleeding.c:131       c ^= 0xa4; ; [0xa4:1]=0
|     :||   0x0000139b      8075f7aa       xor byte [var_9h], 0xaa     ; bleeding.c:132       c ^= 0xaa; ; [0xaa:1]=0
|     :||   0x0000139f      8075f7f5       xor byte [var_9h], 0xf5     ; bleeding.c:133       c ^= 0xf5; ; [0xf5:1]=0
|     :||   0x000013a3      8075f7ee       xor byte [var_9h], 0xee     ; bleeding.c:134       c ^= 0xee; ; [0xee:1]=0
|     :||   0x000013a7      8075f75d       xor byte [var_9h], 0x5d     ; bleeding.c:135       c ^= 0x5d; ; [0x5d:1]=0
|     :||   0x000013ab      8075f735       xor byte [var_9h], 0x35     ; bleeding.c:136       c ^= 0x35; ; [0x35:1]=0
|     :||   0x000013af      8075f712       xor byte [var_9h], 0x12     ; bleeding.c:137       c ^= 0x12; ; [0x12:1]=62
|     :||   0x000013b3      8075f79c       xor byte [var_9h], 0x9c     ; bleeding.c:138       c ^= 0x9c; ; [0x9c:1]=0
|     :||   0x000013b7      8075f785       xor byte [var_9h], 0x85     ; bleeding.c:139       c ^= 0x85; ; [0x85:1]=0
|     :||   0x000013bb      8075f7ac       xor byte [var_9h], 0xac     ; bleeding.c:140       c ^= 0xac; ; [0xac:1]=0
|     :||   0x000013bf      8075f797       xor byte [var_9h], 0x97     ; bleeding.c:141       c ^= 0x97; ; [0x97:1]=0
|     :||   0x000013c3      8075f729       xor byte [var_9h], 0x29     ; bleeding.c:142       c ^= 0x29; ; [0x29:1]=69
|     :||   0x000013c7      8075f703       xor byte [var_9h], 3        ; bleeding.c:143       c ^= 0x3;
|     :||   0x000013cb      8075f789       xor byte [var_9h], 0x89     ; bleeding.c:144       c ^= 0x89; ; [0x89:1]=2
|     :||   0x000013cf      8075f705       xor byte [var_9h], 5        ; bleeding.c:145       c ^= 0x5;
|     :||   0x000013d3      8075f77d       xor byte [var_9h], 0x7d     ; bleeding.c:146       c ^= 0x7d; ; [0x7d:1]=0
|     :||   0x000013d7      8075f7a1       xor byte [var_9h], 0xa1     ; bleeding.c:147       c ^= 0xa1; ; [0xa1:1]=0
|     :||   0x000013db      8075f70e       xor byte [var_9h], 0xe      ; bleeding.c:148       c ^= 0xe; ; [0xe:1]=0
|     :||   0x000013df      8075f710       xor byte [var_9h], 0x10     ; bleeding.c:149       c ^= 0x10; ; [0x10:1]=3
|     :||   0x000013e3      8b45fc         mov eax, dword [var_4h]     ; bleeding.c:150       s[m] = c;
|     :||   0x000013e6      0fb655f7       movzx edx, byte [var_9h]
|     :||   0x000013ea      885405d0       mov byte [rbp + rax - 0x30], dl
|     :||   0x000013ee      8345fc01       add dword [var_4h], 1       ; bleeding.c:47   for (unsigned int m = 0; m < sizeof(s); ++m)
|     :||   ; CODE XREF from main @ 0x1243
|     :`--> 0x000013f2      837dfc20       cmp dword [var_4h], 0x20
|     `===< 0x000013f6      0f864cfeffff   jbe 0x1248
|       |   0x000013fc      488d45d0       lea rax, qword [s]
|       |   0x00001400      4889c7         mov rdi, rax                ; const char *s
|       |   0x00001403      e828fcffff     call sym.imp.puts           ; bleeding.c:31   sleep(1); ; int puts(const char *s)
|       |   ; CODE XREF from main @ 0x11ce
|       `-> 0x00001408      b800000000     mov eax, 0
|           0x0000140d      c9             leave
\           0x0000140e      c3             ret
```

Looking at the binary we can see at this instruction/address ```0x00001196  eb2c   jmp 0x11c4 ; bleeding.c:19  while (leak == 1)```
When the binary jumps to address 11c4, the following instructions are executed:

```
0x000011c4      837df801       cmp dword [var_8h], 1       ; bleeding.c:19  while (leak == 1)
0x000011c8      74ce           je 0x1198
```

The program checks to see if ```var_8h``` is equal to 1, and if it is, then the binary jumps to address ```0x1198```, the following code is then executed:

```
0x00001198      488d3d920e00.  lea rdi, qword str.too_late ; bleeding.c:21   printf("too late!\n"); ; 0x2031 ; "too late!" ; const char *s
0x0000119f      e88cfeffff     call sym.imp.puts           ; int puts(const char *s)
0x000011a4      bf01000000     mov edi, 1                  ; bleeding.c:22   sleep(1); ; int s
0x000011a9      e892feffff     call sym.imp.sleep          ; int sleep(int s)
0x000011ae      488d3d860e00.  lea rdi, qword str.i_died_: ; bleeding.c:23   printf("i died :( \n"); ; 0x203b ; "i died :( " ; const char *s
0x000011b5      e876feffff     call sym.imp.puts           ; int puts(const char *s)
0x000011ba      bf01000000     mov edi, 1                  ; bleeding.c:24   sleep(1); ; int s
0x000011bf      e87cfeffff     call sym.imp.sleep          ; int sleep(int s)
```

This code prints out the following text:

```
    too late!
    i died :(
```

After printing out these statements, the program checks if the ```var_8h``` variable is equal to 1 and so on.

## BSA Step 4

**Patching a Statement**

From this analysis, we can determine that patching an instruction will prevent this loop from executing in the first place.

If we patch this ```0x000011c8  74ce je 0x1198``` instruction to a ```jmp``` instruction, we can avoid the loop entirely. The question is where to provide the address for the jmp instruction to go to.

Scrolling down one instruction from the original ```je 0x1198``` instruction, we can see the binary executes the following instructions if ```var_8h``` is not equal to 1:

```
0x000011ca      837df801       cmp dword [var_8h], 1       ; bleeding.c:28  if (leak != 1)
0x000011ce      0f8434020000   je 0x1408
0x000011d4      488d3d6b0e00.  lea rdi, qword str.thank_you ; bleeding.c:30   printf("thank you\n"); ; 0x2046 ; "thank you" ; const char *s
0x000011db      e850feffff     call sym.imp.puts           ; int puts(const char *s)
0x000011e0      bf01000000     mov edi, 1                  ; bleeding.c:31   sleep(1); ; int s
0x000011e5      e856feffff     call sym.imp.sleep          ; int sleep(int s)
0x000011ea      488d3d5f0e00.  lea rdi, qword str.you_patched_me ; bleeding.c:32   printf("you patched me\n"); ; 0x2050 ; "you patched me" ; const char *s
```

This jump will lead to an return 0 statement and will cause the program to "return 0" and exit. However if we can avoid this jump, then the program flow will continue and the the bytes stored in variable ```local_9h``` will be xored with the long list of keys. This should reveal the secret flag.

If we patch the original statement at address 0x00001196 ```jmp 0x11c4``` to ```jmp 0x11d4```, then we can jump directly to the decryption code.

To patch a statement, the following commands will be run in radare2 respectively, and will be run once:
```V``` - to go to visual mode (capital V)
```p``` - to print out the diassembly (lowercase p)

We will scroll down to the address ```0x00001196``` which should appear as below:
![bl33d1ng](https://user-images.githubusercontent.com/45506405/95939407-99f17000-0e0e-11eb-970a-d517dc56edb3.png)

We will now edit this instruction by pressing ```shift+a```, which would result in the following prompt:
![bl33d1ng](https://user-images.githubusercontent.com/45506405/95939958-d8d3f580-0e0f-11eb-938c-4e30a34a2582.png)

We will edit the instruction to ```jmp 0x11d4``` which will result in the following:
![image](https://user-images.githubusercontent.com/45506405/95940094-2f413400-0e10-11eb-9362-affb0b3be384.png)

Next, to save the changes we have made, press enter. Radare2 will ask you to confirm your changes. Enter 'Y'. To test this patch, exit Radare 2.

## BSA Step 5

**Testing new control path**

Execute the program once more:

![bl33d1ng](https://user-images.githubusercontent.com/45506405/95940359-b2fb2080-0e10-11eb-9238-fb6a484b09c3.png)

**We have patched the program and were able to reverse engineer it to give us the flag, as shown by the md5 flag.**
