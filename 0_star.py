from csv import reader
import maya.cmds as cmds

f = open('/Users/eungyeulssssss/Desktop/data/star.csv', 'r')
data = reader(f)
next(data)

for i, row in enumerate(data):
    x = float(row[1])
    y = float(row[2])
    z = float(row[3])
    sphere = cmds.polySphere(r=0.1)[0]
    cmds.move(x, y, z, sphere)
