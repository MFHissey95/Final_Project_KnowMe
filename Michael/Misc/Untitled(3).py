for nm in allFiles:
  from tensorflow.keras.preprocessing import image
  from tensorflow.keras.preprocessing.image import img_to_array
  image_size = (28, 28)
  im = image.load_img(nm, target_size=image_size, color_mode="grayscale")
  print(im)
  # Convert the image to a numpy array 
  image = img_to_array(im)
  print(image.shape)
  # Scale the image pixels by 255 (or use a scaler from sklearn here)
  image /= 255
  
  # Flatten into a 1x28*28 array
  img = image.flatten().reshape(-1, 28*28)
  print(img.shape)

  plt.imshow(img.reshape(28, 28), cmap=plt.cm.Greys)

  # Invert the pixel values to match the original data
  img = 1 - img
  plt.imshow(img.reshape(28, 28), cmap=plt.cm.Greys)

  # Make predictions
  print(model.predict_classes(img))
