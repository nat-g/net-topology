 #!/usr/bin/python

import paramiko
import getpass


def main():
	host = 'globjump04.test.com.au'
	username = 'natalia'
	password = getpass.getpass(prompt='Password: ')
#	k = paramiko.RSAKey.from_private_key_file("/Users/natalia/.ssh/id_rsa")
#	password = getpass.getpass('Password:')
	ssh = paramiko.SSHClient()
	ssh._policy = paramiko.WarningPolicy()
#	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	print "connecting"

	ssh.connect('host', 22, username = 'username', password = 'password', pkey = 'k')
	print "connected"
	stdin, stdout, stderr = ssh.exec_command("pwd")
	print stdout.readlines()
	ssh.close()

if __name__=="__main__":
	main()
