import requests
import time

print("=" * 50)
print("      NetScope AI - HTTP Analyzer")
print("=" * 50)

website = input("Enter Website (Example: https://amazon.com): ")

try:
    # Start Timer
    start = time.time()

    # Send HTTP GET Request
    response = requests.get(website)

    # Stop Timer
    end = time.time()

    print("\n========== HTTP REPORT ==========")
    print(f"Website         : {website}")
    print(f"Status Code     : {response.status_code}")
    print(f"Response Time   : {(end-start)*1000:.2f} ms")
    print(f"Server          : {response.headers.get('Server', 'Unknown')}")
    print(f"Content Type    : {response.headers.get('Content-Type', 'Unknown')}")
    print(f"Content Length  : {len(response.content)} bytes")

except Exception as e:
    print("\nError :", e)