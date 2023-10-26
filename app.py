import streamlit as st

# Set Streamlit container to wide mode for more space
st.set_page_config(layout="wide")

# Use the font from the local path
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

# Your multi-line text using the OCR font
content = """
    HELLO TEAM

    We are currently a simple group of Technologists. We do the mapping – we do the supply chain.
    We use cutting edge AI in pursuit of our R&D that aims to push the frontiers of how we perceive intelligent-systems.
    We are simply devising supply chain and logistics solutions at this point in time.
    ...
    ... (and so on)
"""
st.markdown(f'<div class="ocr-font">{content}</div>', unsafe_allow_html=True)
