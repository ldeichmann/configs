#!/usr/bin/env python3

from subprocess import Popen, PIPE
import json, sys

def getActiveOutputs(searchOutput):
	(stdout, stderr) = Popen(["i3-msg","-t", "get_outputs"], stdout=PIPE).communicate()
	outputs = json.loads(stdout.decode("utf-8"))

	for i in outputs:
		if i['name'] == searchOutput:
			return i['current_workspace']
	getWorkspacesOnOutput(searchOutput)
#	print(outputs)

def getWorkspacesOnOutput(searchOutput):
	(stdout, stderr) = Popen(["i3-msg","-t", "get_workspaces"], stdout=PIPE).communicate()
	outputs = json.loads(stdout.decode("utf-8"))
	workspaces = []
	for i in outputs:
		if i['output'] == searchOutput:
			workspaces.append({'name':i['name'], 'visible':i['visible'], 'focused':i['focused']})
	return workspaces	



def buildString(searchOutput, active, workspaces):
	returnstring = "%{A5:/usr/bin/i3-msg workspace next_on_output:}%{A4:i3-msg workspace prev_on_output:}"
	for i in workspaces:
		if i['visible'] == True and i['focused'] == True:
			returnstring += "%{F#ffff8547}" + "" + "%{F#ffffffff} "
		elif i['visible'] == True and i['focused'] == False:
			returnstring +=  "%{F#ff17fff0}"+ "" + "%{F#ffffffff} "
		else:
			returnstring +=  "%%{A:/usr/bin/i3-msg workspace %s:}" %i['name'] + "%{F#ffffffff}" + "" + "%{A} "
	returnstring += "%{A}%{A}"

	return returnstring

 


if __name__ == '__main__':
	if len(sys.argv) > 0:
		currws = getActiveOutputs(sys.argv[1])
		listws = getWorkspacesOnOutput(sys.argv[1])
		print(buildString(sys.argv[1], currws, listws))

	else:
		getActiveOutputs('HDMI-0')