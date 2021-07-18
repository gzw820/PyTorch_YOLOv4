1, 训练过程：
在PyTorch_YOLOV4-master目录下新建一个my_datasets文件夹，内容如下：test、train、valid文件夹以及data.yaml。在每个文件夹下存放images，labels文件夹。例如, train文件夹下有images，labels文件夹。
data.yaml内容为：
train: ./my_datasets/train/images
val: ./my_datasets/valid/images
test: ./my_datasets/test/images

nc: 1  #这里修改类别数
names: ['fire']  #这里修改类别名。
*******最重要的一步：修改cfg里面的配置文件,修改类别数，和yolo上面一层的filters个数（类别数+5）乘上3。
训练指令：python train.py --weights yolov4-pacsp-s.pt --batch-size 16 --img 640 640 --data my_datasets/data.yaml --cfg cfg/yolov4-pacsp-s.cfg（这里的pt文件在百度网盘里面放着，我的资源/weights/）
2，测试阶段：python test.py --img 640 --conf 0.001 --batch 8 --device 0 --data --cfg cfg/yolov4-pacsp-s.cfg --weights yolov4-pacsp-s.pt 
注意：这里需要注意标签txt文件不能有空的，否则训练过程中会出现梯度爆炸！！！


