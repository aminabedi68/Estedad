import os
import sys

cwd = os.getcwd()

source = cwd + '\\' + str(sys.argv[1])
destination = cwd + '\\' + str(sys.argv[2])

os.rename(source,destination)