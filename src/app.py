import streamlit as st
import torch
from PIL import Image
import config
from torchvision import transforms

class_names = ['with_mask','without_mask']
def predict(file):

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = torch.load(config.MODEL_SAVE_PATH,map_location=torch.device('cpu'))
    # image = Image.open(file)
    img = preprocess_image(file)
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


def main():
    st.title("Face Mask Detection")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        label = predict(image)
        if label==1:
            st.error(f'Predicted Label: {class_names[label]}')
        else:
            st.success(f'Predicted Label: {class_names[label]}')



if __name__ == '__main__':
    main()

