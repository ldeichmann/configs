#!/usr/bin/env python2
import json
import subprocess
import time, os

i3_cmd = 'i3-msg -t get_tree'

def get_layout():
    get_tree = subprocess.Popen(i3_cmd.split(), stdout=subprocess.PIPE)
    stdout = get_tree.communicate()[0]
    try:
        tree = json.loads(stdout)
    except ValueError:
        tree = {}
    return tree

def lock():
    subprocess.call(['sh', os.path.dirname(os.path.realpath(__file__)) + '/lock.sh'])

def any_fullscreen_window(node):
    if node['window']:
        return node['fullscreen_mode'] == 1
    return any(any_fullscreen_window(n) for n in node.get('nodes', ''))

if __name__ == '__main__':
    if not any_fullscreen_window(get_layout()):
        lock()        
