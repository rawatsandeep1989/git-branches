#!/usr/bin/env python3

import re

with open('/home/sandeepr/server_list') as fp:
    for cnt,line in enumerate(fp):
#        print("{} : {}".format(cnt,line))
        x=re.search("one.com",line)
        print(type(x ))
        
    
    
