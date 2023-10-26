import streamlit as st

# Set Streamlit container to wide mode for more space
st.set_page_config(layout="wide")

font_css = """
<style>
@font-face {
    font-family: 'OCRARegular';
    src: url('ocr-aregular.ttf') format('truetype');
}
.ocr-font {
    font-family: 'OCRARegular';
    word-wrap: break-word;  /* ensures long strings/words break onto the next line */
}
</style>
"""

st.markdown(font_css, unsafe_allow_html=True)

st.title('PILOT')

image_path = "chimp.png" 
st.image(image_path, caption="I FIND YOUR LACK OF FAITH DISTURBING", use_column_width=True)

# Your content using the OCR font
content = """
... [Your content goes here, as previously mentioned]
"""

st.markdown(f'<div class="ocr-font">{content}</div>', unsafe_allow_html=True)
