from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 22,
}

connexion = ConnectHandler(**cisco_router)


clock = connexion.send_command("show clock")
print(clock)

interface = connexion.send_command("sh ip int br")
with open ('interfaces.txt' , "w") as f:
    f.write(interface)


param = [  'interface loopback 0',
           'ip address 10.8.8.8 255.255.255.240',
           'exit'
         ]


loop = connexion.send_config_set(param)
print(loop)














