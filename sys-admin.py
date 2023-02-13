import os
import subprocess

# os.system("ls")


output = subprocess.run(["ls"], capture_output=True, text=True)

# print(output)
print(output.stdout)