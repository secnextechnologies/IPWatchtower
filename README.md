# IPWatchtower
IPWatchtower is a powerful and user-friendly IP and domain lookup tool that puts the world of internet information at your fingertips.

# Description
IP Watchtower is a simple Python tool that allows you to perform DNS lookup and IP address lookup for a given domain name or IP address. It leverages the requests library to fetch IP information from the ipinfo.io API and the socket library to perform DNS lookups.

# Requirements
* Python 3.x
* requests library (install using pip install requests)

# How to Use
1. Clone this repository to your local machine or download the ipwatchtower.py file.
2. Install the required requests library by running the following command: pip install requests.
3. Run the ipwatchtower.py script using Python: python ipwatchtower.py.
4. Choose one of the following options:
  * Option 1: Perform DNS lookup - Enter a domain name to get its corresponding IP address.
  * Option 2: Perform IP lookup - Enter an IP address to get its geographical information.
  * Option 3: Perform both DNS and IP lookup - Enter a domain name to get its IP address and then retrieve its geographical information.
  * Option 4: Exit - Terminate the program.

# Usage Examples
1. Perform DNS lookup:
```
Options:
1 - Only DNS lookup
2 - Only IP lookup
3 - Both DNS and IP lookup
4 - Exit

Enter your choice (1/2/3/4): 1
Enter a domain name to perform DNS lookup: example.com

The IP address of 'example.com' is: 93.184.216.34
```
2. Perform IP lookup:
```
Options:
1 - Only DNS lookup
2 - Only IP lookup
3 - Both DNS and IP lookup
4 - Exit

Enter your choice (1/2/3/4): 2
Enter the IP address to lookup: 8.8.8.8

IP Address: 8.8.8.8
Hostname: dns.google
City: Mountain View
Region: California
Country: US
Location: 37.3860,-122.0838
ISP: AS15169 Google LLC
```
3. Perform both DNS and IP lookup:
```
Options:
1 - Only DNS lookup
2 - Only IP lookup
3 - Both DNS and IP lookup
4 - Exit

Enter your choice (1/2/3/4): 3
Enter a domain name to perform DNS lookup: example.com

The IP address of 'example.com' is: 93.184.216.34

IP Address: 93.184.216.34
Hostname: N/A
City: Dźwirzyno
Region: West Pomerania
Country: PL
Location: 54.1593,15.4112
ISP: AS15133 Edgecast Inc.
```

# Note
* This tool relies on the ipinfo.io API to fetch geographical information for IP addresses. There might be usage limitations or restrictions, so use the tool responsibly.
* If you encounter any issues related to internet connectivity or API errors, please check your internet connection or try again later.

# Disclaimer
This tool is provided as-is with no guarantee or warranty. The authors are not responsible for any misuse or damage caused by this tool.
