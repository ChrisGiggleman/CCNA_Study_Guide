# 02 – Network Access

Quick reminders for switching topics:

## VLANs

- Separate L2 broadcast domains.
- Tagging: **802.1Q** (native VLAN untagged).
- Access port = 1 VLAN, Trunk = multiple VLANs.

## STP (Overview – detailed security in 04 folder)

- Purpose: prevent L2 loops.
- Root Bridge = lowest Bridge ID (priority + MAC).
- Port roles: Root, Designated, Alternate/Blocking.
- Common variants: STP, RSTP, PVST+, Rapid-PVST+.

## EtherChannel (Port-Channel)

- Bundle multiple physical links into one logical.
- Protocols: **PAgP** (Cisco), **LACP** (standard).
- All member links must share:
  - Speed, duplex, VLAN membership, trunk settings.

You’ll see more **security-focused STP content** in:
`../04-L2-Security-DHCP-ARP-STP/`
