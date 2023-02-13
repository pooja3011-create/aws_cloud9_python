import os
import subprocess

#Use os.system() to run a Bash command
#Use subprocess.run() to run Bash commands

os.system("ls")

subprocess.run("ls")

subprocess.run(["ls","-l"])

subprocess.run(["ls","-l","README.md"])

#Retrieving system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])