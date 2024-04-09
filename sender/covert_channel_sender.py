from dotenv import load_dotenv
import os
import requests
import time


def send_http_requests(ip, ports, time_interval):
    sum_time = 0

    for port in ports:
        url = f"http://{ip}:{port}/"
        try:
            start_time = time.time()
            print(f"Request was sent to {url}")
            response = requests.get(url)
            print(f"Response from port {port}: {response.status_code}")
            end_time = time.time()

            rtt = end_time - start_time
            sum_time += rtt

            print(f"Round-Trip Time for port {port}: {rtt} seconds")

            time.sleep(time_interval)
        except ValueError:
            print(ValueError)

    return sum_time


print("Please Enter Your Time Interval First In .env file")
load_dotenv("../.env")

time_interval = int(os.getenv("INTERVAL"))

offset = 1000
ports = []

text = input("Please Enter Your Text: ")
for ch in text:
    ports.append(ord(ch) + offset)

end_port = 4444
ports.append(end_port)

print("Your Encoded Massage is: ", ports)

sum_time = send_http_requests("0.0.0.0", ports, time_interval)
print(f"The sum of sending the entire message is equal to {sum_time} seconds")
