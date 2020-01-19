from keras import layers
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import json
import glob as glob

def Predict():
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
  #img_path = 'captured_img/1_1.jpg'    
  images = glob.glob('captured_img/*.jpg')
  images.sort()
  pred_arr = []
  data = {}
  for im in images:
    new_image = load_image(im)
    pred = model.predict(new_image)
    pred = np.argmax(pred)
    pred_arr.append(pred)
    data = {'pred_arr': pred_arr}
    with open('send.json', 'w') as outfile:
      j = json.dump(data, outfile,indent=4)
    print ("the class for "+im+" is: " + str(pred))
  return pred_arr
  

#predict()
# import h5py

# f = h5py.File('models/design_final.h5', 'r')
# print(f.attrs.get('keras_version'))
