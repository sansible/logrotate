# Logrotate

Master: [![Build Status](https://travis-ci.org/sansible/logrotate.svg?branch=master)](https://travis-ci.org/sansible/logrotate)  
Develop: [![Build Status](https://travis-ci.org/sansible/logrotate.svg?branch=develop)](https://travis-ci.org/sansible/logrotate)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Settings](#settings)
* [Examples](#examples)

Configures logrotate scripts for log files. Comes with some builtin configs and allows for custom configs.

Please [Makefile] for test commands if you wish to contribute to this role. If you want to test
locally using Ubuntu Xenial, create .make file (if it's not already created) and add the line
VAGRANT_BOX=ubuntu/xenial64.




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

To install this role run `ansible-galaxy install sansible.logrotate` or add
this to your `roles.yml`.

```YAML
- src: sansible.logrotate
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs Logrotate server.
* `configure` - Configures and ensures that the service is running.




## Settings

|Variable|Default|Description|
|---|---|---|
|version|~|Version number Logrotate package|
|builtin_configs|{ 'application_logs': { 'enabled': false, 'paths': [] } }|Out of the box configs for certain log types|
|custom_configs|[]|Specify a path and a list of options to go into the config file|




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
    logrotate:
      builtin_configs:
        application_logs:
          enabled: true
          paths:
            - /application/logs/*.log
            - /another_application/logs/*.log
      custom_configs:
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
