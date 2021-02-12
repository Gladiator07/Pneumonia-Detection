#!/bin/bash

"""
This script will set your kaggle api-key to Kaggle api, download data
and arrange it in train, val, test directories
"""

# Put your Kaggle api key path here
echo "Fetching your Kaggle API Key"
kaggle_api_key_path='/content/drive/MyDrive/Kaggle/kaggle.json'

# This snippet will install kaggle api and connect your api-key to it
echo "Installing Kaggle API..."
pip3 install -q kaggle
mkdir -p ~/.kaggle
echo "Setting up your Kaggle key to API..."
cp /content/drive/MyDrive/Kaggle/kaggle.json ~/.kaggle/
cat ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
echo "Kaggle API Key successfully linked !!!"

# This snippet will download the data in root folder and arange it in
# train test val folders

echo "Downloading Pneumonia Data at root directory..."
cd ~/.
kaggle datasets download -d paultimothymooney/chest-xray-pneumonia
mkdir input
mv chest-xray-pneumonia.zip input/
cd input/
echo "Unzipping the data...."
unzip chest-xray-pneumonia.zip
rm chest-xray-pneumonia.zip
echo "Cleaning up redundant folders"
cd chest_xray/
rm -rf chest_xray/ __MACOSX/
echo "Data downloaded successfully..."
