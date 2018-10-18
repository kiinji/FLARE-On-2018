import sys
import os
import json
import subprocess
from ctypes import c_uint8, c_uint16, c_uint32, c_uint64, c_int32
import itertools
import pexpect

key_map_147 = {0x35c7e2: 32, 0x5704e7: 33, 0x8cccc9: 34, 0xe3d1b0: 35, 0x1709e79: 36, 0x2547029: 37, 0x3c50ea2: 38, 0x6197ecb: 39, 0x9de8d6d: 40, 0xff80c38: 41, 0x19d699a5: 42, 0x29cea5dd: 43, 0x43a53f82: 44, 0x6d73e55f: 45, 0xb11924e1: 46, 0x11e8d0a40: 47, 0x1cfa62f21: 48, 0x2ee333961: 49, 0x4bdd96882: 50, 0x7ac0ca1e3: 51, 0xc69e60a65: 52, 0x1415f2ac48: 53, 0x207fd8b6ad: 54, 0x3495cb62f5: 55, 0x5515a419a2: 56, 0x89ab6f7c97: 57, 0xdec1139639: 58, 0x1686c8312d0: 59, 0x2472d96a909: 60, 0x3af9a19bbd9: 61, 0x5f6c7b064e2: 62, 0x9a661ca20bb: 63, 0xf9d297a859d: 64, 0x19438b44a658: 65, 0x28e0b4bf2bf5: 66, 0x42244003d24d: 67, 0x6b04f4c2fe42: 68, 0xad2934c6d08f: 69, 0x1182e2989ced1: 70, 0x1c5575e509f60: 71, 0x2dd8587da6e31: 72, 0x4a2dce62b0d91: 73, 0x780626e057bc2: 74, 0xc233f54308953: 75, 0x13a3a1c2360515: 76, 0x1fc6e116668e68: 77, 0x336a82d89c937d: 78, 0x533163ef0321e5: 79, 0x869be6c79fb562: 80, 0xd9cd4ab6a2d747: 81, 0x16069317e428ca9: 82, 0x23a367c34e563f0: 83, 0x39a9fadb327f099: 84, 0x5d4d629e80d5489: 85, 0x96f75d79b354522: 86, 0xf444c01834299ab: 87, 0x18b3c1d91e77decd: 88, 0x27f80ddaa1ba7878: 89, 0x40abcfb3c0325745: 90, 0x68a3dd8e61eccfbd: 91, 0xa94fad42221f2702: 92, 0x11f38ad0840bf6bf: 93, 0xbb433812a62b1dc1: 94, 0xcd36c2e32a371480: 95, 0x8879faf5d0623241: 96, 0x55b0bdd8fa9946c1: 97, 0xde2ab8cecafb7902: 98, 0x33db76a7c594bfc3: 99, 0x12062f76909038c5: 100, 0x45e1a61e5624f888: 101, 0x57e7d594e6b5314d: 102, 0x9dc97bb33cda29d5: 103, 0xf5b15148238f5b22: 104, 0x937accfb606984f7: 105, 0x892c1e4383f8e019: 106, 0x1ca6eb3ee4626510: 107, 0xa5d30982685b4529: 108, 0xc279f4c14cbdaa39: 109, 0x684cfe43b518ef62: 110, 0x2ac6f30501d6999b: 111, 0x9313f148b6ef88fd: 112, 0xbddae44db8c62298: 113, 0x50eed5966fb5ab95: 114, 0xec9b9e4287bce2d: 115, 0x5fb88f7a983179c2: 116, 0x6e82495ec0ad47ef: 117, 0xce3ad8d958dec1b1: 118, 0x3cbd2238198c09a0: 119, 0xaf7fb11726acb51: 120, 0x47b51d498bf6d4f1: 121, 0x52ad185afe61a042: 122, 0x9a6235a48a587533: 123, 0xed0f4dff88ba1575: 124, 0x877183a413128aa8: 125, 0x7480d1a39bcca01d: 126}

key_map_b3 = {}
key_map_326 = {}

def checksum_2fe(encoded):
    buff = [0xDC ,0x48 ,0x8F ,0x56 ,0xBC ,0x36 ,0xB0 ,0x64 ,0x40 ,0x27 ,0xE6 ,0x2C ,0xD2 ,0x3F ,0xC2 ,0x34 ,0x5D ,0x52 ,0xEE ,0xCD ,0xAA ,0xCA ,0x81 ,0x8D ,0x71 ,0x23 ,0x28 ,0xD7 ,0x96 ,0x4E ,0x7F ,0x6B ,0xA1 ,0x3E ,0xA3 ,0x12 ,0x91 ,0x26 ,0xE4 ,0x03 ,0x60 ,0x8C ,0x01 ,0x44 ,0x79 ,0xE3 ,0x84 ,0x35 ,0xB8 ,0x4A ,0xC1 ,0x55 ,0x1A ,0x9D ,0x11 ,0xE7 ,0x92 ,0xA4 ,0xD4 ,0x68 ,0x37 ,0x85 ,0x62 ,0x66 ,0xFC ,0xBF ,0xD8 ,0x98 ,0x9A ,0x8E ,0x32 ,0x20 ,0x16 ,0x38 ,0x57 ,0x0E ,0x18 ,0x5B ,0xF4 ,0x17 ,0x1E ,0xA0 ,0xDD ,0x53 ,0x5F ,0x06 ,0xF8 ,0xF6 ,0xE1 ,0x0C ,0x02 ,0x74 ,0xF3 ,0xC0 ,0xC3 ,0xF0 ,0x3C ,0x94 ,0x10 ,0xDB ,0x04 ,0xF9 ,0x08 ,0xD6 ,0x1F ,0xBE ,0xEF ,0x95 ,0xE5 ,0x50 ,0xB6 ,0xAB ,0x5A ,0x19 ,0xAD ,0x24 ,0x99 ,0x43 ,0xCB ,0xA5 ,0xEB ,0x39 ,0xCC ,0x67 ,0xB9 ,0xC5 ,0xC9 ,0xA6 ,0x6A ,0x90 ,0x7A ,0x0F ,0xD9 ,0x3B ,0x1C ,0xE8 ,0xA8 ,0x7E ,0xC4 ,0x72 ,0x8B ,0x63 ,0x1B ,0x59 ,0x07 ,0x49 ,0xAE ,0x05 ,0xA9 ,0xEC ,0x00 ,0xC6 ,0x31 ,0x14 ,0x69 ,0xBA ,0x82 ,0x1D ,0x65 ,0x46 ,0x70 ,0x29 ,0xAF ,0xC8 ,0xDE ,0xD0 ,0xFD ,0x77 ,0x73 ,0x2B ,0x6D ,0xDF ,0x6C ,0xFE ,0x30 ,0x2F ,0xF1 ,0x78 ,0x21 ,0x7C ,0x4D ,0xCE ,0x13 ,0xB5 ,0x97 ,0x2A ,0x9E ,0xFF ,0xEA ,0xCF ,0x25 ,0xBD ,0xAC ,0x4C ,0x0D ,0x80 ,0xE9 ,0xB2 ,0x4B ,0xFA ,0x54 ,0x41 ,0x89 ,0x3A ,0x51 ,0xF7 ,0x00 ,0x8A ,0x2D ,0xDA ,0x33 ,0xF2 ,0x22 ,0x9B ,0xD5 ,0xA2 ,0x45 ,0x6E ,0x4F ,0xD3 ,0x76 ,0x3D ,0x86 ,0x2E ,0xBB ,0x7B ,0x0A ,0x42 ,0xB1 ,0x5E ,0xED ,0x9C ,0xE0 ,0x88 ,0x7D ,0x15 ,0x93 ,0xD1 ,0x83 ,0x6F ,0xFB ,0xB4 ,0x9F ,0x47 ,0x09 ,0xA7 ,0x87 ,0xF5 ,0x61 ,0xE2 ,0xC7 ,0xB3 ,0x75 ,0x0B ,0x58 ,0x5C, 0x14, 0x00, 0x00, 0x00]
    
    v11 = 0
    v12 = 0
    v13 = 0
    
    decode_key = []
    for i in range(0, 10):
        v12 += 1
        v12 = v12 % 256
        v11 += buff[v12]
        v11 = v11 % 256
        buff[v12] ^= buff[v11]
        buff[v11] ^= buff[v12]
        buff[v12] ^= buff[v11]
        
        v13 = buff[v12] + buff[v11]
        v13 = v13 % 256
        decode_key.append(buff[v13])
        
    answer = []
    for i in range(0, len(encoded)):
        answer.append(encoded[i] ^ decode_key[i])
    
    return answer
   
def get_magic_pid():
    return subprocess.check_output(['pgrep', 'magic']).decode('utf-8').strip()

def get_magic_mem():
    os.chdir('dumps')
    magic_pid = get_magic_pid()
    subprocess.run('rm -rf *.dump', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.run('./dumper.sh {}'.format(magic_pid), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    b = open('{}-00605000-00618000.dump'.format(magic_pid), 'rb').read()[0x100 : 0x2620]
    os.chdir('..')
    return b

def get_local_magic():
    return open('magic_buffer_2.bin', 'rb').read()

def get_current_key():
    bin = get_magic_mem()
    count = 0

    # bin = open('6/magic_buffer_2.bin', 'rb').read()
    # count = 0

    key = {}

    while True:
        key_pos_offset = (count * 0x120) + 0xC
        key_len_offset = (count * 0x120) + 0x10
        key_chk_offset = (count * 0x120) + 0x20
        key_fnlen_offset = (count * 0x120) + 0x08
        
        if key_pos_offset >= len(bin):
            break
            
        key_pos = int.from_bytes(bin[key_pos_offset : key_pos_offset + 1], 'little')
        key_len = int.from_bytes(bin[key_len_offset : key_len_offset + 1], 'little')
        key_fnlen = int.from_bytes(bin[key_fnlen_offset : key_fnlen_offset + 2], 'little')
        
        if key_fnlen == 0x147:
            for i in range(0, key_len):
                checksum = int.from_bytes(bin[key_chk_offset : key_chk_offset + 8], 'little')
                if checksum not in key_map_147:
                    print("key_chk_offset:", hex(key_chk_offset))
                    break
                charcode = key_map_147[checksum]
                
                key[key_pos + i] = chr(charcode)
                key_chk_offset += 8

        elif key_fnlen == 0x326:
            crypt = bin[key_chk_offset : key_chk_offset + key_len + 2]
            crypt = '0x' + ''.join([hex(b)[2:] for b in crypt]) + '0'
            
            if key_map_326 == {}:
                _ = open('keymap_326.json', 'r').read()
                key_map_326.update(json.loads(_))

            actual_key = key_map_326[crypt]
            for i in range(0, key_len):
                key[key_pos + i] = list(actual_key)[i]

        elif key_fnlen == 0xB3:
            crypt = bin[key_chk_offset : key_chk_offset + 4]

            crypt = int.from_bytes(crypt, byteorder='little', signed=False)
            crypt = hex(crypt)
            if key_map_b3 == {}:
                _ = open('keymap_b3_1.json', 'r').read()
                key_map_b3.update(json.loads(_))
                _ = open('keymap_b3_2.json', 'r').read()
                key_map_b3.update(json.loads(_))
                _ = open('keymap_b3_3.json', 'r').read()
                key_map_b3.update(json.loads(_))

            actual_key = key_map_b3[crypt]

            for i in range(0, key_len):
                key[key_pos + i] = list(actual_key)[i]
        
        elif key_fnlen == 0x2FE:
            encoded = bin[key_chk_offset : key_chk_offset + key_len]
            clear = checksum_2fe(encoded)
            for i in range(0, key_len):
                key[key_pos + i] = chr(clear[i])
            
        elif key_fnlen == 0x326:
            if key_pos == 0x3f:
                key[key_pos] = ' '
            if key_pos == 0x32:
                key[key_pos] = ' '
                key[key_pos + 1] = 'y'
                key[key_pos + 2] = 'o'
                
        elif key_fnlen == 0x8F:
            encoded = bin[key_chk_offset : key_chk_offset + key_len]
            for i, v in enumerate(encoded):
                key[key_pos + i] = chr(v - 13)
            
        elif key_fnlen == 0x7C:
            encoded = bin[key_chk_offset : key_chk_offset + key_len]
            for i, v in enumerate(encoded):
                key[key_pos + i] = chr(v)

        elif key_fnlen == 0x84:
            encoded = bin[key_chk_offset : key_chk_offset + key_len]
            for i, v in enumerate(encoded):
                key[key_pos + i] = chr(v ^ 0x2A)

        else:
            # print(hex(key_fnlen), 'not implemented')
            pass
            
        count += 1

    key_str = ['_' for b in range(0, 69)]
    for i in range(0, 100):
        if i in key:
            key_str[i] = key[i]        
    return ''.join(key_str)
    
proc = pexpect.spawn('./pure/magic')

while True:
    proc.expect('Enter key:')
    key = get_current_key()
    print('##> sending key:', key)

    proc.sendline(key)

    print(proc.before.decode('utf-8'))
    print(proc.after.decode('utf-8'))

# mag!iC_mUshr00ms_maY_h4ve_g!ven_uS_Santa_ClaUs@flare-on.com

exit()
