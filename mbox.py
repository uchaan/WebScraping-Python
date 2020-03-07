import re
hand = open("mbox.txt")
tmp = float(-1)
for line in hand: 
    line.rstrip()
    stuff = re.findall('^X.*: ([0-9.]+)',line)
    if len(stuff):
        val = float(stuff[0])
        if val > tmp:
            tmp = val
        
    
print(tmp)
