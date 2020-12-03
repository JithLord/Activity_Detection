import os

from tensorflow.keras import layers
from tensorflow.keras import Model
!wget --no-check-certificate \
    https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5 \
    -O /tmp/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5
  
from tensorflow.keras.applications.inception_v3 import InceptionV3

local_weights_file = '/tmp/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'

pre_trained_model = InceptionV3(input_shape = (150, 150, 3), 
                                include_top = False, 
                                weights = None)

pre_trained_model.load_weights(local_weights_file)

for layer in pre_trained_model.layers:
  layer.trainable = False
  
# pre_trained_model.summary()

last_layer = pre_trained_model.get_layer('mixed7')
print('last layer output shape: ', last_layer.output_shape)
last_output = last_layer.output

from tensorflow.keras.optimizers import RMSprop

# Flatten the output layer to 1 dimension
x = layers.Flatten()(last_output)
x = layers.Dense(1024, activation='selu')(x)
x = layers.Dropout(0.1)(x)                  
x = layers.Dense(512, activation='selu')(x) 
x = layers.Dropout(0.1)(x)                  
# Final Softmax layer for classification
x = layers.Dense(6, activation='softmax')(x)           

model = Model( pre_trained_model.input, x) 

model.compile(optimizer = RMSprop(lr=0.0001), 
              loss = 'categorical_crossentropy', 
              metrics = ['acc'])

from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_dir = r"/content/drive/MyDrive/DatasetNew"
validation_dir = r"/content/drive/MyDrive/Validation"

# Add our data-augmentation parameters to ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255,
                                  rotation_range=10,
                                  width_shift_range=0.3,
                                  height_shift_range=0.3,
                                  # featurewise_std_normalization=True, 
                                  # samplewise_std_normalization=True,
                                  brightness_range=(0.2,0.5),
                                  # shear_range=0.2,
                                  # zoom_range=0.2,
                                  horizontal_flip=True,
                                  fill_mode='nearest')

# Note that the validation data should not be augmented!
# test_datagen = ImageDataGenerator( rescale = 1.0/255. )

# Flow training images in batches of 20 using train_datagen generator
train_generator = train_datagen.flow_from_directory(train_dir,
                                                    batch_size = 20,
                                                    shuffle="True",
                                                    class_mode = 'categorical', 
                                                    target_size = (150, 150))     

# Flow validation images in batches of 20 using test_datagen generator
validation_generator =  train_datagen.flow_from_directory(validation_dir,
                                                          batch_size  = 20,
                                                          shuffle="True",
                                                          class_mode  = 'categorical', 
                                                          target_size = (150, 150))


import tensorflow as tf
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
class myCallback(tf.keras.callbacks.Callback):
      def on_epoch_end(self, epoch, logs={}):
          if (logs.get('acc')>0.82):
            self.model.stop_training = True
callbacks=myCallback()
history = model.fit(
            train_generator,
            validation_data = validation_generator,
            steps_per_epoch = 20,
            epochs = 100,
            validation_steps = 20,
            verbose = 1,callbacks=[callbacks])
model.save("activity34.h5")
import matplotlib.pyplot as plt
acc = history.history['acc']
# val_acc = history.history['val_acc']
loss = history.history['loss']
# val_loss = history.history['val_loss']

epochs = range(len(acc))

model.save("activity4.h5")
plt.plot(epochs, acc, 'r', label='Training accuracy')
plt.title('Training Accuracy')
plt.legend(loc=0)
plt.figure()
plt.show()

model.save("activity4.h5")
plt.plot(epochs, loss, 'r', label='Training Loss')
plt.title('Training Loss')
plt.legend(loc=0)
plt.figure()
plt.show()

