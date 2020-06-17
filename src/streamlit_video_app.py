import streamlit as st
import cv2 as cv
from PIL import Image
from torchvision import transforms
import torch
import config


class_names = ['with_mask','without_mask']
def predict(file):
    image = cv.cvtColor(file, cv.COLOR_BGR2RGB)
    im = Image.fromarray(image)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = torch.load(config.MODEL_SAVE_PATH,map_location=torch.device('cpu'))
    # image = Image.open(file)
    img = preprocess_image(im)
    img = img.unsqueeze_(0)
    img = img.float()
    model.to(device)
    model.eval()
    output = model(img)
    _, predicted = torch.max(output, 1)
    return predicted[0]

def preprocess_image(img):

    image_transforms = transforms.Compose([
                                        transforms.Resize(256),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                                        ])
    
    return image_transforms(img)


@st.cache(allow_output_mutation=True)
def get_cap():
    return cv.VideoCapture(0)

cap = get_cap()

frameST = st.empty()


while True:
    ret, frame = cap.read()
    height,width = frame.shape[:2]
    label = predict(frame)
    if label==1:
            st.error(f'Predicted Label: {class_names[label]}')
    else:
        st.success(f'Predicted Label: {class_names[label]}') 
    # cv2.putText(frame,str(class_names[label]),(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
    # cv2.imshow('frame',frame)
    # Stop the program if reached end of video
    if not ret:
        print("Done processing !!!")
        cv.waitKey(3000)
        # Release device
        cap.release()
        break

    frameST.image(frame, channels="BGR")

    class_names = ['with_mask','without_mask']
