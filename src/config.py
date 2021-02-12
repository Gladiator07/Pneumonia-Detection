# This script has all the configurations for the dataset

import os

DATA_DIR = "/root/input/chest_xray"

TRAIN_P_DIR = os.path.join(DATA_DIR, "train/PNEUMONIA")
TRAIN_N_DIR = os.path.join(DATA_DIR, "train/NORMAL")

TEST_P_DIR = os.path.join(DATA_DIR, "test/PNEUMONIA")
TEST_N_DIR = os.path.join(DATA_DIR, "test/NORMAL")

VALID_P_DIR = os.path.join(DATA_DIR, "test/PNEUMONIA")
VALID_N_DIR = os.path.join(DATA_DIR, "test/NORMAL")


BATCH_SIZE = 16