#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct
import sys
from pathlib import Path

if len(sys.argv) < 3:
    raise SystemExit(1)

code_filename, boot0_filename = sys.argv[1:]

code = Path(code_filename).read_bytes()

header_len = 64
code_len = len(code)
boot0_len = (((code_len + header_len) // 512) + 1) * 512
padding_len = boot0_len - code_len - header_len

boot0 = bytearray(
    b'\x0e\x00\x00\xea' +           # b 0x40
    b'eGON.BT0' +                   # magic
    struct.pack('<I', 0x5f0a6c39) + # pre-checksum
    struct.pack('<I', boot0_len) +  # length
    b'\x00' * 44 +                  # header padding
    code +                          # code
    b'\x00' * padding_len           # padding
)

checksum = sum(sum(struct.iter_unpack('<I' , boot0), ())) & 0xffffffff
boot0[12:16] = struct.pack('<I', checksum)

Path(boot0_filename).write_bytes(boot0)
