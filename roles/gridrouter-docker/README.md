## GridRouter in docker

Set up [GridRouter](https://github.com/aerokube/ggr) in docker

#### Requirements

* `python`
* `docker`

#### Variables

```yaml
grid_router_version: 1.7.1 # Install GridRouter version
grid_router_path: /etc/grid-router # Path to GridRouter
grid_router_qouta_path: /etc/grid-router/quota # Path to GridRouter quota
grid_router_qouta_user: selenoid # GridRouter quota user
grid_router_qouta_password: selenoid # GridRouter quota password
grid_router_time_zone: Europe/London # Timezone in container
grid_router_port: 4444 # GridRouter port
grid_router_sctl_version: 1.2.0 # sctl version — https://github.com/seleniumkit/sctl/releases
grid_router_docker_api_version: 1.42 # Docker api version (for GridRouter)
grid_router_host_list: group # Host list for selenoid.xml

grid_router_regions: # Hosts list per region
    - name: "region-1"
      hosts:
        - name: localhost
          port: 4444
          browser_count: 4


grid_router_browsers: # Browser list usage selenoid
  - name: "firefox"
    defaultVersion: "119.0"
    versions:
      - "119.0"
      - "118.0"
      - "117.0"
  - name: "chrome"
    defaultVersion: "119.0"
    versions:
      - "119.0"
      - "118.0"
      - "117.0"
  - name: "opera"
    defaultVersion: "105.0"
    versions:
      - "105.0"
      - "104.0"
      - "103.0"
```

All supported browsers see [here](https://github.com/aerokube/selenoid#ready-to-use-browser-images).

Ggr is [using](http://aerokube.com/ggr/latest/#_creating_users_file) htpasswd files to store authentication data. Passwords are stored in encrypted form.

#### Example

```yaml
---
- hosts: all
  roles:
  - gridrouter
```
