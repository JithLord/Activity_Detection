# Activity_Detection_Python


You can run the program on colab.research.google.com
Click runtime and change runtime type to GPU or TPU for faster processing

Parameters You need to change either sequentially or parallely:
- [ ] - img_height it should always be less than 500 and greater than 150
- [ ] - img_width it should always be less than 500 and greater than 150
- [ ] - batch_size
- [ ] - The set of parameters in training_datagen = ImageDataGenerator (Please do not remove rescale=1./255)
- [ ] - model = tf.keras.models.Sequential part always keep the first line and last 3 lines as it is, the parameters you can add or remove
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
- [ ] - The parameters in model.compile() like the loss function and the optimizer again they are on the tensorflow's official website, also try to verify different parameters like learning rate
- [ ] - In model.fit() try to vary the number of epochs, steps per epoch and stuff, verbose is one of the two values always


## Some resources you can use:
- [ ] - https://www.tensorflow.org/tutorials/keras/overfit_and_underfit
- [ ] - https://www.tensorflow.org/tutorials/keras/save_and_load
- [ ] - https://www.tensorflow.org/tutorials/images/classification (Super useful)
- [ ] - https://www.tensorflow.org/tutorials/images/transfer_learning
- [ ] - https://www.tensorflow.org/api_docs/python/tf/keras/losses
- [ ] - https://www.tensorflow.org/api_docs/python/tf/keras/layers
