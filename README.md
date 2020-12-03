# Activity_Detection_Python


You can run the program on colab.research.google.com
THe code is attached here in .ipynb format, just copy the code to the colab website.
Click runtime and change runtime type to GPU or TPU for faster processing
## Download the .h5 model
https://we.tl/t-HBscIiHwov

## Super Important
For loading images from your drive:
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



## Parameters You need to change either sequentially or parallely:
1.      img_height it should always be less than 500 and greater than 150
1.      img_width it should always be less than 500 and greater than 150
1.      batch_size
1.      The set of parameters in training_datagen = ImageDataGenerator (Please do not remove rescale=1./255)
1.      model = tf.keras.models.Sequential part always keep the first line and last 3 lines as it is, the parameters you can add or remove
                tf.keras.layers.Conv2D(16, (3,3), padding='same'),
                tf.keras.layers.MaxPooling2D(2, 2),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.Conv2D(32, (3,3), padding='same'),
                tf.keras.layers.MaxPooling2D(2, 2),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.Conv2D(64, (3,3), padding='same'),
                tf.keras.layers.MaxPooling2D(2, 2),
                tf.keras.layers.BatchNormalization(),
                tf.keras.layers.Conv2D(128, (3,3)),
                tf.keras.layers.MaxPooling2D(2, 2),
                tf.keras.layers.BatchNormalization()
       Search for more stuff on the tensorflow website by specfying the tf.keras.models keyword
       If you ever get an error just search for the exact same text online eg
       "OSError: Could'nt do this because of that" From the error part only
1.      The parameters in model.compile() like the loss function and the optimizer again they are on the tensorflow's official website, also try to verify different parameters like learning rate
1.      In model.fit() try to vary the number of epochs, steps per epoch and stuff, verbose is one of the two values always


## Some resources you can use:
1.      https://www.tensorflow.org/tutorials/keras/overfit_and_underfit
1.      https://www.tensorflow.org/tutorials/keras/save_and_load
1.      https://www.tensorflow.org/tutorials/images/classification (Super useful)
1.      https://www.tensorflow.org/tutorials/images/transfer_learning
1.      https://www.tensorflow.org/api_docs/python/tf/keras/losses
1.      https://www.tensorflow.org/api_docs/python/tf/keras/layers



## How your result should look like
##### The place where you mounted the google drive will have the "model1.h5" file, send that to me with a plot of accuracy and loss plots
![image](https://user-images.githubusercontent.com/45201620/100517523-0a7f0100-31b1-11eb-80d2-b36984e141ad.png)
![image](https://user-images.githubusercontent.com/45201620/100517529-179bf000-31b1-11eb-823b-25ae40c4c5e4.png)
![image](https://user-images.githubusercontent.com/45201620/100517546-30a4a100-31b1-11eb-9c25-4e6cd52a0527.png)
![image](https://user-images.githubusercontent.com/45201620/100517568-6b0e3e00-31b1-11eb-95c4-17f5c5bcdc50.png)
![image](https://user-images.githubusercontent.com/45201620/100517576-76616980-31b1-11eb-989e-f1a51a4a574a.png)

##### Should'nt have this like sudden increase or decrease
![image](https://user-images.githubusercontent.com/45201620/100517536-271b3900-31b1-11eb-8312-668ddb48f885.png)
##### This could be a sign of overfitting:
![image](https://user-images.githubusercontent.com/45201620/100517559-5631aa80-31b1-11eb-92e8-13704886126d.png)


## Important:
The model will automatically stop WITHOUT ERRORS automatically after the training and validation accuracies are above 0.8 
If it does stop automatically save the model with 
```
  model.save("model1.h5")
```
