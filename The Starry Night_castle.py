from csv import reader
import maya.cmds as cmds
import random

# CSV 파일 경로 설정
csv_file_path = '/Users/eungyeulssssss/Desktop/data/castle.csv'

# CSV 파일 읽기
with open(csv_file_path, 'r') as file:
    data = reader(file)
    next(data)  # 헤더 행 스킵

    target_sphere = cmds.polySphere(radius=1, n='target_sphere')[0]
    cmds.move(7.5, 50, 15, target_sphere)

    # 각 랜덤 데이터에 대해 실린더 생성 및 aimConstraint 설정
    for i, row in enumerate(data):
        x = float(row[1])
        y = float(row[2])
        z = float(row[3])

        cylinder = cmds.polyCylinder(r=0.1, h=5, n=f'castle_{i}')[0]
        cmds.move(x, y, z, cylinder)
        cmds.select(f'castle_{i}')

        aim_constraint = cmds.aimConstraint(target_sphere, cylinder, aimVector=(0, 1, 0), u=(0, 0, 1),
                                            wut="objectrotation", wuo=target_sphere)
