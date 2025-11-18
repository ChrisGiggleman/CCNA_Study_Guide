# CCNA Subnetting Quick Reference (IPv4 & IPv6)

> Built for **speed on exams** – minimal formulas, maximum pattern recognition.

---

## 1. Core IPv4 Subnetting Concepts

### 1.1 Powers of 2 You MUST Know

These cover almost all CCNA questions:

| Bits for Hosts | # Hosts | Typical Prefix |
|----------------|---------|----------------|
| 2              | 4       | /30            |
| 3              | 8       | /29            |
| 4              | 16      | /28            |
| 5              | 32      | /27            |
| 6              | 64      | /26            |
| 7              | 128     | /25            |
| 8              | 256     | /24            |
| 9              | 512     | /23            |
| 10             | 1024    | /22            |

**Formula (conceptual):**

- Hosts per subnet (usable) ≈ `2^(32 − prefix) − 2`
- But in the exam, you should **recognize the common ones** from the table.

---

### 1.2 Block Size Trick (FAST)

**Block size** = `256 − subnet_mask_octet`

Example:  
- `/29` → mask = 255.255.255.248 → `256 − 248 = 8` → block size = **8**
- `/28` → mask = 255.255.255.240 → block size = **16**
- `/26` → mask = 255.255.255.192 → block size = **64**

You use this to find:
- Network address
- Broadcast address
- Valid host range
- Which answer choice is correct

---

### 1.3 3-Step Method to Find the Network (IPv4)

Given an IP and prefix, e.g. `10.10.13.155/28`:

1. **Find the “interesting” octet**  
   - /25–/32 → 4th octet  
   - /17–/24 → 3rd octet  
   - /9–/16 → 2nd octet  

   `/28` → interesting octet = **4th** (`155`).

2. **Calculate block size**  
   - `/28` → mask 255.255.255.240 → `256 − 240 = 16`  
   - Block size = **16**

3. **Find the block the IP belongs to**  
   - List multiples of 16 up to 255: 0,16,32,48,64,80,96,112,128,144,160,176,192,208,224,240  
   - The largest multiple **≤ 155** is **144**

**Result:**

- Network: `10.10.13.144/28`
- Broadcast: `10.10.13.159`
- Host range: `10.10.13.145 – 10.10.13.158`

> Exam pattern: most “Which prefix does Router1 use for traffic to Host A?” are exactly this.

---

### 1.4 Quickly Choosing the Right Prefix for X Hosts

**Steps:**

1. Take required hosts (e.g. 50).
2. Add 2 (network + broadcast) → 52.
3. Find **next power of 2 ≥ that number**.
4. Subtract host bits from 32 → prefix.

Examples:

- Need **6 hosts**  
  - 6 + 2 = 8 → 8 is 2³ → host bits = 3 → prefix = 32 − 3 = **/29**

- Need **50 hosts**  
  - 50 + 2 = 52 → next power of 2 = 64 = 2⁶ → prefix = 32 − 6 = **/26**

- Need **200 hosts**  
  - 200 + 2 = 202 → next power of 2 = 256 = 2⁸ → prefix = 32 − 8 = **/24**

---

### 1.5 Quickly Finding # of Subnets

Given an original prefix and a new (longer) prefix:

- `# subnets = 2^(new_prefix − old_prefix)`

Example:  
From a /16, you subnet into /24s:  
- New_prefix − old_prefix = 24 − 16 = 8  
- `2^8 = 256` subnets of size /24.

---

### 1.6 “Instant Recognition” Table (IPv4 /24 and Smaller)

Very handy for CCNA:

| Prefix | Mask              | Hosts | Block Size (last octet) | Network Increments |
|--------|-------------------|-------|--------------------------|--------------------|
| /24    | 255.255.255.0     | 254   | 256 / 1 = 256 → 1       | 0–255 (normal)     |
| /25    | 255.255.255.128   | 126   | 128                      | 0, 128             |
| /26    | 255.255.255.192   | 62    | 64                       | 0,64,128,192       |
| /27    | 255.255.255.224   | 30    | 32                       | 0,32,64,96,...     |
| /28    | 255.255.255.240   | 14    | 16                       | 0,16,32,...,240    |
| /29    | 255.255.255.248   | 6     | 8                        | 0,8,16,...,248     |
| /30    | 255.255.255.252   | 2     | 4                        | 0,4,8,...,252      |

---

## 2. IPv6 Subnetting – MUCH Easier

### 2.1 Massive Key Idea

- typical LAN prefix: **/64**
- subnetting is done **above /64**, usually from /48, /56, or /60
- no “host” math like IPv4; just change the **subnet part**.

General structure:  
`Global :: Subnet :: Interface`

Example:  
`2001:DB8:ACAD:0010::/64`

- `2001:DB8:ACAD` = global routing prefix (/48)
- `0010` = subnet ID (within /64)
- `::` = interface ID zeroed

---

### 2.2 Common IPv6 Prefixes

| Prefix | Use Case                            |
|--------|-------------------------------------|
| /32    | ISP allocation                      |
| /48    | Site / Organization (large)         |
| /56    | Small site / customer               |
| /60    | Even smaller customer subnet block  |
| /64    | Single LAN / VLAN                   |

---

### 2.3 Simple IPv6 Subnetting Example

Given: `2001:DB8:ACAD::/56`

- /56 means:  
  - first 56 bits fixed
  - we have **8 bits** for subnetting before /64
  - that’s **256 subnets**, each /64.
- So subnets look like:

- `2001:DB8:ACAD:00::/64`
- `2001:DB8:ACAD:01::/64`
- `2001:DB8:ACAD:02::/64`
- ...
- `2001:DB8:ACAD:FF::/64`

To find which /64 subnet an address belongs to:
1. Identify the /56 block (first 3.5 hextets).
2. Look at the high-order part of the 4th hextet.
3. Zero out bits below /64 to get subnet ID.

---

## 3. ONE-PAGE QUICK SUBNETTING REFERENCE (Print This)

### IPv4 – Core Tricks

1. **Block size**: `256 − mask_octet`
2. **Network address**:  
   - Focus on interesting octet  
   - `network_octet = (ip_octet // block) * block`
3. **Broadcast** = `network_octet + block − 1` (in that octet, rest 255s)
4. **Usable hosts**: roughly `2^(32 − prefix) − 2`
5. **Prefix for X hosts**:
   - `hosts_needed + 2 → next power of 2 → 32 − power = prefix`
6. **# of subnets** from old → new:
   - `2^(new_prefix − old_prefix)`

**Memorize this mini table:**

| Hosts Needed | Prefix |
|--------------|--------|
| 2            | /30    |
| 6            | /29    |
| 14           | /28    |
| 30           | /27    |
| 62           | /26    |
| 126          | /25    |
| 254          | /24    |

---

### IPv6 – Core Tricks

1. Most LANs use **/64**.
2. Subnetting is done above /64:
   - /48 → /64 = 16 bits of subnetting (65,536 subnets)
   - /56 → /64 = 8 bits of subnetting (256 subnets)
3. To find the subnet:
   - Keep bits up to the prefix
   - Zero out the rest
4. To list subnets:
   - Just increment the subnet hextet or nibble.

---

## 4. Practice (Sample CCNA-Style IPv4 Questions)

1. You need at least **50 hosts** on a subnet. Which prefix should you use?  
   → /26

2. Network 192.168.10.0/27. What is the **4th subnet’s** network address?  
   - Block = 32  
   - Subnets: .0, .32, .64, .96  
   → 192.168.10.96/27

3. Host 10.10.13.155/28 is in which network?  
   - Block = 16  
   - 16 multiples: 0,16,32,48,64,80,96,112,128,144,160…  
   - 144 ≤ 155 < 160  
   → Network = 10.10.13.144/28

4. From 172.16.0.0/16, you create /24 subnets. How many subnets do you get?  
   - 24−16 = 8 bits → 2⁸ = **256 subnets**.

---

## 5. Practice (Sample IPv6 Questions)

1. Given `2001:DB8:CAFE::/56`, how many /64 subnets can you create?  
   - 64 − 56 = 8 bits → 2⁸ = **256 /64 subnets**.

2. Which /64 subnet does `2001:DB8:CAFE:00AB::1` belong to if the site prefix is /56?  
   - `/56` = `2001:DB8:CAFE:00AB::/64` (keep first 56 bits, zero host).

---
