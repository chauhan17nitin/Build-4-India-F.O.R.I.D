from keras import layers
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

def predict():
  from keras.utils.generic_utils import CustomObjectScope
  with CustomObjectScope({'relu6': layers.ReLU(6.),'DepthwiseConv2D':layers.DepthwiseConv2D}):
      model = load_model('models/design1.h5')

  model.compile(loss='categorical_crossentropy',
                optimizer='Adam',
                metrics=['accuracy'])

  def load_image(img_path, show=False):

      img = image.load_img(img_path, target_size=(224, 224))
      img_tensor = image.img_to_array(img)                    # (height, width, channels)
      img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
      img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

      return img_tensor
    
  #img_path = 'C:/Users/Ferhat/Python Code/Workshop/Tensoorflow transfer learning/blue_tit.jpg'
  img_path = '3.JPG'
  new_image = load_image(img_path)

  pred = model.predict(new_image)
  pred = np.argmax(pred)
  print ("the class is: " + str(pred))
  return pred
  
  
predict()
# import h5py

# f = h5py.File('models/design_final.h5', 'r')
# print(f.attrs.get('keras_version'))
