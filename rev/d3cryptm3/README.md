# Reverse Engineering (Advanced)

![d3cryptm3](https://user-images.githubusercontent.com/45506405/96070623-26fdfd00-0ed3-11eb-95a0-4ee92f95b825.png)

## Basic Static Analysis (BSA) - Step 1

**Downloading the file and running the "file" command shows that it is a linux executable:**

![d3cryptm3](https://user-images.githubusercontent.com/45506405/96070863-95db5600-0ed3-11eb-8acc-59be1579d408.png)

We can also see that the executable has been stripped

## BSA - Step 2 ##

**Executing the binary gives us the following output**

![d3cryptm3](https://user-images.githubusercontent.com/45506405/96071285-5e20de00-0ed4-11eb-8f7e-aa8840235933.png)

Looks like our input is being compared to something...

## BSA - Step 3 ##

**Open the binary using a disassembler/debugger**

```
sdevalpa@LAPTOP-LAFUS4CN:~$ r2 -w d3cryptm3
[0x000010b0]> aaaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze len bytes of instructions for references (aar)
[x] Analyze function calls (aac)
[x] Emulate code to find computed references (aae)
[x] Analyze consecutive function (aat)
[x] Constructing a function name for fcn.* and sym.func.* functions (aan)
[x] Type matching analysis for all functions (afta)
[0x000010b0]> afl
0x00001000    3 23           sub.__gmon_start___232_0
0x00001030    1 6            sym.imp.puts
0x00001040    1 6            sym.imp.strlen
0x00001050    1 6            sym.imp.printf
0x00001060    1 6            sym.imp.fgets
0x00001070    1 6            sym.imp.strcmp
0x00001080    1 6            sym.imp.exit
0x00001090    1 6            sym.imp.sleep
0x000010a0    1 6            sub.__cxa_finalize_248_a0
0x000010b0    1 43           entry0
0x000010e0    3 33           sub._ITM_deregisterTMCloneTable_216_e0
0x00001150    4 49           entry2.fini
0x00001190    5 5    -> 56   entry1.init
0x00001195    1 261          main
0x0000129a    6 270          sub.Checking_each_byte..._29a
0x000013a8    3 75           sub.strlen_3a8
[0x000010b0]> s main
[0x00001195]> pdf
/ (fcn) main 261
|   main ();
|           ; var int local_b0h @ rbp-0xb0
|           ; var int local_a8h @ rbp-0xa8
|           ; var int local_a0h @ rbp-0xa0
|           ; var int local_98h @ rbp-0x98
|           ; var int local_90h @ rbp-0x90
|           ; var int local_8eh @ rbp-0x8e
|           ; var int local_80h @ rbp-0x80
|           ; var int local_10h @ rbp-0x10
|           ; var int local_8h @ rbp-0x8
|              ; DATA XREF from 0x000010cd (entry0)
|           0x00001195      55             push rbp
|           0x00001196      4889e5         mov rbp, rsp
|           0x00001199      4881ecb00000.  sub rsp, 0xb0
|           0x000011a0      488d3d610e00.  lea rdi, qword str.Attention_Earthling ; 0x2008 ; "Attention Earthling!" ; const char * s
|           0x000011a7      e884feffff     call sym.imp.puts           ; int puts(const char *s)
|           0x000011ac      bf01000000     mov edi, 1                  ; int s
|           0x000011b1      e8dafeffff     call sym.imp.sleep          ; int sleep(int s)
|           0x000011b6      488d3d600e00.  lea rdi, qword str.To_Enter_Kryptonian_Airspace ; 0x201d ; "To Enter Kryptonian Airspace," ; const char * s
|           0x000011bd      e86efeffff     call sym.imp.puts           ; int puts(const char *s)
|           0x000011c2      bf01000000     mov edi, 1                  ; int s
|           0x000011c7      e8c4feffff     call sym.imp.sleep          ; int sleep(int s)
|           0x000011cc      488d3d6d0e00.  lea rdi, qword str.You_must_a_pre_approved_token: ; 0x2040 ; "You must a pre-approved token: " ; const char * format
|           0x000011d3      b800000000     mov eax, 0
|           0x000011d8      e873feffff     call sym.imp.printf         ; int printf(const char *format)
|           0x000011dd      488b157c2e00.  mov rdx, qword [obj.stdin]  ; rdi ; [0x4060:8]=0 ; FILE *stream
|           0x000011e4      488d4580       lea rax, qword [local_80h]
|           0x000011e8      be64000000     mov esi, 0x64               ; 'd' ; int size
|           0x000011ed      4889c7         mov rdi, rax                ; char *s
|           0x000011f0      e86bfeffff     call sym.imp.fgets          ; char *fgets(char *s, int size, FILE *stream)
|           0x000011f5      488d4580       lea rax, qword [local_80h]
|           0x000011f9      488945f8       mov qword [local_8h], rax
|           0x000011fd      488b45f8       mov rax, qword [local_8h]
|           0x00001201      4889c7         mov rdi, rax                ; const char * s
|           0x00001204      e89f010000     call sub.strlen_3a8         ; size_t strlen(const char *s)
|           0x00001209      48b8c2c09595.  movabs rax, -0x6d6d383a6a6a3f3e
|           0x00001213      48ba929494c1.  movabs rdx, -0x3d3f3b6a3e6b6b6e
|           0x0000121d      48898550ffff.  mov qword [local_b0h], rax
|           0x00001224      48899558ffff.  mov qword [local_a8h], rdx
|           0x0000122b      48b8c397c892.  movabs rax, -0x6f6b3c6d6d37683d
|           0x00001235      48ba9793c6c7.  movabs rdx, -0x3a376c6b38396c69
|           0x0000123f      48898560ffff.  mov qword [local_a0h], rax
|           0x00001246      48899568ffff.  mov qword [local_98h], rdx
|           0x0000124d      66c78570ffff.  mov word [local_90h], 0xfbfb
|           0x00001256      c68572ffffff.  mov byte [local_8eh], 0xf1
|           0x0000125d      488d8550ffff.  lea rax, qword [local_b0h]
|           0x00001264      488945f0       mov qword [local_10h], rax
|           0x00001268      488d4580       lea rax, qword [local_80h]
|           0x0000126c      4889c6         mov rsi, rax
|           0x0000126f      488d3dea0d00.  lea rdi, qword str.Sending___s__to_air_control ; 0x2060 ; "Sending '%s' to air control\n" ; const char * format
|           0x00001276      b800000000     mov eax, 0
|           0x0000127b      e8d0fdffff     call sym.imp.printf         ; int printf(const char *format)
|           0x00001280      488b55f0       mov rdx, qword [local_10h]
|           0x00001284      488b45f8       mov rax, qword [local_8h]
|           0x00001288      4889d6         mov rsi, rdx
|           0x0000128b      4889c7         mov rdi, rax
|           0x0000128e      e807000000     call sub.Checking_each_byte..._29a
|           0x00001293      b800000000     mov eax, 0
|           0x00001298      c9             leave
\           0x00001299      c3             ret
```

Looking at the binary, we can see that, after the program prints out ```You must a pre-approved token:``` at address ```0x000011cc```, the program then calls ```sub.Checking_each_byte..._29a``` at address ```0x0000128e```. The instructions after "You must a pre-approved token" are irrelevant.

We can see that after the program prompts the user for input, the rsi and rdi registers are passed into this ```sub.Checking_each_byte..._29a`` function.

## BSA Step 5

**Performing further static analysis**

It has become clear that the user input is being passed into the ```sub.Checking_each_byte..._29a``` function so we need to figure out what this function is doing. To view the disassembly of this function, we will enter the following commands:

```
[0x00001195]> s sub.Checking_each_byte..._29a
[0x0000129a]> pdf
/ (fcn) sub.Checking_each_byte..._29a 270
|   sub.Checking_each_byte..._29a ();
|           ; var int local_20h @ rbp-0x20
|           ; var int local_18h @ rbp-0x18
|           ; var int local_6h @ rbp-0x6
|           ; var int local_5h @ rbp-0x5
|           ; var int local_4h @ rbp-0x4
|              ; CALL XREF from 0x0000128e (main)
|           0x0000129a      55             push rbp
|           0x0000129b      4889e5         mov rbp, rsp
|           0x0000129e      4883ec20       sub rsp, 0x20
|           0x000012a2      48897de8       mov qword [local_18h], rdi
|           0x000012a6      488975e0       mov qword [local_20h], rsi
|           0x000012aa      488d3dcc0d00.  lea rdi, qword str.Checking_each_byte... ; 0x207d ; "Checking each byte..." ; const char * s
|           0x000012b1      e87afdffff     call sym.imp.puts           ; int puts(const char *s)
|           0x000012b6      c745fc000000.  mov dword [local_4h], 0
|       ,=< 0x000012bd      eb32           jmp 0x12f1
|       |      ; JMP XREF from 0x000012f7 (sub.Checking_each_byte..._29a)
|      .--> 0x000012bf      8b45fc         mov eax, dword [local_4h]
|      :|   0x000012c2      4863d0         movsxd rdx, eax
|      :|   0x000012c5      488b45e8       mov rax, qword [local_18h]
|      :|   0x000012c9      4801d0         add rax, rdx                ; '('
|      :|   0x000012cc      0fb600         movzx eax, byte [rax]
|      :|   0x000012cf      8845fb         mov byte [local_5h], al
|      :|   0x000012d2      8075fbad       xor byte [local_5h], 0xad
|      :|   0x000012d6      8075fb5c       xor byte [local_5h], 0x5c
|      :|   0x000012da      8b45fc         mov eax, dword [local_4h]
|      :|   0x000012dd      4863d0         movsxd rdx, eax
|      :|   0x000012e0      488b45e8       mov rax, qword [local_18h]
|      :|   0x000012e4      4801c2         add rdx, rax                ; '#'
|      :|   0x000012e7      0fb645fb       movzx eax, byte [local_5h]
|      :|   0x000012eb      8802           mov byte [rdx], al
|      :|   0x000012ed      8345fc01       add dword [local_4h], 1
|      :|      ; JMP XREF from 0x000012bd (sub.Checking_each_byte..._29a)
|      :`-> 0x000012f1      8b45fc         mov eax, dword [local_4h]
|      :    0x000012f4      83f807         cmp eax, 7
|      `==< 0x000012f7      76c6           jbe 0x12bf
|           0x000012f9      488b55e0       mov rdx, qword [local_20h]
|           0x000012fd      488b45e8       mov rax, qword [local_18h]
|           0x00001301      4889d6         mov rsi, rdx                ; const char * s2
|           0x00001304      4889c7         mov rdi, rax                ; const char * s1
|           0x00001307      e864fdffff     call sym.imp.strcmp         ; int strcmp(const char *s1, const char *s2)
|           0x0000130c      85c0           test eax, eax
|       ,=< 0x0000130e      754c           jne 0x135c
|       |   0x00001310      bf01000000     mov edi, 1                  ; int s
|       |   0x00001315      e876fdffff     call sym.imp.sleep          ; int sleep(int s)
|       |   0x0000131a      488d3d720d00.  lea rdi, qword str.Your_token_has_been_verified ; 0x2093 ; "Your token has been verified!" ; const char * s
|       |   0x00001321      e80afdffff     call sym.imp.puts           ; int puts(const char *s)
|       |   0x00001326      bf01000000     mov edi, 1                  ; int s
|       |   0x0000132b      e860fdffff     call sym.imp.sleep          ; int sleep(int s)
|       |   0x00001330      488d45fa       lea rax, qword [local_6h]
|       |   0x00001334      4889c6         mov rsi, rax
|       |   0x00001337      488d3d7a0d00.  lea rdi, qword str.Here_is_the_decrypted_text___s ; 0x20b8 ; "Here is the decrypted text! %s\n" ; const char * format
|       |   0x0000133e      b800000000     mov eax, 0
|       |   0x00001343      e808fdffff     call sym.imp.printf         ; int printf(const char *format)
|       |   0x00001348      bf01000000     mov edi, 1                  ; int s
|       |   0x0000134d      e83efdffff     call sym.imp.sleep          ; int sleep(int s)
|       |   0x00001352      bf00000000     mov edi, 0                  ; int status
|       |   0x00001357      e824fdffff     call sym.imp.exit           ; void exit(int status)
|       |      ; JMP XREF from 0x0000130e (sub.Checking_each_byte..._29a)
|       `-> 0x0000135c      bf01000000     mov edi, 1                  ; int s
|           0x00001361      e82afdffff     call sym.imp.sleep          ; int sleep(int s)
|           0x00001366      488d3d6b0d00.  lea rdi, qword str.Your_token_could_not_be_verified ; 0x20d8 ; "Your token could not be verified!" ; const char * s
|           0x0000136d      e8befcffff     call sym.imp.puts           ; int puts(const char *s)
|           0x00001372      bf01000000     mov edi, 1                  ; int s
|           0x00001377      e814fdffff     call sym.imp.sleep          ; int sleep(int s)
|           0x0000137c      488d3d770d00.  lea rdi, qword str.Please_try_again... ; 0x20fa ; "Please try again..." ; const char * s
|           0x00001383      e8a8fcffff     call sym.imp.puts           ; int puts(const char *s)

```

Looking at the function we can see that after the program prints out ```Checking each byte...```, the program jumps to address ```0x000012f1```, the program intiates a loop that repeats 8 times, with each loop xoring each byte (stored in ```local_5h```) with the following keys: ```0xad``` and ```0x5c```. At the end of the loop, the program increments the ```local_4h``` by one and compares it to 7. **Ultimately, this means that only the first 8 bytes of the user's input will be encrypted.**

```
0x000012bf      8b45fc         mov eax, dword [local_4h]
0x000012c2      4863d0         movsxd rdx, eax
0x000012c5      488b45e8       mov rax, qword [local_18h]
0x000012c9      4801d0         add rax, rdx                ; '('
0x000012cc      0fb600         movzx eax, byte [rax]
0x000012cf      8845fb         mov byte [local_5h], al
0x000012d2      8075fbad       xor byte [local_5h], 0xad
0x000012d6      8075fb5c       xor byte [local_5h], 0x5c
0x000012da      8b45fc         mov eax, dword [local_4h]
0x000012dd      4863d0         movsxd rdx, eax
0x000012e0      488b45e8       mov rax, qword [local_18h]
0x000012e4      4801c2         add rdx, rax                ; '#'
0x000012e7      0fb645fb       movzx eax, byte [local_5h]
0x000012eb      8802           mov byte [rdx], al
0x000012ed      8345fc01       add dword [local_4h], 1
0x000012f1      8b45fc         mov eax, dword [local_4h]
0x000012f7      76c6           jbe 0x12bf
```

Once this variable equals 7, the program compares two strings at address ```0x00001307```:

If the comparison is not equal to zero, the program prints out the following text:

```
    Your token could not be verified
    Please try again...
    Goodbye...
```

The program proceeds to exit.

However, if the comparison is succesful, the program will print out the following:

```
    Your token has been verified
    Here is the decrypted text %s
```

## Step 6

**Perform dynamic analysis**

Now that we now how the program works, we need to understand what's being compared at address ```0x00001307```. To do this, we'll need to enter debugging mode.

```
sdevalpa@LAPTOP-LAFUS4CN:~$ r2 -d d3cryptm3
```

The same commands from above were executed (including the seek into the ```Checking_each_byte...``` function.

Next, a breakpoint needs to be set at an address so that we can view the value of the registers. We will set the breakpoint at address ```0x7f842700f30c```. This instruction is the instruction after the ```sym.imp.strcmp``` function is called so we know that the registers have been populated.

To set the breakpoint, the following command was executed:

```
db 0x7f842700f30c
```

Next, we need to execute the program, to do this, execute the following command: ```dc```. The program will start executing and you will see the following:

*I've entered "somerandomgarbageinput" for the user input but this can be anything.*

![d3cryptm3](https://user-images.githubusercontent.com/45506405/96096997-09e12280-0f03-11eb-8507-60838281937c.png)

Next, we need to view the values of the registers so we will execute the following command ```dr```:

![d3cryptm3](https://user-images.githubusercontent.com/45506405/96097677-d5ba3180-0f03-11eb-896b-970df37d78f0.png)

We know that after encrypting the user input, the following code is executed:

```
0x7f842700f2f9      488b55e0       mov rdx, qword [local_20h]
0x7f842700f2fd      488b45e8       mov rax, qword [local_18h]
0x7f842700f301      4889d6         mov rsi, rdx            ; const char * s2
0x7f842700f304      4889c7         mov rdi, rax            ; const char * s1
0x7f842700f307      e864fdffff     call sym.imp.strcmp     ; int strcmp(const char *s1, const char *s2)
0x7f842700f30c      85c0           test eax, eax
```

If we print out the values of ```rsi``` and ```rdi``` then we can find out whats being compared. From the output that ```dr``` gave us, we can see the memory locations of these two registers.

```
    rsi = 0x7fffc36d4a90
    rdi = 0x7fffc36d4ac0
```

To print out the two values stored at these memory locations, we will execute the following command ```ps``` (print string):

```
    ps @ 0x7fffc36d4a90
    ps @ 0x7fffc36d4ac0
```

This gives us the following output:

![d3cryptm3](https://user-images.githubusercontent.com/45506405/96099082-6e9d7c80-0f05-11eb-8673-6a7542827b4c.png)

We can see that the first memory location is storing the encrypted text (**its 32 characters**) and also appears to be in a **hexadecimal format**.

The second memory location is storing our user input.
**Note: Only the first 8 characters of our user input has been encrypted (s o m e r a n d) and the rest of the characters are still in plaintext. This means that even if we had the right plaintext, the program wouldn't encrypt all charaters thus giving us an error message**.

However, we now posess the encrypted flag. We also know that the program was encrpyting the user input by using the keys ```ad``` and ```5c```. This means that we can decrypt the plain text :) using a tool such as **CyberChef**:

![d3cryptm3](https://user-images.githubusercontent.com/45506405/96100512-08b1f480-0f07-11eb-99d4-06e6ec9bb6c6.png)

**We can now see the decrypted flag, which is in an md5 format! (31dd46cccee0d5132f9cc2eafb76eb94)**
