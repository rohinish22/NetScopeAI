import socket
import time


def analyze(website):

    try:

        ip = socket.gethostbyname(website)

        start = time.time()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.settimeout(3)

        result = sock.connect_ex((website, 443))

        end = time.time()

        sock.close()

        return {

            "ip_address": ip,

            "port_open": result == 0,

            "connection_time": round((end-start)*1000,2)

        }

    except Exception as e:

        return {

            "error": str(e)

        }


def run():

    print("=" * 55)
    print("      NetScope AI - TCP Analyzer")
    print("=" * 55)

    website = input("Enter Website: ")

    result = analyze(website)

    if "error" in result:
        print(result["error"])
        return

    print("\n===== TCP REPORT =====")

    print("IP Address      :", result["ip_address"])
    print("Port 443 Open   :", result["port_open"])
    print("Connection Time :", result["connection_time"], "ms")


if __name__ == "__main__":
    run()