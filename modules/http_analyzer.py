import requests
import time


def analyze(website):
    """
    Analyze the HTTP response of a website and return the results.
    """

    # Add https:// if the user didn't enter it
    if not website.startswith(("http://", "https://")):
        url = "https://" + website
    else:
        url = website

    try:
        start = time.time()

        response = requests.get(url, timeout=5)

        end = time.time()

        return {
            "status_code": response.status_code,
            "response_time": round((end - start) * 1000, 2),
            "server": response.headers.get("Server", "Unknown"),
            "content_type": response.headers.get("Content-Type", "Unknown"),
            "content_length": response.headers.get("Content-Length", "Unknown")
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": str(e)
        }


def run():
    print("=" * 55)
    print("        NetScope AI - HTTP Analyzer")
    print("=" * 55)

    website = input("Enter Website (Example: google.com): ")

    result = analyze(website)

    if "error" in result:
        print("\nError:", result["error"])
        return

    print("\n========== HTTP REPORT ==========\n")

    print(f"Status Code   : {result['status_code']}")
    print(f"Response Time : {result['response_time']} ms")
    print(f"Server        : {result['server']}")
    print(f"Content Type  : {result['content_type']}")
    print(f"Content Length: {result['content_length']}")


if __name__ == "__main__":
    run()