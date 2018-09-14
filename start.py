#!/usr/bin/env python
# -*- coding: utf-8 -*-
from termcolor import *
from iprange import *
import re

should_change_target = 1

print colored("[+] Please input your team token...", "cyan")
teamtoken = raw_input()
print colored("[+] Please input the word when submit flag failed, default is `err`...", "cyan")
failed = raw_input()
if (failed == ""):
    failed = "err"
print colored("[+] Please input target iprange, like 192.168.1.1-192.168.1.22, if input nothing, target will not change ...", "cyan")
ip = raw_input()
if (ip == ""):
    should_change_target = 0
print colored("[+] Please input target port, default 80 ...", "cyan")
port = raw_input()


# write tean token and failed string
with open("exploit_all.py", "a") as f:
    content = f.read()
    f.write(re.sub(r'token = \".+\"', 'token="%s"' % (teamtoken), content))
    pass


# write targets ip and port
if should_change_target == 1:
    with open("targets.txt", "w") as f:
        for host in iprange(ip):
            f.write("%s:%s\n" % (host, port))
