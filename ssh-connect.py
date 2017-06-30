from netmiko import ConnectHandler
import getpass
import sys

#ip_addr = raw_input("Enter IP Address: ").strip()
password = getpass.getpass(prompt='Password: ')
host = sys.argv[1]

srx = {
	'device_type': 'cisco_ios',
    'host': host,
    'username': 'natalia.gromova',
    'password': password,
    'port': 22,
    'ssh_config_file': '~/.ssh/config',
    'verbose': False,
}

net_connect = ConnectHandler(**srx)
output = net_connect.send_command('show version')
print output
