## ROP Emporium (x86-64) write4 challenge !
A detailed write-up and exploit script for challenge . this challenge demonstrates how to write an arbitrary string (flag.txt) into  writable memory (`.data ` section) using a write gadget when the string is not present in the binary.
**Read the flag by passing the filename`"flag.txt"` to the `print_file` function , the string (`flag.txt`) does not exist anywhere in the binary file !** .

**offset**: 40 bytes to reach RIP.

1. **target writeable memory (`.data` section ):**
 using `pwntools` we can locates the address of the [.data section] which is writable and maintains a static address. 
2. **useful gadgets**:
   1. `pop r14 ; pop r15 ; ret` : we use it to load the target memory address into r14 register and the 8-byte chunk of the string (`"flag.txt"`) into `r15`. (Note: Address for standard pop gadgets are dynamically extracted in the exploit script via `pwntools.ROP` + in x86-64 architecture, general-purpose registers like `r15` are 64 bits , wich is equals **8 byytes** , the string `flag.txt` has a length of exactly 8 characters (bytes) allowing it to fit perfectly into a singel register in one go ).
   2. `mov [r14], r15; ret ` : we use gadgets at address `0x400628` to moves data (the string (`"flag.txt"`)) from a register r15 into a memory location (.data section address) in register r14. 
   3. `pop rdi ; ret` : we use it to pass the pointer of our written string (`.data ` address ) as a first arg of `print_file` function.
   4. `ret` : used for 16-bytes stack alignment before calling print_file function to prevent segmentation fault (SIGSEGV) .
3. **payload structure :**
   the final rop chain follow this repetitive sequence :
   [Padding (40-bytes)] -> [pop r14 ; pop r15 ; ret] -> [ r14 :target memory address(.data)] -> [r15 : "flag.txt"] -> [mov [r14], r15 ; ret ] -> [ret] -> [pop rdi ; ret ] -> [rdi : target memory address(.data)] -> [print_file].
4. **Usage**
Run the exploit script using python3 (pwntools)
```bash
python exploit.py
