# NAT Overview and Terminology

## Why NAT Exists

- IPv4 address space is limited.
- Enterprises use **private addresses (RFC 1918)** internally.
- To reach the Internet, these private IPv4 addresses must be translated to **public IPv4 addresses**.
- NAT is typically implemented on **border devices** (routers or firewalls).

NAT between two IPv4 domains is often called **NAT44** (IPv4 ↔ IPv4).

---

## NAT Address Types (Inside vs Outside, Local vs Global)

From the perspective of the NAT device:

- **Inside**: addresses belonging to the internal network.
- **Outside**: addresses not in the internal network (Internet or another external domain).

Then we add local vs global (what’s seen inside vs outside):

- **Inside Local**  
  - The IP address assigned to an inside host.
  - Usually a private RFC 1918 address (e.g., `192.168.10.10`).

- **Inside Global**  
  - The **translated** address for that inside host.
  - This is the public (or external) IPv4 address that outside hosts see (e.g., `209.165.200.5`).

- **Outside Global**  
  - The IPv4 address assigned to a host on the outside network (e.g., a public web server).
  - Allocated from a globally routable space (e.g., `209.165.201.1`).

- **Outside Local**  
  - The address of an outside host **as it appears to the inside network**.
  - In many inside-only NAT scenarios, outside local = outside global.

### Memory Trick

- **Inside** = internal device.
- **Outside** = external device.
- **Local** = what is visible inside.
- **Global** = what is visible outside.

“Inside global” = internal box seen from the outside.

---

## Where NAT Happens in the Packet Flow

**Inside → Outside (Outbound)**

1. Packet enters **inside interface**.
2. Router **routes** it.
3. NAT translates:
   - Inside local → Inside global.
   - Creates or updates the NAT table entry.
4. Packet exits **outside interface**.

**Outside → Inside (Inbound)**

1. Packet enters **outside interface** with destination = inside global.
2. NAT translates:
   - Inside global → Inside local.
3. Router routes it into the inside network.

If a packet comes from outside with **no matching NAT mapping**, it is **dropped** (especially for dynamic NAT and PAT).

---

## Types of NAT

- **Static NAT** – 1:1 mapping (inside local ↔ inside global).
- **Dynamic NAT** – Many:Many, using a pool of global addresses.
- **PAT (NAPT / NAT Overload)** – Many:1 or Many:Few using:
  - IPv4 address _and_ port translation.
  - Most common in home and small business routers.

Each type is broken down in the next files.
