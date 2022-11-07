import streamlit as st
from PIL import Image
import requests
import base64
from io import BytesIO

hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
            

# @st.cache
def predict(encoded_string):
    
    url = 'https://hv6egfvgwctna6wz54qk7eiw6i0yablo.lambda-url.us-east-2.on.aws/'
    data = {'body': encoded_string}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers).json()
    confidences = {}
    confidences['Labels'] = list(response[0].keys())
    confidences['Confidence (%)'] = list(response[0].values())
    confidences['Confidence (%)'] = [i * 100 for i in confidences['Confidence (%)']]    
    return confidences

def main():
    st.set_page_config(
        page_title="EMLOv2 - S9 - MMG",
        layout="centered",
        page_icon="🐍",
        initial_sidebar_state="expanded",
    )

    st.title("CIFAR10 Classifier using Lambda")
    st.subheader("Upload an image to classify it")

    uploaded_file = st.file_uploader(
        "Choose an image...", type=["jpg", "png", "jpeg"]
    )

    if st.button("Predict"):
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            io_buffer = BytesIO()
            image.save(io_buffer, format="JPEG")
            encoded_string = base64.b64encode(io_buffer.getvalue()).decode("utf-8")
            encoded_string = "data:image/jpeg;base64," + encoded_string
            
            st.image(image, caption="Uploaded Image", use_column_width=False)
            st.write("")

                    
            try:
                with st.spinner("Predicting..."):
                    predictions = predict(encoded_string)
                
                    # get key with highest value
                    st.success(f"Predictions are...")
                    st.markdown(hide_table_row_index, unsafe_allow_html=True)
                    st.table(predictions)
            except:
                st.error("Something went wrong. Please try again.")
        else:
            st.warning("Please upload an image.")

    

if __name__ == "__main__":
    main()
