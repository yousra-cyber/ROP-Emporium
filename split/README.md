# ROP Emporium - split (x86-64)
##solution overview
1. **Offset:** 40 bytes (found using `cyclic` and `corefile` , it's in comment part!)
2. **Gadgets**:
   - `pop rdi ; ret ` : to pass the flag string address to `rdi `
   - `ret`  for stack alignment.
3. **target adreess:** `system@plt` and `flag` string at `0x601060`.
## EXploit script 
check `exploit.py` for the full exploit code.
