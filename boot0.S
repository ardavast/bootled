PH_CFG0 = 0x01c208fc
PH_DAT  = 0x01c2090c

.globl _start

_start:
    mov    r0, #0x100
    ldr    r1, =PH_CFG0
    str    r0, [r1]        @PH2 = OUTPUT
    mov    r0, #0x4
    ldr    r1, =PH_DAT
    str    r0, [r1]        @PH2 = HIGH
loop:
    b      loop
