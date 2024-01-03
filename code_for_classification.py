from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np
def classify_image(file_path):
    model = load_model('mymodel5.h5')
    img_path = file_path
    img = image.load_img(img_path, target_size=(224, 224))  # Adjust target_size according to your model
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = img_array.reshape((1,) + img_array.shape)  
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    mylst=["dandelion", "daisy", "sunflower", "tulip", "rose"]
    return mylst[predicted_class]
