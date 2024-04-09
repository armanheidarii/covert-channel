import requests
import time

offset = 1000
ports = []

text = input("Please Enter Your Text: ")
for ch in text:
    ports.append(ord(ch) + offset)

ports.append(4444)

print("Your Encoded Massage is: ", ports)


def send_http_requests(ip, ports, time_interval):
    for port in ports:
        url = f"{ip}:{port}"
        try:
            start_time = time.time()
            print(f"Request was sent to {url}")
            response = requests.get(url)
            print(f"Response from port {port}: {response.status_code}")
            end_time = time.time()

            rtt = end_time - start_time

            print(f"Round-Trip Time for port {port}: {rtt} seconds")

            time.sleep(time_interval)
        except:
            print("No Response")


time_interval = int(input("Please Enter Your Time Interval: "))
send_http_requests("194.225.24.105", ports, time_interval)
