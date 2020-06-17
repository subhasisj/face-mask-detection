import os

EPOCHS = 15
MODEL_SAVE_PATH = os.path.join('Saved_Models','facemaskdetector.pth')
BATCH_SIZE = 32
TRAINING_DATA = os.path.join('data','train')
TESTING_DATA = os.path.join('data','test')