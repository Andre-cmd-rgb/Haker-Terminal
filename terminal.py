import subprocess
import platform
import socket
import time
import os
import wget

url = 'https://raw.githubusercontent.com/Andre-cmd-rgb/Cherry-Terminal/main/terminal.py'
path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Cherry Terminal [Version 1.2 beta]")
while True:
	code = input(">>> ")
	if code == 'ping':
		host = input("Enter Website To Ping: ")
		number = input("Enter How Many Times To Ping: ")

		def ping(host):
			param = '-n' if platform.system().lower() == 'windows' else '-c'
			command = ['ping', param, number, host]
			return subprocess.call(command)
		print(ping(host))
	if code == 'local':
		print("Your Local IPS Is: " + host_ip)
		print("Your Desktop Name Is: " + host_name)
	if code == 'date':
		print("The Local Date Is: " + time.strftime("%m/%d/%Y"))
	if code == 'ls':
		dir_list = os.listdir(path)
		print("Files and Directories in '", path, "' :")
		print(dir_list)
	if code == 'ls -a':
		file = input("Enter The Direct File Path To Read: ")
		dir_list2 = os.listdir(file)
		print("Files and directories in '", file, "':")
		print(dir_list2)
	if code == 'echo':
		echo = input("What Do You Want Me To Echo:")
	if code == 'help':
		print('aviable commands:')
		print('ping')
		print('local')
		print('date')
		print('ls')
		print('ls -a')
		print('echo')
		print('cd')
		print('exit')
	if code == 'exit':
		os.system(exit)
	if code == 'cd':
		chdir = input("Where do you want to cd:")
		os.chdir(chdir)
	if code == 'upgrade':
		filename = wget.download(url)
		os.remove("terminal.py")
		os.rename('terminal (1).py', 'terminal.py')
		os.system(exit)
