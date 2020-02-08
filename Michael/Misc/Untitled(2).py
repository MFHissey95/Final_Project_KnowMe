### Import a Custom Image
from google.colab import files

uploaded = files.upload()
allFiles = []
for fn in uploaded.keys():
  allFiles.append(fn)
  print('User uploaded file "{name}" with length {length} bytes'.format(name=fn, length=len(uploaded[fn])))
