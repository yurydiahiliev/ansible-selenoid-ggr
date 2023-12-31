import argparse
from configparser import ConfigParser

def generate_hosts_file(pem_path, ggr_ip, selenoid1_ip, selenoid2_ip):
    config = ConfigParser()

    config['all:vars'] = {
        'ansible_python_interpreter': '/usr/bin/python3',
        'ansible_user': 'ubuntu',
        'ansible_ssh_private_key_file': pem_path,
        'ansible_ssh_common_args': "'-o StrictHostKeyChecking=no'"
    }

    config['ggr'] = {
        'ggr ansible_host': ggr_ip
    }

    config['selenoid-nodes'] = {
        'selenoid1 ansible_host': selenoid1_ip,
        'selenoid2 ansible_host': selenoid2_ip
    }

    with open('hosts.ini', 'w') as file:
        for section in config.sections():
            file.write(f"[{section}]\n")
            for key, value in config[section].items():
                file.write(f"{key}={value}\n")
            file.write("\n")

    print("hosts.ini file created successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate hosts.ini file with specified PEM file path and IP addresses.")
    parser.add_argument("pem_path", help="Path to the PEM file")
    parser.add_argument("ggr_ip", help="IP address for ggr")
    parser.add_argument("selenoid1_ip", help="IP address for selenoid1")
    parser.add_argument("selenoid2_ip", help="IP address for selenoid2")

    args = parser.parse_args()

    generate_hosts_file(args.pem_path, args.ggr_ip, args.selenoid1_ip, args.selenoid2_ip)
