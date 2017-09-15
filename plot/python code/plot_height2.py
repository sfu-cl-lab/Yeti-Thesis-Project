import getData
import matplotlib.pyplot as plt

age_node1 = getData.getData('2nd_node1.csv',5)
gp_7y_node1 = getData.getData('2nd_node1.csv',23)

age_node2 = getData.getData('2nd_node2.csv',5)
gp_7y_node2 = getData.getData('2nd_node2.csv',23)

age_node3 = getData.getData('2nd_node3.csv',5)
gp_7y_node3 = getData.getData('2nd_node3.csv',23)

age_node4 = getData.getData('2nd_node4.csv',5)
gp_7y_node4 = getData.getData('2nd_node4.csv',23)

age_node5 = getData.getData('2nd_node5.csv',5)
gp_7y_node5 = getData.getData('2nd_node5.csv',23)

node1_top = getData.getData_String('2nd_node1.csv',1)[0]
node2_top = getData.getData_String('2nd_node2.csv',1)[0]
node3_top = getData.getData_String('2nd_node3.csv',1)[0]
node4_top = getData.getData_String('2nd_node4.csv',1)[0]
node5_top = getData.getData_String('2nd_node5.csv',1)[0]

age_node1_top = age_node1[:3]
age_node2_top = age_node2[:3]
age_node3_top = age_node3[:3]
age_node4_top = age_node4[:3]
age_node5_top = age_node5[:3]

gp_7y_node1_top = gp_7y_node1[:3]
gp_7y_node2_top = gp_7y_node2[:3]
gp_7y_node3_top = gp_7y_node3[:3]
gp_7y_node4_top = gp_7y_node4[:3]
gp_7y_node5_top = gp_7y_node5[:3]


x1_top = age_node1[:1][0]
x2_top = age_node2[:1][0]
x3_top = age_node3[:1][0]
x4_top = age_node4[:1][0]
x5_top = age_node5[:1][0]

y1_top = gp_7y_node1[:1][0]
y2_top = gp_7y_node2[:1][0]
y3_top = gp_7y_node3[:1][0]
y4_top = gp_7y_node4[:1][0]
y5_top = gp_7y_node5[:1][0]


print len(age_node1)
print age_node1
print len(gp_7y_node1)
print gp_7y_node1

print len(age_node2)
print age_node2
print len(gp_7y_node2)
print gp_7y_node2

print len(age_node3)
print age_node3
print len(gp_7y_node3)
print gp_7y_node3

print len(age_node4)
print age_node4
print len(gp_7y_node4)
print gp_7y_node4

print len(age_node5)
print age_node5
print len(gp_7y_node5)
print gp_7y_node5


plt.subplot(2,3,1)
plt.scatter(age_node1,gp_7y_node1,s=66,facecolors='none',edgecolors='m');
plt.scatter(age_node1_top,gp_7y_node1_top,s=66,marker=r'$\bullet$',label='Fluid-Cell',facecolors='k',edgecolors='k');
plt.annotate(node1_top,xy=(x1_top +0.02,y1_top+13), xytext=(x1_top+2.2,y1_top+77), arrowprops = dict(facecolor='black', shrink=0.02),)
plt.axis([65,85,-10,530])
plt.ylabel('sum_7yr_GP')
plt.xlabel('Height_node1')

plt.subplot(2,3,2)
plt.scatter(age_node2,gp_7y_node2,s=66,facecolors='none',edgecolors='r');
plt.scatter(age_node2_top,gp_7y_node2_top,s=66,marker=r'$\bullet$',label='Fluid-Cell',facecolors='k',edgecolors='k');
plt.annotate(node2_top,xy=(x2_top +0.02,y2_top+13), xytext=(x2_top+2.2,y2_top+77), arrowprops = dict(facecolor='black', shrink=0.02),)
plt.axis([65,85,-10,530])
plt.ylabel('sum_7yr_GP')
plt.xlabel('Height_node2')

plt.subplot(2,3,3)
plt.scatter(age_node3,gp_7y_node3,s=66,facecolors='none',edgecolors='g');
plt.scatter(age_node3_top,gp_7y_node3_top,s=66,marker=r'$\bullet$',label='Fluid-Cell',facecolors='k',edgecolors='k');
plt.annotate(node3_top,xy=(x3_top +0.02,y3_top+13), xytext=(x3_top+2.2,y3_top+77), arrowprops = dict(facecolor='black', shrink=0.02),)
plt.axis([65,85,-10,530])
plt.ylabel('sum_7yr_GP')
plt.xlabel('Height_node3')

plt.subplot(2,3,4)
plt.scatter(age_node4,gp_7y_node4,s=66,facecolors='none',edgecolors='b');
plt.scatter(age_node4_top,gp_7y_node4_top,s=66,marker=r'$\bullet$',label='Fluid-Cell',facecolors='k',edgecolors='k');
plt.annotate(node4_top,xy=(x4_top +0.02,y4_top+13), xytext=(x4_top+2.2,y4_top+77), arrowprops = dict(facecolor='black', shrink=0.02),)
plt.axis([65,85,-10,530])
plt.ylabel('sum_7yr_GP')
plt.xlabel('Height_node4')

plt.subplot(2,3,5)
plt.scatter(age_node5,gp_7y_node5,s=66,facecolors='none',edgecolors='c');
plt.scatter(age_node5_top,gp_7y_node5_top,s=66,marker=r'$\bullet$',label='Fluid-Cell',facecolors='k',edgecolors='k');
plt.annotate(node5_top,xy=(x5_top +0.02,y5_top+13), xytext=(x5_top+2.2,y5_top+77), arrowprops = dict(facecolor='black', shrink=0.02),)
plt.axis([65,85,-10,530])
plt.ylabel('sum_7yr_GP')
plt.xlabel('Height_node5')

plt.subplot(2,3,6)
plt.scatter(age_node1,gp_7y_node1,s=66,facecolors='none',edgecolors='m');
plt.scatter(age_node2,gp_7y_node2,s=66,facecolors='none',edgecolors='r');
plt.scatter(age_node3,gp_7y_node3,s=66,facecolors='none',edgecolors='g');
plt.scatter(age_node4,gp_7y_node4,s=66,facecolors='none',edgecolors='b');
plt.scatter(age_node5,gp_7y_node5,s=66,facecolors='none',edgecolors='c');
plt.axis([65,85,-10,530])
plt.ylabel('sum_7yr_GP')
plt.xlabel('Height_AllNode')


plt.show()