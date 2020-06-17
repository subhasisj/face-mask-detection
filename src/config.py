import os

EPOCHS = 15
MODEL_SAVE_PATH = os.path.join('..','saved_models','facemaskdetection_new_mask_types.pth')
BATCH_SIZE = 32
TRAINING_DATA = os.path.join('data','train')
TESTING_DATA = os.path.join('data','test')