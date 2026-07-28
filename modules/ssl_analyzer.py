import ssl
import socket
from datetime import datetime


def analyze(website):

    try:

        context = ssl.create_default_context()

        with socket.create_connection((website, 443), timeout=5) as sock:

            with context.wrap_socket(sock, server_hostname=website) as secure_sock:

                cert = secure_sock.getpeercert()

                issuer = dict(x[0] for x in cert["issuer"])

                subject = dict(x[0] for x in cert["subject"])

                expiry = datetime.strptime(
                    cert["notAfter"],
                    "%b %d %H:%M:%S %Y %Z"
                )

                remaining = (expiry - datetime.utcnow()).days

                return {
                    "tls_version": secure_sock.version(),
                    "issuer": issuer.get("organizationName", "Unknown"),
                    "subject": subject.get("commonName", "Unknown"),
                    "days_remaining": remaining
                }

    except Exception as e:

        return {
            "error": str(e)
        }


def run():

    print("=" * 55)
    print("       NetScope AI - SSL Analyzer")
    print("=" * 55)

    website = input("Enter Website: ")

    result = analyze(website)

    if "error" in result:
        print(result["error"])
        return

    print("\n========== SSL REPORT ==========\n")

    print("TLS Version :", result["tls_version"])
    print("Issuer      :", result["issuer"])
    print("Subject     :", result["subject"])
    print("Days Left   :", result["days_remaining"])


if __name__ == "__main__":
    run()