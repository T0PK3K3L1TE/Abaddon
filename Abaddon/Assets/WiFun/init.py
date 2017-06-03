import os, sys, commands 

#FilesToCheck
fls = ['Main.py']

#Stage 1      | Grab Files In Directory For Correct Install
cmd = "ls"
out = commands.getoutput(cmd)
osp = out.split("\n")

