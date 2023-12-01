## Selenoid in docker

Set up [selenoid](https://github.com/aerokube/selenoid) in docker

#### Requirements

* `python`
* `docker`

#### Variables

```yaml
selenoid_version: 1.10.10 # Install selenoid version
selenoid_cm_version: 1.8.5 # Install configuration manager version
selenoid_docker_api_version: 1.42 # Docker api version (for Selenoid)
selenoid_limit: 4 # Total number of simultaneously running containers http://aerokube.com/selenoid/latest/#_recommended_docker_settings
selenoid_tmpfs: 128 # Add in-memory filesystem (tmpfs) to container http://aerokube.com/selenoid/latest/#_other_optional_fields
selenoid_config_dir: /etc/selenoid # Selenoid configuration dir
selenoid_listen_port: 4444 # Listen port
selenoid_time_zone: Europe/London # Timezone in container
selenoid_browsers_last_versions: 2 # How many last version browsers need download in selenoid
selenoid_browsers: # What browsers to download
  - firefox
  - opera
  - chrome
```

#### Example

```yaml
---
- hosts: all
  roles:
  - selenoid
```
