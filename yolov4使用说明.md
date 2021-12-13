## 1、推理检测：

**在pycharm终端下命令行运行：python detect.py --weights weights/yolov4-pacsp-s.pt --source 0 --cfg cfg/yolov4-pacsp-s.cfg --device 0** 

说明：

--weights weights/yolov4-pacsp-s.pt 代表输入模型权重的路径，这里是相对路径，训练好的pt文件在weights文件夹下

--source 0 代表输入源头是0号摄像头，一般机器内置的摄像头是0号，如果外接usb摄像头则选择1，例如 --source 1；如果选择本地视频或者图片，则同样的输入其路径，例如 --source test_source/2.jpg

--cfg cfg/yolov4-pacsp-s.cfg 代表配置文件的设置，这里cfg也是相对路径，yolov4-pacsp-s.cfg 是具体的配置文件

--device 0 代表使用的gpu编号，0代表使用0号gpu

注：当前yolov4代码文件夹路径为：D:PyTorch_YOLOv4-master/PyTorch_YOLOv4-master

## 2、自定义数据集训练

### 2.1重新自定义数据集

如果想重新训练模型，例如重新训练一个仅仅检测船舶的模型，则需要自定义数据集重新训练。具体做法如下：

​		在PyTorch_YOLOV4-master目录下新建一个my_datasets文件夹，内容如下：test、train、valid文件夹以及data.yaml。在每个文件夹下存放images，labels文件夹。例如, train、valid和test文件夹均有下有images，labels文件夹，images是训练集数据集图片, labels是标注过的标签，txt标注格式。
data.yaml内容为：
train: ./my_datasets/train/images
val: ./my_datasets/valid/images
test: ./my_datasets/test/images

例如下图：

<img src="C:\Users\aaaac\AppData\Roaming\Typora\typora-user-images\image-20211110135502125.png" alt="image-20211110135502125" style="zoom:200%;" />



<img src="C:\Users\aaaac\AppData\Roaming\Typora\typora-user-images\image-20211110135613933.png" alt="image-20211110135613933" style="zoom: 200%;" />

<img src="C:\Users\aaaac\AppData\Roaming\Typora\typora-user-images\image-20211110140900103.png" alt="image-20211110140900103" style="zoom:200%;" />

### 2.2 修改配置文件

 **修改cfg路径下的配置文件，以yolov4-pacsp-s.cfg配置为例**

<img src="C:\Users\aaaac\AppData\Roaming\Typora\typora-user-images\image-20211110140521105.png" alt="image-20211110140521105" style="zoom:200%;" />

### 2.3 训练阶段

**训练阶段，在终端命令行输入指令：**python train.py --weights weights/yolov4-pacsp-s.pt --batch-size 16 --img 640 640 --data my_datasets/data.yaml --cfg cfg/yolov4-pacsp-s.cfg
**测试阶段：**python test.py --img 640 --conf 0.001 --batch 8 --device 0 --data  my_datasets/data.yaml  --cfg cfg/yolov4-pacsp-s.cfg --weights weights/yolov4-pacsp-s.pt (评测指标使用)

