from csv import reader
import maya.cmds as cmds

f = open('/Users/eungyeulssssss/Desktop/data/mountain.csv', 'r')
data = reader(f)
next(data)
increment = 5

for i, row in enumerate(data):
    x = float(row[1])
    y = float(row[2])
    z = float(row[3])
    sphere = cmds.polySphere(r=0.5)[0]
    cmds.move(x, y, z, sphere)

    # x 축 25를 기준으로 왼쪽은 y 축이 4까지 내려가도록, 오른쪽은 y 축이 10까지 올라가도록
    if x < 25:
        cmds.move(0, (y - (25 - x) * 0.), 0, sphere, relative=True)  # y 값을 현재 좌표에 추가
    else:
        cmds.move(0, (y + (x - 25) * 0.3), 0, sphere, relative=True)  # y 값을 현재 좌표에 추가

f.close()
