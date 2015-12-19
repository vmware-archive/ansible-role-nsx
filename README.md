# ansible-role-nsx

Ansible playbook to automate installing and maintaining VMware NSX.

## Requirements

This role has a single dependency on the [Chaperone](https://github.com/vmware/chaperone)
project. In particular, this role requires that an external source(e.g., the
playbook) define the variable django_app, which usually is "chaperone" but may
be set to any value that defines the 'chaperone application' intending to
configure and install NSX.

## Role Variables

```yaml
# this is where the UI installs the ovftool this by default
ovftool: /usr/local/bin/ovftool/ovftool
```

## Example playbook

```yaml
---
- hosts: nsx
  sudo: True
  roles:
    - nsx
  vars:
    - ... forthcoming
```

# License and Copyright
 
Copyright 2015 VMware, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

