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
 
Copyright 2015 VMware, Inc. All rights reserved.

SPDX-License-Identifier: Apache-2.0 OR GPL-3.0-only

This code is Dual Licensed Apache License 2.0 or GPLv3

You may obtain a copy of the License(s) at

    http://www.apache.org/licenses/LICENSE-2.0

    or

    https://www.gnu.org/licenses/gpl-3.0.en.html
