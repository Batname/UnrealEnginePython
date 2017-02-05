import runcmd as cmd
import sys
from threading import Thread

def pipModuleAction(command, module):
	cmd.run('pip ' + command + ' ' + module, sys.path[1] + "/Scripts")

def install(module):
	t = Thread(target=installModule, args=('install',module,))
	t.start()

def uninstall(module):
	t = Thread(target=installModule, args=('uninstall',module,))
	t.start()