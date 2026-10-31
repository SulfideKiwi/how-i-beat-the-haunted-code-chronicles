from botcore import *
from time import sleep

rat_spells = {
    "Jill" : [349, 440],
    "Jeff" : [262, 272, 282],
    "Sarah" : [523, 440, 330, 349],
    "David": [523, 262, 440, 330, 392]
}

for i in rat_spells:
    for j in rat_spells[i]:
        spkr.pitch(j)
        sleep(.001)
        spkr.off()
    sleep(3)
    
for i in range(3):
    for i in rat_spells:
        for j in rat_spells["David"]:
            spkr.pitch(j)
            sleep(.001)
            spkr.off 
        sleep(3)
