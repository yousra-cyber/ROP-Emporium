# ROP Emporuim - callme (x86-64) ! A detailed write-up and exploit for the **callme** challenge.
**Architecture : 64-bit (ELF)**
**security protections : NX enabled , NO PIE , etc.**

## solution Overview:
1. **offset**: using a cyclic pattern , we determined that the offset to overwrite the instruction pointer `RIP` -40 bytes- .
2. **Gadgets**:
   -`pop rdi ; pop rsi ; pop rdx ;ret` : used to load the required arguments into the registers before calling each function .
    - the required arguments for all three functions (`callme_one`|`callme_two`|`callme_three` ) are:
      - Argument 1 :` 0xdeadbeefdeadbeef`
      - Argument 2 : `0xcafebabcafebabe`
      - Argument 3 : `0xd00df00dd00df00d`
   - `pop rdi` : used to load `0x0` into the rdi register as an `argument 4` for the exit function.
3. ** Payload structure** :
  the final ROP chain follows this repetitive sequence :
 [padding (40 bytes) ] -> [POp Gadget ] -> [arg 1] -> [arg 2] -> [Arg3] -> [call target function](repeat for one , two and three ) -> [pop_rdi] -> [arg4] :
4.**run the exploit script using python 3 ( pwntools library)**
```bash
python exploit.py
