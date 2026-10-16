## ROP Emporium (x86-64) | Callme challenge!
A detailed write-up and exploit script for the challenge , this challenge demonstrates how to chain multiple function call in a specific order while passing parameters through registers.
**offset** : 40 bytes padding to reach and overwrite `RIP`.
**EXPLOIT STRATEGY:**
1. in the system AMD64 ABI convention (x86-64 linux),function arguments are passed via  registers in the following orders:
 **1st arg** : `RDI` 
 **2nd arg** : `RSI`
 **3rd arg** : `RDX`
2. To fulfill the requirements, we need a ROP gadget that sets these three registers in sequence: `pop rdi ; pop rsi ; pop rdx ; ret `.
  1. load arguments into `rdi` , `rsi` , `rdx` using pop gadget : `pop rdi ; pop rsi ; pop rdx ; ret`
  2. call callme_one function
  3. load arguments agin into `rdi` , `rsi` , `rdx` using pop gadget : `pop rdi ; pop rsi ; pop rdx ; ret`
  4. call callme_two function
  5. load arguments agin into `rdi` , `rsi` , `rdx` using pop gadget : `pop rdi ; pop rsi ; pop rdx ; ret`
  6. call callme_three function
  7. load argument (`0x0`) in `RDI` register. using :` pop rdi ; ret`.
  8. call `exit` function.

**the exploit payload is constructed as follows : **
  1. Buffer Overflow : `40 bytes` of padding ("`A`* 40") to reach `RIP` 
  2. the gadget : `pop rdi ; pop rsi ; pop rdx ; ret` :
      - 0xdeadbeefdeadbeef -> RDI
      - 0xcafebabecafebabe -> RSI
      - 0xd00df00dd00df00d -> RDX
  3. call `callme_one`
  4. the gadget : `pop rdi ; pop rsi ; pop rdx ; ret` :
      - 0xdeadbeefdeadbeef -> RDI
      - 0xcafebabecafebabe -> RSI
      - 0xd00df00dd00df00d -> RDX
  5. call `callme_two`
  6. the gadget : `pop rdi ; pop rsi ; pop rdx ; ret` :
      - 0xdeadbeefdeadbeef -> RDI
      - 0xcafebabecafebabe -> RSI
      - 0xd00df00dd00df00d -> RDX
  7. call `callme_three`
  8. the gadget : `pop rdi; ret`
      - 0x0 -> RDI
  9. call exit function ( exit address ).

**Usage**
Run the python exploit script using python3 (pwntools)
```bash
python3 exploit.py
