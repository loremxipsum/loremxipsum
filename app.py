import streamlit as st

font_css = """
<style>
@font-face {
    font-family: 'OCRARegular';
    src: url('ocr-aregular.ttf') format('truetype');  # Ensure the path to the font file is correct
}
.ocr-font {
    font-family: 'OCRARegular';
}
</style>
"""

st.markdown(font_css, unsafe_allow_html=True)

# Use the font by wrapping your text in a div with the class 'ocr-font'
st.markdown('<div class="ocr-font">JKKKK\OCR A font</div>', unsafe_allow_html=True)
