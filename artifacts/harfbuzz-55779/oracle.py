"""
	It receives an execution result of fuzzer with a failing test case
"""

import sys

failure_type = "ERROR"

f = open(sys.argv[1], 'r')
exec_result = ''.join(f.readlines())

if failure_type not in exec_result:
	print("This is different failure type")
	exit()

print("Find a failure by a target bug")
