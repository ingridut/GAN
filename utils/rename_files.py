import os
import sys
from PIL import Image

directory = sys.argv[1]
img_type = sys.argv[2]
filenames = os.listdir(directory)

counter = 1
for filename in filenames: 
	file = directory + '/' + filename
	try:
		Image.open(file)
		new_name = img_type + '_' + str(counter) + '.' + filename.split('.')[-1]
		os.rename(file, directory + '/' + new_name)
		counter += 1
	except:
		print('Deleted ', file)
		os.remove(file)
