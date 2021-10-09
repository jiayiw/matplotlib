import matplotlib.pyplot as plt

x=[0,200,400,800,1200,1600,2000,2400,2800,3200,3600]
y=[20,18,16,14,12,10,8,6,4,2,0]
plt.xticks([0,400,800,1200,1600,2000,2400,2800,3200,3600])
plt.yticks([20,18,16,14,12,10,8,6,4,2,0])
#plt.xlim(0,3600)
#plt.ylim(0,20)
plt.margins(0,0)
#plt.subplots_adjust(top=1,bottom=0,left=0,right=1,hspace=0,wspace=0) 
plt.plot(x,y,label='总需求曲线',linestyle='-',color='green')
plt.scatter(x,y,s=15,edgecolor='pink',c=y,cmap=plt.cm.cool)
plt.xlabel('Q')
plt.ylabel('P',rotation=0)
plt.savefig("test1.png")

