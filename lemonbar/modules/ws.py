#!/usr/bin/env python3

from subprocess import Popen, PIPE
import json, sys
import i3ipc
from os.path import expanduser

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
	returnstring = returnstring[:-1]
	returnstring += "%{A}%{A}"

	return returnstring

def on_workspace(self, e):
    # The first parameter is the connection to the ipc and the second is an object
    # with the data of the event sent from i3.
	currws = getActiveOutputs(sys.argv[1])
	listws = getWorkspacesOnOutput(sys.argv[1])
	full = buildString(sys.argv[1], currws, listws)
	#print(buildString(sys.argv[1], currws, listws))
	f = open(expanduser("~")+'/.config/lemonbar/modules/ws.out', 'w')
	print(buildString(sys.argv[1], currws, listws), file=f, end="")
	#(stdout, stderr) = Popen(['sed -i "1 c\%s" ~/.config/lemonbar/bar.out' %(full)], stdout=PIPE).communicate()
	#print(stdout)

if __name__ == '__main__':

	if len(sys.argv) > 1:
		# currws = getActiveOutputs(sys.argv[1])
		# listws = getWorkspacesOnOutput(sys.argv[1])
		# print(buildString(sys.argv[1], currws, listws))
		f = open(expanduser("~")+'/.config/lemonbar/modules/ws.out', 'w')
		print("", file=f, end="")
		# Create the Connection object that can be used to send commands and subscribe
		# to events.
		conn = i3ipc.Connection()

		# Subscribe to the workspace event
		conn.on('workspace::focus', on_workspace)

		# Start the main loop and wait for events to come in.
		conn.main()

	else:
		print("xrandr output name required")