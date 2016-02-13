import os, time, sys, json
// debug variable
debg = True
// pipe for tshark input
pipe_name = '/tmp/myshark'
// read input lines from tshark , convert to json store in mongodb
pipein = open(pipe_name, 'r')
while True:
	line = pipein.readline()[:-1]
	if debg: 
		print line
	fields = line.split()
	if debg:
		print fields

	json_line = json.dumps(line)



	



