CROSS = arm-none-eabi-
OBJCOPY = objcopy
LDFLAGS = -Ttext 0x40

boot0.bin: boot0-nohdr.bin
	python hdr.py $< $@

boot0-nohdr.bin: boot0
	$(CROSS)$(OBJCOPY) -O binary $< $@

boot0: boot0.o
	$(CROSS)$(LD) $(LDFLAGS) -o $@ $<

boot0.o: boot0.S
	$(CROSS)$(AS) -o $@ $<

.PHONY: clean
clean:
	rm -f boot0.o boot0 boot0-nohdr.bin boot0.bin
