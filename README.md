# Logrotate

Master: [![Build Status](https://travis-ci.org/sansible/logrotate.svg?branch=master)](https://travis-ci.org/sansible/logrotate)  
Develop: [![Build Status](https://travis-ci.org/sansible/logrotate.svg?branch=develop)](https://travis-ci.org/sansible/logrotate)

* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Settings](#settings)
* [Examples](#examples)

Configures logrotate scripts for log files. Comes with some builtin configs
and allows for custom configs.


## Installation and Dependencies

To install this role run `ansible-galaxy install sansible.logrotate` or add
this to your `roles.yml`.

```YAML
- src: sansible.logrotate
  version: v4.1.0-latest
```

and run `ansible-galaxy install -p ./roles -r roles.yml`


## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs Logrotate server.
* `configure` - Configures and ensures that the service is running.


## Settings

|Variable|Default|Description|
|---|---|---|
|sansible_logrotate_application_logs_delay_compress|yes|Whether to delay compression of rotated application logs [1]|
|sansible_logrotate_application_logs_delete_rotated_logs|no|Whether to delete rotated application logs via postrotate [2]|
|sansible_logrotate_application_logs_frequency|daily|Frequency of logrotate executions [1]|
|sansible_logrotate_application_logs_paths|[]|Out of the box config for generic application logs|
|sansible_logrotate_application_logs_rotate_days|7|Number of days to retain application logs|
|sansible_logrotate_application_logs_rotate_size|~|Size constraint for rotating application logs|
|sansible_logrotate_custom_configs|[]|Specify a path and a list of options to go into the config file|
|sansible_logrotate_version|~|Version number Logrotate package|

[1] https://linux.die.net/man/8/logrotate
[2] Forcible deletes log files as rotate 0 seems to leave a single rotated log behind

## Examples

**Note** You can force logrotate to run like so:

```BASH
# Dry run
logrotate -d /etc/logrotate.conf
# Actual run
logrotate -d -f /etc/logrotate.conf
```

Install with builtin application log config and custom config:

```YAML
- name: Install Logrotate
  hosts: sandbox

  roles:
    role: logrotate
    sansible_logrotate_application_logs_delay_compress: yes
    sansible_logrotate_application_logs_paths:
      - /application/logs/*.log
      - /another_application/logs/*.log
    sansible_logrotate_custom_configs:
      - name: custom_log
        path: "/var/log/cutom/*.log"
        options:
          - weekly
          - size 25M
          - missingok
          - compress
          - delaycompress
          - copytruncate
        scripts:
          postrotate: "service rsyslog restart"
```
