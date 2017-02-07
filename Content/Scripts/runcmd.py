#ue.exec('pip2.py')

import subprocess
import sys
import unreal_engine as ue
import _thread as thread

ue.log(sys.path)

#define some convenience paths
def PythonHomePath():
	for path in sys.path:
		if ('UnrealEnginePython' in path and
			path.endswith('Binaries/Win64')):
			return path
	
	#return sys.path[1]
	return "not found"

def PythonHomeScriptsPath():
	home = PythonHomePath()
	return home + "/Scripts"

_PythonHomePath = PythonHomePath()

def FolderCommand(folder):
	#replace backslashes
	folder = folder.replace('/','\\')

	changefolder = "cd /d \"" + folder + "\" & "
	return changefolder


#main public function
def run(process, folder=_PythonHomePath):
	#todo: change folder
	fullcommand = FolderCommand(folder) + process
	ue.log("Started cmd <" + fullcommand + ">")
	stdoutdata = subprocess.getstatusoutput(fullcommand)
	ue.log("cmd Result: ")
	ue.log(stdoutdata[1])
	return stdoutdata[1] #return the data for dependent functions


def Test():
	#debug test - 
	run('dir')	