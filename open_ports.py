import socket

open_ports_list = []

file_name = 'open_ports.txt'
with open(file_name,'w') as f:
	f.close()

choice = str(input('''Choose 1 OR 2:\n
	1 - Test All ports
	2 - Test Specific Ports\n\n>> '''))

#socket commands
a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if choice == "1":
	ports = range(65535)
	for port in ports:
		location = ("127.0.0.1", port)
		result_of_check = a_socket.connect_ex(location)
		if result_of_check == 0:
			print(f"[+] Port {port} is opened\n")
			open_ports_list.append(str(port))
			with open(file_name,'a') as f:
				f.write(str(port))
				f.close()
	if len(open_ports_list) != 0:
		print(f'[*] Open ports found: {len(open_ports_list)}')
		print(f'[*] All open ports found: {open_ports_list}')
	elif len(open_ports_list) == 0:
		print('No open ports found.')
elif choice == "2":
	while True:
		port = int(input('Write a port to check >> '))
		location = ("127.0.0.1", port)
		result_of_check = a_socket.connect_ex(location)
		if result_of_check == 0:
			print(f"[+] Port {port} is opened\n")
			with open(file_name,'a') as f:
				f.write(str(port))
				f.close()
		else:
			print(f"[-] Port {port} is closed\n")
