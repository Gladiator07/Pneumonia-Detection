#!/bin/bash

"""
This script will set your kaggle api-key to the api and download the data
and arange it in folders
"""

# Put your Kaggle api key path here
kaggle_api_key_path = /content/drive/MyDrive/Kaggle/kaggle.json

# This snippet will install kaggle api and connect your api-key to it
pip install -q kaggle
mkdir -p ~/.kaggle
cp /content/drive/MyDrive/Kaggle/kaggle.json ~/.kaggle/
cat ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json

# This snippet will download the data in root folder and arange it in
# train test val folders

cd ~/.
kaggle datasets download -d paultimothymooney/chest-xray-pneumonia
mkdir input
mv chest-xray-pneumonia.zip input/
cd input/
unzip chest-xray-pneumonia.zip
rm chest-xray-pneumonia.zip
cd chest_xray/
rm -rf chest_xray/ __MACOSX/
