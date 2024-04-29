import streamlit as st
from PIL import Image
import google.generativeai as genai


# Function to handle gemini-pro-vision model
def handle_gemini_pro_vision(model, prompt_value=''):
    imageupload = st.file_uploader('Upload your image')
    if imageupload:
        pr = st.text_input('Write Your Question here', value=prompt_value)
        generate_button = st.button("Generate Content")
        if generate_button:
            img = Image.open(imageupload)
            response = model.generate_content([pr, img])
            st.subheader('Your Image 👇')
            st.image(img)
            st.subheader('The Answer of Your Question 👇️')
            st.write(response.text)


# Function to handle gemini-pro model
def handle_gemini_pro(model):
    inp = st.text_area('Write your prompt')
    bt = st.button('Generate')
    if inp and bt:
        response = model.generate_content(inp)
        st.write(response.text)


# Main function
def main():
    api_key = st.text_input('Enter your GEMINI API key')
    genai.configure(api_key=api_key)

    models = st.selectbox('Select your model', ['gemini-pro-vision', 'gemini-pro'])
    model = genai.GenerativeModel(models)

    if models == "gemini-pro-vision":
        handle_gemini_pro_vision(model)
    elif models == "gemini-pro":
        handle_gemini_pro(model)


if __name__ == "__main__":
    main()
