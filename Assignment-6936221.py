# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 07:03:25 2023

@author: Mimi
"""

"MIRIAM ENNIM" #my github account is MiriamEnnim
"CIVIL ENGINEERING 2"
"COMPUTER APPLICATIONS IN CIVIL ENGINEERING"
"6936221"
import numpy as np
#question a
L=12 #length of beam in m
w=10 #load intensity on beam in KN/m
x=0 #distance
M=((w*((-6*x**2)+6*L*x-L**2)/12)) #calculating bending moment at this distance
V=(w*(L/2-x)) #calculating shear force at this distance
FirstM='The bending moment when x is zero is '
FirstV='The shear force when x is zero is '
print('a. '+FirstM+str(M))
print(FirstV+str(V))
x=L #distance
M=((w*((-6*x**2)+6*L*x-L**2)/12)) #calculating bending moment at this distance
V=(w*(L/2-x)) #calculating shear force at this distance
SecondM='The bending moment when x is L is '
SecondV='The shear force when x is L is '
print(SecondM+str(M))
print(SecondV+str(V))
#question b
"When the bending moment is zero, the expression obtained is -5*x**2+60x-120"
#from the expression and using the quadratic formula
a=-5
b=60
c=-120
discriminant=b**2-(4*a*c)
#solutions to the formula indicating the positions at which bending moment is 0
Root1=int(-b+np.sqrt(discriminant))/(-2*a)
Root2=int(-b-np.sqrt(discriminant))/(-2*a)
print()
print("b. The distances at which the bending moment will be zero are {0} and {1}".format(Root1,Root2))
#question c
"When the shear force is zero, the expression obtained is 60-10x"
SF=str(6)
print()
print('c. The shear force will be 0 when x is equal to '+ SF )
#question d
E=0 #initial variable
F=0.01 #interval
G=L+F #Final 
Discretize=np.arange(E,F,G) #array discretizing the span
M=((w*((-6*Discretize**2)+6*L*Discretize-L**2)/12))
print()
print('d. Using the initialized variable, the bending moment at each step in the array is '+str(M))
#question e
#for shear force at 10mm interval
V=w*(L/2-Discretize)
print()
print('e. Using the initialized varible, the shear force at each step is '+str(V))
#question f
Absolute=abs(M) #absolute value of bending moment array
MinValue=min(Absolute) #minimum absolute value
"The expression for when the bending moment is minimum is x**2-Lx+(L**2/6)+(2*MinValue)/w = 0"
#comparing to the standard quadratic
a=1
b=-L
c=(L**2/6)+(2*MinValue)/w
#solving the equation using the quadratic formula
Root3=int((-b+np.sqrt(discriminant))/(-2*a))
Root4=int((-b-np.sqrt(discriminant))/(-2*a))
print()
print('f. The points along L for which the bending moment value is minimum are {0} and {1}'.format(Root3,Root4))
#question g
relativeError1=int(((Root1-Root3)/Root1)*100)
relativeError2=int(((Root4-Root2)/Root4)*100)
print()
print('g. The relative errors between the estimated points of contraflexure are {0}% and {1}%'.format(relativeError1, relativeError2))
#question h
MaxMoment=max(M) #maximum bending moment
# the expression for maximum moment is x**2-Lx+(L**2/6)+(2*MaxMoment)/w = 0
s=1
t=-L
u=(L**2/6)+(2*MaxMoment)/w
#solving the equation using the quadratic formula
discriminant2=(-L)**2-4*s*u
Root5=int((-t+np.sqrt(discriminant2))/(-2*s))
Root6=int((-t-np.sqrt(discriminant2))/(-2*s))
print()
print('h. The points at which the maximum bending moment value occur are {0} and {1}'.format(Root5,Root6))
MinMoment=min(M) #minimum bending moment
# the expression for minimum moment is x**2-Lx+(L**2/6)+(2*MinMoment)/w = 0
v=1
z=-L
q=(L**2/6)+(2*MinMoment)/w
#solving the equation using the quadratic formula
discriminant3=(z)**2-4*v*q
Root7=int((-z+np.sqrt(discriminant3))/(-2*v))
Root8=int((-z-np.sqrt(discriminant3))/(-2*v))
print()
print('h. The points at which the minimum bending moment value occur are {0} and {1}'.format(Root7,Root8))