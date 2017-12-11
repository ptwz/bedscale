import collections
import math
import serial
import sys
import time

class sensor(collections.deque):
    def average(self):
        return float(sum(self))/len(self)

    def stdev(self):
        if len(self)<2:
            return 0
        avg = self.average()
        return math.sqrt(sum([ (x-avg)**2 for x in self ])/(len(self)-1))

SENSORS = 4
FACTOR =  (86./float(abs(2.37353e+06 - 3.82145e+06))) * 83.3/81.6973984751

queues = [None]*SENSORS

for i in range(SENSORS):
    queues[i] = sensor(maxlen=20)

summe = 0
avg = 0
stable = False
i=0
last_value = 0

s=serial.Serial("/dev/ttyUSB0", 38400)

while s.is_open:
    line = s.readline()
    i+=1
    line = line.strip()
    d = line.split("\t")
    d = [int(x) for x in  d[-SENSORS:]]
    for (queue,value) in zip(queues, d):
        queue.append(value)
    
    averages = [ queue.average() for queue in queues]
    sdevs = [ queue.stdev() for queue in queues]

    summe = sum(averages)*FACTOR
    avg = ((avg * 9) + summe)/10
    sdev = sum(sdevs)*FACTOR
    new_stable = sdev < .05
    if new_stable!=stable:
        if new_stable:
            if abs(last_value - summe) > 2:
                print time.time(), summe, summe-last_value, sum(sdevs)*FACTOR
                sys.stdout.flush()
                last_value = summe
        stable = new_stable
    #print sum(v)*FACTOR, " ".join([str(x*FACTOR) for x in v])
    
