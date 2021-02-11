import os
import config

import numpy as np
import pandas as pd


np.random.seed(42)

TRAIN_P = os.listdir(config.TRAIN_P_DIR)
TRAIN_N = os.listdir(config.TRAIN_N_DIR)

VALID_P = os.listdir(config.VALID_P_DIR)
VALID_N = os.listdir(config.VALID_N_DIR)

TEST_P = os.listdir(config.TEST_P_DIR)
TEST_N = os.listdir(config.TEST_N_DIR)

TRAIN_DATA = []
TEST_DATA = []
VAL_DATA = []

# 1 ==> Pneumonia, 0 ==> Normal

for i in TRAIN_P:
    TRAIN_DATA.append((i, 1))

for i in TRAIN_N:
    TRAIN_DATA.append((i, 0))

for i in VALID_P:
    VAL_DATA.append((i, 1))

for i in VALID_N:
    VAL_DATA.append((i, 0))

for i in TEST_P:
    TEST_DATA.append((i, 1))

for i in TEST_N:
    TEST_DATA.append((i, 0))


# Transform list to Pandas DataFrame

TRAIN_DATA = pd.DataFrame(TRAIN_DATA, columns=['image', 'label'], index=None)
TRAIN_DATA = TRAIN_DATA.sample(frac=1, random_state=15).reset_index(drop=True)

VAL_DATA = pd.DataFrame(VAL_DATA, columns=['image', 'label'], index=None)
VAL_DATA = VAL_DATA.sample(frac=1, random_state=15).reset_index(drop=True)

TEST_DATA = pd.DataFrame(TEST_DATA, columns=['image', 'label'], index=None)
TEST_DATA = TEST_DATA.sample(frac=1, random_state=15).reset_index(drop=True)


print(type(TEST_DATA))
print(type(TEST_DATA.iloc[0, :].image))

# As validation data has only 16 images we will concat it with training data

full_data = pd.concat([TRAIN_DATA, VAL_DATA], ignore_index=True)
full_data = full_data.sample(frac=1, random_state=17).reset_index(drop=True)

msk = np.random.rand(len(full_data)) < 0.9

train_df = full_data[msk].reset_index()
val_df = full_data[~msk].reset_index() 