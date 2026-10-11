import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('model.h5')
st.set_page_config(page_title="Brain Disease Prediction", page_icon="🧠", layout='wide', initial_sidebar_state="collapsed")

# Class labels
class_labels = ['Haemorrhagic', 'Ischemic', 'Normal']

def load_and_predict(image):
    # Preprocess the image for prediction
    image = cv2.resize(image, (200, 200))  # Resize the image to match the input shape of the model
    image = np.expand_dims(image, axis=0)  # Add an extra dimension for batch size

    # Make predictions
    predictions = model.predict(image)
    predicted_class_idx = np.argmax(predictions)
    predicted_class = class_labels[predicted_class_idx]

    return predicted_class

def main():
    st.markdown(
        """
        <div style="text-align: center; color: blue; font-size: 32px; font-weight: bold;">
            MRI based Brain Disease Classification and Paralysis Prediction
        </div>
        """,
        unsafe_allow_html=True
    )
    col1, col2,col3= st.columns([1,6,1])
    uploaded_file = col2.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    st.markdown(
        """
        <style>
        /* Apply background image to the main content area */
        .main {
            background-image: url('https://www.shutterstock.com/image-photo/patient-brain-treatment-protection-concept-600nw-1996512854.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-color: rgba(255, 255, 255, 0.3);
            background-blend-mode: overlay;
        }
        </style>
        """,
        unsafe_allow_html=True
        )
    if uploaded_file is not None:
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)
        col1,col2,col3=st.columns([5,6,1])
        col2.image(image, caption="Uploaded Image.", width=200)
        col1,col2,col3=st.columns([6.3,6,1])
        if col2.button("Predict",type='primary'):
            predicted_class = load_and_predict(image)
            if predicted_class=='Haemorrhagic':
                col1, col2, col3 = st.columns([7, 6, 3])
                col2.markdown(f"<h2 style='color:red;'>Haemorrhagic</h2>", unsafe_allow_html=True)
                description = "A hemorrhagic stroke is a life-threatening condition that occurs when a blood vessel in the brain ruptures or leaks. This causes bleeding in or around the brain, which can damage brain cells and tissues. Hemorrhagic strokes are less common than ischemic strokes, but they are more severe and have a higher risk of death. There are two main types of hemorrhagic strokes: intracerebral hemorrhage and subarachnoid hemorrhage."
                st.markdown(
                    f"""
                    <div style="text-align: justify; padding: 10px; background-color: #f0e222; border-radius: 20px; border: 1.5px solid black; margin-bottom: 20px;">
                        <h2 style="color: #111df7; font-size: 20px;"><b>Disease Description:</b></h2>
                        <p style="color: black; font-size: 15px;"><b>{description}</b></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                #display the symptoms in a list
                col1,col2=st.columns([5,3])
                symptoms = ["Sudden severe headache", "Weakness or numbness on one side of the body", "Difficulty speaking or understanding speech", "Loss of balance or coordination", "Vision problems"]
                col1.markdown(
                    f"""
                    <div style="text-align: justify; padding: 10px; background-color: #42d1f5; border-radius: 20px; border: 1.5px solid black; margin-bottom: 20px;">
                        <h2 style="color: #111df7; font-size: 20px;"><b>Symptoms:</b></h2>
                        <ul style="color: black; font-size: 15px;">
                            <li>{symptoms[0]}</li>
                            <li>{symptoms[1]}</li>
                            <li>{symptoms[2]}</li>
                            <li>{symptoms[3]}</li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                #display the prevention measures
                prevention = ["Control high blood pressure", "Don`t smoke", "Eat a healthy diet", "Exercise regularly", "Limit alcohol consumption"]
                col2.markdown(
                    f"""
                    <div style="text-align: justify; padding: 10px; background-color: #84f74f; border-radius: 20px; border: 1.5px solid black; margin-bottom: 20px;">
                        <h2 style="color: #111df7; font-size: 20px;"><b>Prevention Measures:</b></h2>
                        <ul style="color: black; font-size: 15px;">
                            <li>{prevention[0]}</li>
                            <li>{prevention[1]}</li>
                            <li>{prevention[2]}</li>
                            <li>{prevention[3]}</li>
                            <li>{prevention[4]}</li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                st.write(f"")

            elif predicted_class=='Ischemic':
                col1, col2, col3 = st.columns([7, 6, 3])
                col2.markdown(f"<h2 style='color:red;'>Ischemic</h2>", unsafe_allow_html=True)
                description = "An ischemic stroke is a life-threatening condition that occurs when a blood vessel in the brain becomes blocked or narrowed, cutting off blood flow to part of the brain. This deprives brain cells of oxygen and nutrients, causing them to die. Ischemic strokes are the most common type of stroke, accounting for about 87% of all strokes. There are two main types of ischemic strokes: thrombotic strokes and embolic strokes."
                st.markdown(
                    f"""
                    <div style="text-align: justify; padding: 10px; background-color: #f0e222; border-radius: 20px; border: 1.5px solid black; margin-bottom: 20px;">
                        <h2 style="color: #111df7; font-size: 20px;"><b>Disease Description:</b></h2>
                        <p style="color: black; font-size: 15px;"><b>{description}</b></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                #display the symptoms in a list
                col1,col2=st.columns([5,3])
                symptoms = ["Sudden severe headache", "Weakness or numbness on one side of the body", "Difficulty speaking or understanding speech", "Loss of balance or coordination", "Vision problems"]
                col1.markdown(
                    f"""
                    <div style="text-align: justify; padding: 10px; background-color: #42d1f5; border-radius: 20px; border: 1.5px solid black; margin-bottom: 20px;">
                        <h2 style="color: #111df7; font-size: 20px;"><b>Symptoms:</b></h2>
                        <ul style="color: black; font-size: 15px;">
                            <li>{symptoms[0]}</li>
                            <li>{symptoms[1]}</li>
                            <li>{symptoms[2]}</li>
                            <li>{symptoms[3]}</li>
                            <li>{symptoms[4]}</li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                #display the prevention measures
                prevention = ["Control high blood pressure", "Don`t smoke", "Eat a healthy diet", "Exercise regularly", "Limit alcohol consumption"]
                col2.markdown(
                    f"""
                    <div style="text-align: justify; padding: 10px; background-color: #84f74f; border-radius: 20px; border: 1.5px solid black; margin-bottom: 20px;">
                        <h2 style="color: #111df7; font-size: 20px;"><b>Prevention Measures:</b></h2>
                        <ul style="color: black; font-size: 15px;">
                            <li>{prevention[0]}</li>
                            <li>{prevention[1]}</li>
                            <li>{prevention[2]}</li>
                            <li>{prevention[3]}</li>
                            <li>{prevention[4]}</li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


            elif predicted_class=='Normal':
                col,col2,col3=st.columns([7,6,3])
                col2.markdown(
                    f"""
                    <div style="text-align: center; padding: 10px; background-color: #42f551; border-radius: 20px; border: 1.5px solid black; margin-bottom: 20px;">
                        <h2 style="color: black; font-size: 20px;"><b>No Tumor Detected</b></h2>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


if __name__ == "__main__":
    main()
