#!/usr/bin/env python3

import json
student='{"name":"sandeepr","standard":"mca","rollno":20}'
print(student)
print(type(student))
t=json.loads(student)
print(t)
