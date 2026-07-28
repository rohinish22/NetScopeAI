import socket
import dns.resolver
import time

# Project Header
print("=" * 50)
print("        NetScope AI - DNS Analyzer")
print("=" * 50)

# Get website from user
website = input("Enter Website (Example: amazon.com): ")

try:
    # Start timer
    start = time.time()

    # Get IPv4 Address
    ipv4 = socket.gethostbyname(website)

    # Stop timer
    end = time.time()

    # Display DNS Report
    print("\n" + "=" * 20 + " DNS REPORT " + "=" * 20)
    print(f"Website      : {website}")
    print(f"IPv4 Address : {ipv4}")
    print(f"Lookup Time  : {(end-start)*1000:.2f} ms")

    # Get MX Records
    print("\nMX Records:")
    try:
        answers = dns.resolver.resolve(website, "MX")

        for record in answers:
            print(f" • {record}")

    except dns.resolver.NoAnswer:
        print("No MX records found.")

    except dns.resolver.NXDOMAIN:
        print("Domain does not exist.")

    except Exception:
        print("Unable to retrieve MX records.")

except socket.gaierror:
    print("\n Invalid domain name or unable to resolve DNS.")

except Exception as e:
    print("\nUnexpected Error:", e)