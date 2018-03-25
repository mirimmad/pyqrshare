from setuptools import setup

setup(name='pyqrshare',
      version='1.0',
      description='Lets you transfer files and directories from your computer to your mobile device by scanning a QR code right from the terminal',
      classifiers=[
        'Development Status :: Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: File Sharing :: QRCode',
      ],
      entry_points = {
        'console_scripts': ['pyqrshare=pyqrshare.command_line:main'],
      },
      url='http://github.com/mirimmad/pyqrshare',
      author='Mir Immad',
      author_email='mirimmad17@gmail.com',
      license='MIT',
      packages=['pyqrshare'],
      install_requires=[
          'netifaces',
          'Flask',
          'pyqrcode'
      ],
      zip_safe=False)
