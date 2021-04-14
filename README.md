# Activity_Detection
This repository uses tensorflow to train on 4268 Non copyrighted images obtained after scraping duckduckgo searches to classify live using the camera into 6 different categories Sitting, Standing, Walking, Walking on Stairs and Control.

## IMPORTANT
Feel free to use the code, make sure you give us credits everytime you use the code.
## Dataset
Dataset divided into 6 categories of 150x150x3 ie the image of size 150x150 and a 3 channel(RGB). Category Control used to prevent Random images to be classified into any of the remaining 5 categories. Use of Augmentation to have more number of images to train the model. The dataset involved humans of various backgrounds, ages, skin tone, time of day. </br ></br >
 &nbsp; &nbsp;   &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <img src="https://user-images.githubusercontent.com/45201620/113389040-fa6c6d80-93ac-11eb-974e-ad3112eba8c3.png" width="60%"></img>

*My dataset is now available to download for free on kaggle www.kaggle.com/jithinnambiarj/human-activity-recognition-dataset.* </br>
**Please do give me credits everytime you use it.**


## Code
Using InceptionV3 transfer learning model, along with mixed7 layer, 1024 neuron Selu with activation, 0.1 Dropout, 512 neuron with Selu activation, 0.1 dropout and 6 Neuron with softmax Activation.
Use of RMSprop optimizer with learning rate 0.0001 and loss function as categorical crossentropy.
</br >
</br >
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <img src="https://user-images.githubusercontent.com/45201620/113389135-1f60e080-93ad-11eb-916b-c88b206104ee.png" width="60%"></img>
</br >

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Block Diagram of the Project </br >

<img src="https://user-images.githubusercontent.com/45201620/113389310-736bc500-93ad-11eb-80a7-88f476845f52.png" width="45%"></img> <img src="https://user-images.githubusercontent.com/45201620/113389339-7f578700-93ad-11eb-9f15-39aedcc44f16.png" width="45%"></img> 
</br >

&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Training Accuracy  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Training Loss

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
  1. Runtime -> Change runtime type -> GPU or TPU
  2. Click on Files from the left toolbar
  3. Click Mount drive
  4. Copy the path of the dataset folder (and assign them to the train_dir and val_dir)


### Please feel free to open any issues

## Some resources you can use to improve your model:
1.      https://www.tensorflow.org/tutorials/keras/overfit_and_underfit
1.      https://www.tensorflow.org/tutorials/keras/save_and_load
1.      https://www.tensorflow.org/tutorials/images/classification (Super useful)
1.      https://www.tensorflow.org/tutorials/images/transfer_learning
1.      https://www.tensorflow.org/api_docs/python/tf/keras/losses
1.      https://www.tensorflow.org/api_docs/python/tf/keras/layers

## The LiveClassifier.py file can be used to classify images from a webcam or any camera.
