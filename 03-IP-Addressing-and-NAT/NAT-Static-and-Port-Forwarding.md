# Static NAT and Port Forwarding

## Static NAT

Static NAT creates a **permanent 1:1 mapping** between one inside local and one inside global address.

### Use Cases

- Internal servers that must always be reachable from the Internet:
  - Web server, mail server, VPN gateway, etc.
- When you need a **fixed public IP** for an inside host.

### Key Properties

- Mapping is **always present**.
- Allows sessions **initiated from outside** to reach inside hosts.
- Uses **one public address per mapped host** (not address-efficient).

### Example Flow

- PC1 (inside local): `192.168.10.10`
- Static mapping: `192.168.10.10` ↔ `209.165.200.226` (inside global)
- Server SRV1 (outside global): `209.165.201.1`

Steps:

1. PC1 sends packet to `209.165.201.1` (source `192.168.10.10`).
2. NAT device sees `192.168.10.10` and translates source to `209.165.200.226`.
3. SRV1 responds to `209.165.200.226`.
4. NAT device translates destination back to `192.168.10.10`.

Static mapping lives in the NAT table whether or not traffic is flowing.

---

## Static NAT – IOS Configuration Example

```bash
! Mark inside / outside interfaces
R1(config)# interface g0/0
R1(config-if)# ip address 192.168.10.1 255.255.255.0
R1(config-if)# ip nat inside
R1(config-if)# exit

R1(config)# interface g0/1
R1(config-if)# ip address 209.165.200.225 255.255.255.248
R1(config-if)# ip nat outside
R1(config-if)# exit

! Static inside NAT mapping
R1(config)# ip nat inside source static 192.168.10.10 209.165.200.226
