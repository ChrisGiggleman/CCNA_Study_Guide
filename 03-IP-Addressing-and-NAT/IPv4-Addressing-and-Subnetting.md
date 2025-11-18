# IPv4 Addressing and Subnetting (Quick Reference)

## Private IPv4 Ranges (RFC 1918)

- **Class A**: 10.0.0.0 – 10.255.255.255 (/8)
- **Class B**: 172.16.0.0 – 172.31.255.255 (/12)
- **Class C**: 192.168.0.0 – 192.168.255.255 (/16)

These addresses are **not routed on the public Internet**. NAT is used to translate them to public addresses.

## Key Subnetting Ideas (for speed on the exam)

- **Network bits + Host bits = 32**
- Number of hosts per subnet:
  - `2^(host bits) – 2`
- Block size for a given prefix:
  - `Block size = 256 – subnet mask octet`
  - Example: /26 → mask 255.255.255.192 → 256 – 192 = 64 → ranges: .0, .64, .128, .192

### Fast Pattern Examples

- /24 → 256 addresses → 254 usable.
- /25 → 128 addresses → 126 usable.
- /26 → 64 addresses → 62 usable.
- /27 → 32 → 30 usable.
- /28 → 16 → 14 usable.
- /29 → 8 → 6 usable.
- /30 → 4 → 2 usable (common in point-to-point WAN links).

## Practice Tips

- Always identify:
  1. **Network ID**
  2. **Broadcast**
  3. **Usable range**
- For CCNA, practice until you can do /24–/30 in your head quickly.
