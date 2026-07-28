import socket
import dns.resolver
import time


def analyze(website):
    try:
        start = time.time()

        ip = socket.gethostbyname(website)

        end = time.time()

        mx_records = []

        try:
            answers = dns.resolver.resolve(website, 'MX')
            for record in answers:
                mx_records.append(str(record.exchange))
        except:
            mx_records.append("No MX Records Found")

        return {
            "ip_address": ip,
            "dns_time": (end - start) * 1000,
            "mx_records": mx_records
        }

    except Exception as e:
        return {"error": str(e)}


def run():
    website = input("Enter Website: ")

    result = analyze(website)

    if "error" in result:
        print(result["error"])
        return

    print("\n===== DNS REPORT =====")
    print(f"IP Address : {result['ip_address']}")
    print(f"Lookup Time: {result['dns_time']:.2f} ms")
    print("MX Records:")

    for mx in result["mx_records"]:
        print("-", mx)


if __name__ == "__main__":
    run()