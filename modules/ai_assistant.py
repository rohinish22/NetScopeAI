def analyze(report):

    print("\n" + "=" * 60)
    print("           AI NETWORK ANALYSIS")
    print("=" * 60)

    score = 0

    # ---------------- HTTP ----------------
    status = report.get("status_code")

    print("\nHTTP Analysis")
    print("-" * 30)

    if status == 200:
        print("✔ Website responded successfully.")
        score += 40
    elif status == 301:
        print("✔ Website redirects correctly.")
        score += 35
    elif status == 404:
        print("❌ Page not found.")
    elif status == 500:
        print("❌ Internal Server Error.")
    else:
        print("⚠ Unable to verify HTTP response.")

    # ---------------- TLS ----------------
    tls = report.get("tls_version")

    print("\nTLS Analysis")
    print("-" * 30)

    if tls == "TLSv1.3":
        print("✔ Latest TLS 1.3 is enabled.")
        score += 30

    elif tls == "TLSv1.2":
        print("✔ Secure TLS 1.2 detected.")
        score += 25

    else:
        print("⚠ Older TLS version.")

    # ---------------- TCP ----------------
    print("\nTCP Analysis")
    print("-" * 30)

    if report.get("port_open"):
        print("✔ HTTPS Port (443) is open.")
        score += 30
    else:
        print("❌ HTTPS Port is closed.")

    # ---------------- Final ----------------
    print("\n" + "=" * 60)
    print(f"Overall Security Score : {score}/100")

    if score >= 90:
        print("Overall Status : Excellent")

    elif score >= 70:
        print("Overall Status : Good")

    elif score >= 50:
        print("Overall Status : Fair")

    else:
        print("Overall Status : Needs Attention")

    print("=" * 60)