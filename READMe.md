## Ansible GGR Selenoid Cluster

#### Requirements

* `python`
* `docker`

For running Ansible cluster's playbook required pre-installed Python and Ansible

Install [Python](https://www.python.org/downloads/)
Install [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

or using HomeBrew for MacOS users

```console
$ brew install python
$ brew install ansible
```

#### Check that Ansible is installed. Example of console output

```console
$ ansible --version
ansible [core 2.16.0]
  config file = None
  configured module search path = ['/Users/user/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/Cellar/ansible/9.0.1/libexec/lib/python3.12/site-packages/ansible
  ansible collection location = /Users/user/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/local/bin/ansible
  python version = 3.12.0 (main, Oct  5 2023, 15:52:37) [Clang 14.0.3 (clang-1403.0.22.14.1)] (/usr/local/Cellar/ansible/9.0.1/libexec/bin/python)
  jinja version = 3.1.2
  libyaml = True
  ```

### Preparing VM cloud machines

  By default, cluster is expecting 1 VM for GGR and 2 for Selenoid, but it can be changed inside "cluster.yml"

### Generating hosts.ini file

Before running Ansible playbooks, you need to generate your hosts.ini file that already exists in project, but you can override it using Python script "generate_hosts_file.py" with the following arguments:

  | Argument                     | Values              | Description                                   |
  | ---                          | ---                 | ---                                           |
  | ansible_ssh_private_key_file | ~/.ssh/test.pem     | Your ssh key, generated to working with VM's  |
  | GGR IP                       | cloud machine ip    | VM IP in AWS, GCP, Azure                      |
  | Selenoid 1 IP                | cloud machine ip    | VM IP in AWS, GCP, Azure                      |
  | Selenoid 2 IP                | cloud machine ip    | VM IP in AWS, GCP, Azure                      |
  
Selenoid VM's can be extended

```console
$  generate_hosts_file.py "~/.ssh/test.pem" 10.1.2.3 10.4.5.6 10.7.8.9
```

### Running Ansible cluster

Use the following command to up and run Ansible cluster

```console
$  ansible-playbook cluster.yml -i hosts
```
Note: it takes 2-4 min to set up all necessary libraries, docker to all machines and run GGR and Selenoid

To check cluster status make request to GGR instance "http://ggr-ip:8888/status". It should returns JSON data with connected machines, browser types, browser versions.

Browsers data, versions before running playbook can be added/changed in "cluster.yml"