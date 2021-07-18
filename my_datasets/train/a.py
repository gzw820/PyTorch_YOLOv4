
#show_pkl.py
 
import pickle
path='data.pkl'   #path='/root/……/aus_openface.pkl'   pkl文件所在路径
	   
f=open(path,'rb')
data=pickle.load(f)
 
print(data)
print(len(data))


