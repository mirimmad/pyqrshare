import sys, os, zipfile, tempfile


FINAL_PATH = ''


def zipdir(path, ziph):
	for root, _dir, files in os.walk(path):
		for file in files:
			ziph.write(os.path.join(root, file))


def set_file_to_serve(path):
	global FINAL_PATH
	if os.path.isfile(path):
		FINAL_PATH = path
	elif os.path.isdir(path):
		tempdir = tempfile.mkdtemp()
		temp_path = tempdir + tempdir.split('/')[1]+'.zip'
		zipf = zipfile.ZipFile(temp_path, 'w', zipfile.ZIP_DEFLATED)
		zipdir(path, zipf)
		zipf.close()
		FINAL_PATH = temp_path
		return
	else:
		sys.exit("Not a valid path")
