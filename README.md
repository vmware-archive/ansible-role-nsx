# ansible-role-nsx

[![Build Status](https://travis-ci.org/jdatx/ansible-role-nsx.svg?branch=master)](https://travis-ci.org/jdatx/ansible-role-nsx)

Ansible playbook to automate installing and maintaining VMware NSX.

## Requirements
* nsx api endpoint
* [nsxramlclient](https://github.com/vmware/nsxramlclient)
* [ovftool](https://my.vmware.com/web/vmware/details?downloadGroup=OVFTOOL400&productId=353)
* nsx raml file which can be found [here](https://github.com/vmware/nsxraml/blob/master/nsxvapi.raml)
* nsx ansible modules which can be found [here](https://github.com/vmware/nsxansible)


## Role Variables

```yaml
# Playbook Variables
deploy_nsx_ova: (bool)
# local dir containing nsx ova
nsxmanOvaPath: '/var/www/html/downloads'
# nsx ova being deployed
nsxmanOva: 'VMware-NSX-Manager-6.2.4-4292526.ova'
# path to ovftool
ovfToolPath: '/usr/local/bin/ovftool'
# Raml File location
nsx_raml_file_path: '/path/to/raml/file'
#
```

## Example playbook

```yaml
---
- hosts: nsx
  roles:
    - nsx
  vars:
    - vars/main.yml
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
