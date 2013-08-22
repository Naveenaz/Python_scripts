
import os
import time


pnumber = os.getpid()
where = os.getcwd()
used = os.times()
now = time.time()
means = time.ctime(now)
time_clock=time.clock()

print "Process ID",pnumber
print "Current Directory",where

print "System information",used

print "\nTime is now",now
print "Which interprets as",means

print "time_clock",time_clock