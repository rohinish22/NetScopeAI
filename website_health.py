import socket
import requests
import time

print("=" * 60)
print("        NetScope AI - Website Health Analyzer")
print("=" * 60)

website = input("Enter Website (Example: https://www.google.com): ")

# Remove https:// for DNS lookup
domain = website.replace("https://", "").replace("http://", "").split("/")[0]

print("\nChecking Website...")

# ---------------- DNS ----------------
try:
    dns_start = time.time()

    ip = socket.gethostbyname(domain)

    dns_end = time.time()

    dns_time = (dns_end - dns_start) * 1000

    dns_status = "PASS"

except:
    ip = "Not Found"
    dns_time = 0
    dns_status = "FAIL"

# ---------------- HTTP ----------------
try:
    http_start = time.time()

    response = requests.get(website)

    http_end = time.time()

    http_time = (http_end - http_start) * 1000

    status_code = response.status_code

    server = response.headers.get("Server", "Unknown")

    content_type = response.headers.get("Content-Type", "Unknown")

    http_status = "PASS"

except:
    status_code = "Error"
    server = "Unknown"
    content_type = "Unknown"
    http_time = 0
    http_status = "FAIL"

print("\n" + "=" * 60)
print("DNS")
print("-" * 60)
print(f"Domain          : {domain}")
print(f"IPv4 Address    : {ip}")
print(f"Lookup Time     : {dns_time:.2f} ms")

print("\nHTTP")
print("-" * 60)
print(f"Status Code     : {status_code}")
print(f"Response Time   : {http_time:.2f} ms")
print(f"Server          : {server}")
print(f"Content Type    : {content_type}")

print("\nWebsite Health")
print("-" * 60)
print(f"DNS             : {dns_status}")
print(f"HTTP            : {http_status}")

score = 0

if dns_status == "PASS":
    score += 50

if http_status == "PASS":
    score += 50

print(f"Overall Score   : {score}/100")