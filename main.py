from modules import dns_analyzer
from modules import http_analyzer
from modules import ssl_analyzer
from modules import tcp_analyzer
from modules import ai_assistant

while True:

    print("\n" + "=" * 50)
    print("          NetScope AI")
    print("=" * 50)

    print("1. DNS Analyzer")
    print("2. HTTP Analyzer")
    print("3. SSL Analyzer")
    print("4. TCP Analyzer")
    print("5. Full Website Scan")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        dns_analyzer.run()

    elif choice == "2":
        http_analyzer.run()

    elif choice == "3":
        ssl_analyzer.run()

    elif choice == "4":
        tcp_analyzer.run()

    elif choice == "5":

        website = input("\nEnter Website: ")

        dns = dns_analyzer.analyze(website)
        http = http_analyzer.analyze(website)
        ssl = ssl_analyzer.analyze(website)
        tcp = tcp_analyzer.analyze(website)

        report = {}

        report.update(dns)
        report.update(http)
        report.update(ssl)
        report.update(tcp)

        print("\n")
        print("=" * 60)
        print("              WEBSITE REPORT")
        print("=" * 60)

        print("Website :", website)

        if "ip_address" in report:
            print("IP Address :", report["ip_address"])

        if "status_code" in report:
            print("HTTP Status :", report["status_code"])

        if "tls_version" in report:
            print("TLS Version :", report["tls_version"])

        if "port_open" in report:
            print("Port 443 :", "OPEN" if report["port_open"] else "CLOSED")

        ai_assistant.analyze(report)

    elif choice == "6":
        break

    else:
        print("Invalid Choice")