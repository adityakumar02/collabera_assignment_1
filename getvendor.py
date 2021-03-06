import requests
import argparse

print("[*] Welcome")

# Function to get the interface name


def get_arguments():

	
	parser = argparse.ArgumentParser()

	# Parsing the arguments
	parser.add_argument("-m", "--macaddress",
                     dest="mac_address",
                     help="44:38:39:ff:ef:57"
                     )
	options = parser.parse_args()

	
	if options.mac_address:
		return options.mac_address
	else:
		parser.error("[!] Invalid Syntax. ")


def mac_details(mac_address):

	# This is the Api that I get it from macaddress.io
	url = "https://api.macaddress.io/v1?apiKey=at_DI1LSWjj7x0H4iBuzlVzyjYhC5wys&output=json&search=44:38:39:ff:ef:57"

	# Use get method to fetch details
	response = requests.get(url+mac_address)
	if response.status_code != 200:
		raise Exception("[!] Invalid MAC Address!")
	return response.content.decode()


# Driver Code
if __name__ == "__main__":
	mac_address = get_arguments()
	print("[+] Checking Details...")

	try:
		company_name = mac_details(mac_address)
		print("[+] company is "+company_name, "and the MAC is"+mac_address)
	except:

	
		print("[!] An error occured.")
