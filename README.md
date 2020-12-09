# Activity_Detection
This repository uses tensorflow to train on 4268 Non copyrighted images to classify into 6 different categories Sitting, Standing, Walking, Walking on Stairs and Control.

## IMPORTANT
Feel free to use the code, make sure you give us credits everytime you use the code.
## Dataset
Dataset divided into 6 categories of 150x150x3 ie the image of size 150x150 and a 3 channel(RGB). Category Control used to prevent Random images to be classified into any of the remaining 5 categories. Use of Augmentation to have more number of images to train the model. The dataset involved humans of various backgrounds, ages, skin tone, time of day.

## Code
Using InceptionV3 transfer learning model, along with mixed7 layer, 1024 neuron Selu with activation, 0.1 Dropout, 512 neuron with Selu activation, 0.1 dropout and 6 Neuron with softmax Activation.
Use of RMSprop optimizer with learning rate 0.0001 and loss function as categorical crossentropy.

## Important
You can run this program on colab.research.google.com with a TPU or GPU for faster processing.
THe code is attached here in .ipynb format, just copy the code to the colab website.
Click runtime and change runtime type to GPU or TPU for faster processing

## Download the .h5 model
https://we.tl/t-HBscIiHwov

## For loading images from your drive:
```
  from google.colab import drive
  drive.mount('/content/drive')
```
or you could do this and also specify the exact folder where you want it to take from: 


![image](https://user-images.githubusercontent.com/45201620/100517127-92afd700-31ae-11eb-9bf1-8ecf00e0f08b.png)

Then select this icon:
![image](https://user-images.githubusercontent.com/45201620/100517194-06ea7a80-31af-11eb-9353-f296f07643ea.png)


![image](https://user-images.githubusercontent.com/45201620/100517198-0f42b580-31af-11eb-942e-68468d3aa327.png)


Then copy the filepath


![image](https://user-images.githubusercontent.com/45201620/100517241-3e592700-31af-11eb-93f7-fc90a6e2a80b.png)



## Please feel free to open any issues

## Some resources you can use to improve your model:
1.      https://www.tensorflow.org/tutorials/keras/overfit_and_underfit
1.      https://www.tensorflow.org/tutorials/keras/save_and_load
1.      https://www.tensorflow.org/tutorials/images/classification (Super useful)
1.      https://www.tensorflow.org/tutorials/images/transfer_learning
1.      https://www.tensorflow.org/api_docs/python/tf/keras/losses
1.      https://www.tensorflow.org/api_docs/python/tf/keras/layers

## The LiveClassifier.py file can be used to classify images from a webcam or any camera.
