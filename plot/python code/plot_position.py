import getData
import matplotlib.pyplot as plt

hight_node1 = getData.getData('2nd_node1.csv',4)
gp_7y_node1 = getData.getData('2nd_node1.csv',22)

hight_node2 = getData.getData('2nd_node2.csv',4)
gp_7y_node2 = getData.getData('2nd_node2.csv',22)

hight_node3 = getData.getData('2nd_node3.csv',4)
gp_7y_node3 = getData.getData('2nd_node3.csv',22)

hight_node4 = getData.getData('2nd_node4.csv',4)
gp_7y_node4 = getData.getData('2nd_node4.csv',22)

print len(hight_node1)
print hight_node1
print len(gp_7y_node1)
print gp_7y_node1

print len(hight_node2)
print hight_node2
print len(gp_7y_node2)
print gp_7y_node2

print len(hight_node3)
print hight_node3
print len(gp_7y_node3)
print gp_7y_node3

print len(hight_node4)
print hight_node4
print len(gp_7y_node4)
print gp_7y_node4


#D,R,L,C in m,r,g,b color
plt.subplot(2,2,1)
plt.scatter(gp_7y_node1,hight_node1,s=66,facecolors='none',edgecolors='m');
plt.axis([-10,530,60,90])
plt.xlabel('sum_7yr_GP')
plt.ylabel('Height')
plt.subplot(2,2,2)
plt.scatter(gp_7y_node2,hight_node2,s=66,facecolors='none',edgecolors='r');
plt.axis([-10,530,60,90])
plt.xlabel('sum_7yr_GP')
plt.ylabel('Height')
plt.subplot(2,2,3)
plt.scatter(gp_7y_node3,hight_node3,s=66,facecolors='none',edgecolors='g');
plt.axis([-10,530,60,90])
plt.xlabel('sum_7yr_GP')
plt.ylabel('Height')
plt.subplot(2,2,4)
plt.scatter(gp_7y_node4,hight_node4,s=66,facecolors='none',edgecolors='b');
plt.axis([-10,530,60,90])
plt.xlabel('sum_7yr_GP')
plt.ylabel('Height')
#plt.plot(gp_7y_node2,age_node2,'ro')
#plt.plot(gp_7y_node3,age_node3,'bo')
#plt.plot(gp_7y_node4,age_node4,'yo')
#plt.axis([-10,500,15,25])

plt.show()