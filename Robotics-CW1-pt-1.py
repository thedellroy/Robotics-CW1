import numpy as np
import sympy as sy
import roboticstoolbox as rtb
import matplotlib.pyplot as plt
import spatialmath as sp

#DH parameters ||===========================================
L0 = 0.10
L1 = 0.20
L2 = 0.30
L3 = 0.30
L4 = 0.10
L5 = 0.05

init = [0,0.5,0,0,0,0]

theta1 = 0
theta4 = 0
theta5 = 0
theta6 = 0

D2 = 0.5
D3 = 0

J1 = np.radians(theta1)
J4 = np.radians(theta4)
J5 = np.radians(theta5)
J6 = np.radians(theta6)

#DH Table 

DH = np.array([[0,0,L0,0],[0,0,0,J1],[0,0,D2,0],[np.radians(90),0,D3,0],[0,0,L1,J4],[np.radians(90),L2,L5,J5],[0,0,L3,J6],[0,0,L4,0]])

print(DH,"\n")

#Transformation matrices ||=================================

TB_0 = np.array([[np.cos(DH[0,3]),-np.sin(DH[0,3]),0,DH[0,0]],[np.sin(DH[0,3]),np.cos(DH[0,3]),0,0],[0,0,1,0],[0,0,0,1]])
T0_1 = np.array([[np.cos(DH[1,3]),-np.sin(DH[1,3]),0,DH[1,0]],[np.sin(DH[1,3]),np.cos(DH[1,3]),0,0],[0,0,1,0],[0,0,0,1]])
T1_2 = np.array([[np.cos(DH[2,3]),-np.sin(DH[2,3]),0,DH[2,0]],[np.sin(DH[2,3]),np.cos(DH[2,3]),0,0],[0,0,1,0],[0,0,0,1]])
T2_3 = np.array([[np.cos(DH[3,3]),-np.sin(DH[3,3]),0,DH[3,0]],[np.sin(DH[3,3]),np.cos(DH[3,3]),0,0],[0,0,1,0],[0,0,0,1]])
T3_4 = np.array([[np.cos(DH[4,3]),-np.sin(DH[4,3]),0,DH[4,0]],[np.sin(DH[4,3]),np.cos(DH[4,3]),0,0],[0,0,1,0],[0,0,0,1]])
T4_5 = np.array([[np.cos(DH[5,3]),-np.sin(DH[5,3]),0,DH[5,0]],[np.sin(DH[5,3]),np.cos(DH[5,3]),0,0],[0,0,1,0],[0,0,0,1]])
T5_T = np.array([[np.cos(DH[6,3]),-np.sin(DH[6,3]),0,DH[6,0]],[np.sin(DH[6,3]),np.cos(DH[6,3]),0,0],[0,0,1,0],[0,0,0,1]])

#Forward kinematics 

TB_T = TB_0*T0_1*T1_2*T2_3*T3_4*T4_5*T5_T
#print("\n\n",TB_T)

#print(T0_1)
#print("\n",T1_2)
#print("\n",T2_3)
#print("\n",T3_4)
#print("\n",T4_5)
#print("\n",T5_T)

#Visualisation ||===========================================

origin = np.array([0,0,0])                #define origin

#Define frames

FB = np.eye(3)
print(FB)

XB = FB[:,0]
YB = FB[:,1]
ZB = FB[:,2]









