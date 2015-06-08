#!/usr/bin/env python
# this needs to be made in a template and then called as a template
#   with variables

import json
import requests
import atexit
import ssl
import threading, os
import sys
from pyVim.connect import SmartConnect, Disconnect
from sys import argv

script, input_name = argv

vuser = 'administrator@vsphere.local'
vcsvr = '192.168.110.20'
passwd = 'VMware1!'
vport = 443


class Getvcenterids(object):
    def __init__(self, vhost):
        self.vhost = vhost

    def si_connection(self, vhost, user, password, port):
        try:
            self.SI = SmartConnect(host=vhost, user=user, pwd=password, port=port)
        except:
            creds = self.vhost + " " + user + " " + password
            print creds
        return self.SI

    def get_names(self, top_path, name_list):
        path_list = top_path
        p = len(path_list)
        for i in range(0, p):
            dc_obj = path_list[i]
            name = dc_obj.name
            name_string = str(name)
            name_list.append(name_string)

    def get_ids(self, top_path, target_name):
        path_list = top_path
        p = len(path_list)
        for i in range(0, p):
            dc_obj = path_list[i]
            name = dc_obj.name
            name_string = str(name)
            if name_string == target_name:
                to_string = str(dc_obj)
                dc_obj_str = to_string.split(':')
                target_id = dc_obj_str[1]
                new_target_id = target_id.replace("'", "")
                obj_id = new_target_id
                return obj_id
            else:
                var_is = 0


v = Getvcenterids(vcsvr)
c = v.si_connection(vcsvr, vuser, passwd, vport)

dc = c.content.rootFolder.childEntity
dc_root = dc[0]

cluster_hash = {}
dvp_hash = {}
data_hash = {}

cluster_root = dc_root.hostFolder.childEntity
dvp_root = dc_root.networkFolder.childEntity
data_root = dc_root.datastoreFolder.childEntity

cluster_names = []
dvp_names = []
data_names = []

v.get_names(cluster_root, cluster_names)
v.get_names(dvp_root, dvp_names)
v.get_names(data_root, data_names)

for i in cluster_names:
    cluster_hash[i] = v.get_ids(cluster_root, i)

for d in data_names:
    data_hash[d] = v.get_ids(data_root, d)

for n in dvp_names:
    dvp_hash[n] = v.get_ids(dvp_root, n)

if isinstance(input_name, str):
    if input_name in cluster_names:
        print cluster_hash[input_name]
    elif input_name in dvp_names:
        print dvp_hash[input_name]
    elif input_name in data_names:
        print data_hash[input_name]
    else:
        print "ERROR Name not found"
