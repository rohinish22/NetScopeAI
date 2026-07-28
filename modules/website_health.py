from modules import dns_analyzer
from modules import http_analyzer


def analyze(website):

    dns = dns_analyzer.analyze(website)
    http = http_analyzer.analyze(website)

    score = 0

    if "error" not in dns:
        score += 50

    if http.get("status_code") == 200:
        score += 50

    return {
        "score": score,
        "dns": dns,
        "http": http
    }


def run():
    website = input("Enter Website: ")

    result = analyze(website)

    print("\n===== WEBSITE HEALTH =====")
    print(f"Health Score : {result['score']}/100")


if __name__ == "__main__":
    run()