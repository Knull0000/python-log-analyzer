ip_count = {}

with open("bf.log") as log:

    for line in log:

        if "Failed password" in line:

            ip = line.split()[-4]

            if ip not in ip_count:
                ip_count[ip] = 1
            else:
                ip_count[ip] += 1


print("Analyzing log...\n")

for ip in ip_count:

    print(f"IP {ip} failed login {ip_count[ip]} times")

    if ip_count[ip] >= 3:
        print(" Possible brute force attack\n")