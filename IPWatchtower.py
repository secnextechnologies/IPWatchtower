import requests
import socket

def ip_lookup(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\nIP Address: {data['ip']}")
        print(f"Hostname: {data.get('hostname', 'N/A')}")
        print(f"City: {data.get('city', 'N/A')}")
        print(f"Region: {data.get('region', 'N/A')}")
        print(f"Country: {data.get('country', 'N/A')}")
        print(f"Location: {data.get('loc', 'N/A')}")
        print(f"ISP: {data.get('org', 'N/A')}")
    else:
        print("Failed to fetch IP data. Please check your internet connection or try again later.")

def dns_lookup(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror as e:
        return f"Error: {e}"

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1 - Only DNS lookup")
        print("2 - Only IP lookup")
        print("3 - Both DNS and IP lookup")
        print("4 - Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            domain_name = input("Enter a domain name to perform DNS lookup: ")
            ip_address = dns_lookup(domain_name)
            print(f"\nThe IP address of '{domain_name}' is: {ip_address}")

        elif choice == "2":
            ip_address = input("Enter the IP address to lookup: ")
            ip_lookup(ip_address)

        elif choice == "3":
            domain_name = input("Enter a domain name to perform DNS lookup: ")
            dns_ip = dns_lookup(domain_name)
            print(f"\nThe IP address of '{domain_name}' is: {dns_ip}")

            ip_lookup(dns_ip)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")
