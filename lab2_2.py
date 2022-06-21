#  2.2 Lab - CLI Automation with Python using netmiko
from netmiko import ConnectHandler

def exec():
    sshCli = ConnectHandler(device_type='cisco_ios',
                            host='192.168.18.47',
                            port=22,
                            username='cisco',
                            password='cisco123!')

    createLoopback(sshCli)
    showIP(sshCli)


def createLoopback(sshCli):
    config_commands = [
        'int loopback 1',
        'ip address 2.2.2.2 255.255.255.0',
        'description WHATEVER'
    ]
    output = sshCli.send_config_set(config_commands)
    print(output)

def showIP(sshCli):
    output = sshCli.send_command("show ip int brief")
    print("show ip int brief:\n{}\n".format(output))

if __name__ == '__main__':
    exec()
