import ipaddress
import random
import math
import sys

BANNER = r"""
===========================================
   CCNA Subnetting Trainer (IPv4 / IPv6)
===========================================
"""

def ask_ipv4_hosts_to_prefix():
    # random host requirement in a realistic CCNA range
    candidates = [2, 6, 14, 30, 50, 100, 200, 500]
    hosts_needed = random.choice(candidates)
    print(f"\n[IPv4] You need at least {hosts_needed} usable hosts.")
    answer = input("What prefix length (e.g., /26) should you use? ").strip()

    required = hosts_needed + 2  # include network + broadcast
    power = math.ceil(math.log2(required))
    prefix = 32 - power
    correct = f"/{prefix}"

    if answer == correct:
        print("✅ Correct!")
    else:
        print(f"❌ Not quite. Correct answer: {correct}")
    explain = input("Type 'e' for explanation or Enter to continue: ").strip().lower()
    if explain == 'e':
        print(f"- Hosts needed = {hosts_needed}")
        print(f"- Add 2 (network + broadcast): {required}")
        print(f"- Next power of 2 ≥ {required} is 2^{power}")
        print(f"- Host bits = {power}, so prefix = 32 - {power} = {prefix}")
        print(f"→ Use {correct}")

def generate_random_ipv4_prefix():
    # focus on /24 - /30 range, common on CCNA
    return random.choice([24, 25, 26, 27, 28, 29, 30])

def ask_ipv4_network_for_ip():
    prefix = generate_random_ipv4_prefix()
    # build random network in private ranges
    base_networks = ["10.0.0.0", "172.16.0.0", "192.168.0.0"]
    base = random.choice(base_networks)
    net = ipaddress.IPv4Network(f"{base}/{prefix}", strict=False)
    # pick random host inside that /prefix network
    host = random.choice(list(net.hosts()))
    question_prefix = random.choice([prefix, prefix + random.choice([0, 1])])
    if question_prefix > 30:
        question_prefix = prefix

    print(f"\n[IPv4] Which network does this host belong to?")
    print(f"Host IP: {host} /{question_prefix}")
    answer = input("Enter network address with prefix (e.g., 192.168.1.0/26): ").strip()

    question_net = ipaddress.IPv4Network(f"{host}/{question_prefix}", strict=False)
    correct = f"{question_net.network_address}/{question_prefix}"

    if answer == correct:
        print("✅ Correct!")
    else:
        print(f"❌ Not quite. Correct answer: {correct}")
    explain = input("Type 'e' for explanation or Enter to continue: ").strip().lower()
    if explain == 'e':
        host_octets = str(host).split(".")
        net_octets = str(question_net.netmask).split(".")
        print(f"- Subnet mask: {question_net.netmask}")
        print("- Identify the interesting octet: the one not 255 or 0.")
        for i, (h, m) in enumerate(zip(host_octets, net_octets)):
            print(f"  Octet {i+1}: host={h}, mask={m}")
        print(f"- Network address is calculated by ANDing each octet or using block size trick.")
        print(f"- Final network: {correct}")

def ask_ipv4_subnet_count():
    old_prefix = random.choice([8, 16])
    new_prefix = random.choice([24, 25, 26])
    while new_prefix <= old_prefix:
        new_prefix = random.choice([24, 25, 26])

    print(f"\n[IPv4] You have a /{old_prefix} and create /{new_prefix} subnets.")
    answer = input("How many subnets do you get? ").strip()

    diff = new_prefix - old_prefix
    correct = 2 ** diff

    try:
        user_val = int(answer)
        if user_val == correct:
            print("✅ Correct!")
        else:
            print(f"❌ Not quite. Correct answer: {correct}")
    except ValueError:
        print(f"❌ Please enter a number. Correct answer: {correct}")

    explain = input("Type 'e' for explanation or Enter to continue: ").strip().lower()
    if explain == 'e':
        print(f"- New prefix - old prefix = {new_prefix} - {old_prefix} = {diff}")
        print(f"- Number of subnets = 2^{diff} = {correct}")

def ask_ipv6_subnetting():
    # Simple /48 or /56 questions
    base = "2001:db8:acad::"
    site_prefix = random.choice([48, 56])
    lan_prefix = 64
    bits = lan_prefix - site_prefix
    total_subnets = 2 ** bits

    print(f"\n[IPv6] You are given a {base}/{site_prefix} site prefix.")
    print(f"You want to create /64 LANs from it.")
    q_type = random.choice(["count", "identify"])

    if q_type == "count":
        answer = input("How many /64 subnets can you create? ").strip()
        try:
            user_val = int(answer)
            if user_val == total_subnets:
                print("✅ Correct!")
            else:
                print(f"❌ Not quite. Correct answer: {total_subnets}")
        except ValueError:
            print(f"❌ Please enter a number. Correct answer: {total_subnets}")

        explain = input("Type 'e' for explanation or Enter to continue: ").strip().lower()
        if explain == 'e':
            print(f"- Site prefix: /{site_prefix}, LAN prefix: /64")
            print(f"- Subnet bits = 64 - {site_prefix} = {bits}")
            print(f"- Number of subnets = 2^{bits} = {total_subnets}")
    else:
        # identify subnet: pick a random /64 within the site
        subnet_id = random.randint(0, total_subnets - 1)
        # express subnet_id as 2-hex-digit or 4-hex-digit depending on /56 or /48
        if site_prefix == 56:
            # varies in 4th hextet low byte
            hextet = f"{subnet_id:02x}"
            example = f"2001:db8:acad:{hextet}::1/{lan_prefix}"
            print(f"Example host: {example}")
            answer = input("What is the /64 network (e.g., 2001:db8:acad:xx::/64)? ").strip()
            correct = f"2001:db8:acad:{hextet}::/{lan_prefix}"
        else:
            # site_prefix == 48 → subnet spans full 4th hextet
            hextet = f"{subnet_id:04x}"
            example = f"2001:db8:acad:{hextet}::1/{lan_prefix}"
            print(f"Example host: {example}")
            answer = input("What is the /64 network (e.g., 2001:db8:acad:xxxx::/64)? ").strip()
            correct = f"2001:db8:acad:{hextet}::/{lan_prefix}"

        if answer.lower() == correct.lower():
            print("✅ Correct!")
        else:
            print(f"❌ Not quite. Correct answer: {correct}")

        explain = input("Type 'e' for explanation or Enter to continue: ").strip().lower()
        if explain == 'e':
            print(f"- Site prefix /{site_prefix} stays fixed.")
            print(f"- /64 means remaining bits select the subnet ID.")
            print(f"- We zero the interface ID and keep the subnet ID in the 4th hextet.")
            print(f"→ Result: {correct}")

def main_menu():
    print(BANNER)
    print("Choose a practice mode:")
    print(" 1) IPv4 – Hosts → Prefix")
    print(" 2) IPv4 – Find Network for Host")
    print(" 3) IPv4 – Subnet Count (old/new prefix)")
    print(" 4) IPv6 – Simple Subnetting (/48 or /56 to /64)")
    print(" 5) Mixed Random Question")
    print(" 0) Quit")

def ask_mixed():
    funcs = [
        ask_ipv4_hosts_to_prefix,
        ask_ipv4_network_for_ip,
        ask_ipv4_subnet_count,
        ask_ipv6_subnetting,
    ]
    random.choice(funcs)()

def main():
    while True:
        main_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == '1':
            ask_ipv4_hosts_to_prefix()
        elif choice == '2':
            ask_ipv4_network_for_ip()
        elif choice == '3':
            ask_ipv4_subnet_count()
        elif choice == '4':
            ask_ipv6_subnetting()
        elif choice == '5':
            ask_mixed()
        elif choice == '0':
            print("Good luck on your CCNA – may your subnets always align. 😈")
            sys.exit(0)
        else:
            print("Please choose a valid option (0–5).")

        input("\nPress Enter for menu...")

if __name__ == "__main__":
    main()
