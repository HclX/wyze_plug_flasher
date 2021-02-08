#!/bin/python3

import struct
import sys
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument(
    '--ssid',
    help='WIFI SSID to connect')
parser.add_argument(
    '--password', default='',
    help="WIFI password")

parser.add_argument(
    '--ota_url', default='',
    help="OTA URL")

parser.add_argument(
    '--in', dest='in_file',
    help="Input firmware")

parser.add_argument(
    '--out', dest='out_file',
    help="Output firmware"
)
args = parser.parse_args()


def xor_checksum(s):
    cs = 0
    for x in s:
        cs = cs ^ x
    return cs

TAG = "__SYS_CONFIG_TAG__"

config_template = TAG.ljust(0xFF, '\x00').encode('ascii')
checksum = xor_checksum(config_template)
print("checksum= %02X" % checksum)

config_real = ''.join([x.ljust(y, '\x00') for x, y in zip([TAG, args.ssid, args.password, args.ota_url], [32, 32, 64, 127])]).encode('ascii')
checksum = xor_checksum(config_real)
config_real += bytes([checksum])
print("checksum= %02X" % checksum)

print("Real config:")
print(config_real)

firmware = open(args.in_file, 'rb').read()
index = firmware.find(TAG.encode('ascii'))
if index >= 0:
    print("config tag found at offset 0x%08X" % index)
    firmware = firmware[:index] + config_real + firmware[index + len(config_real):]
    open(args.out_file, 'wb').write(firmware)
else:
    print("config tag not found!")
