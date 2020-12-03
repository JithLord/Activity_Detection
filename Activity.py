import cv2
import numpy as np
from PIL import Image, ImageOps
from tensorflow.keras import models
import tensorflow as tf
from datetime import datetime

#Load the saved model
model = models.load_model('activity4.h5')
video = cv2.VideoCapture(0)
class_names=["Control","Sitting","Walking on Stairs","Standing","Sleeping","Walking"]
# freq
while True:
        _, frame = video.read()
        image = Image.fromarray(frame, 'RGB')
        size = (150, 150)
        data = np.ndarray(shape=(1, 150, 150, 3), dtype=np.float32)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
        data[0] = normalized_image_array

        prediction = model.predict(data)
        score = tf.nn.softmax(prediction[0])
        print(datetime.now(),class_names[np.argmax(score)])

        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)

        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()