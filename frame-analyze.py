statmenthex = input("[+] Enter hexdeicaml : ").strip()
frame_dest = statmenthex[0:12]
frame_source = statmenthex[12:24]
type1 = statmenthex[24:28]
version = statmenthex[28]
headerLength = statmenthex[29]
totalLength = statmenthex[32:36] 
decimal_val = int(totalLength, 16)
header_bytes = int(headerLength, 16) * 4
print("[+] Destination Mac :", frame_dest)
print("[+] Source Mac :", frame_source)
if type1 == "0800":
  print("[+] Type : IPv4")
else:
  print("[-] Type EtherType:", type1)
if version == "4":
  print("[+] Version : IPv4")
elif version == "6":
  print("[+] Version : IPv6")
else:
  print(f"[+] Unknown version: {version}")
print(f"[+] Header Length : {header_bytes} Bytes")
print(f"[+] Total length : {decimal_val} Bytes")
print(f"[+] Data length : {decimal_val - header_bytes} Bytes")
