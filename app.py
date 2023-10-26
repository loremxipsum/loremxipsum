import streamlit as st

# CSS to embed and use Roboto Mono font from Google Fonts
font_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono&display=swap');

body, h1, h2, h3, h4, h5, h6, p, li, a {
    font-family: 'Roboto Mono', monospace !important;
}
</style>
"""

# Inject the font into the Streamlit app
st.markdown(font_css, unsafe_allow_html=True)


st.title('PILOT')

st.write('''
    HELLO WORLD

    We are a team of Technologists and specialists in international trade. We do the mapping – we do the supply chain. We use cutting edge AI in pursuit of our R&D that aims to push the frontiers of how we perceive intelligent-systems. We devise supply chain and logistics solutions for the time being. But, we are about to use the same framework that goes into building these solutions to change intelligence as we know it – forever.

    We will soon build supply chain and logistics systems robotized, governed, and robustized to the point where we will be capable of transporting anything from hash-tokenized-military-assets to sugar. But for now, we do salt.

    We start with the operational expenses we have access to from a group of small tier logistics companies. We start working with a fleet of 500 trucks that comply with standards of transport authorities (this allows us to architecture governance easily around vendors and other parties involved).

    Our vectorized smart-contract calculates your contributions and logs them into the blockchain automating immediate transfer of funds on your centralized-by-design, decentralized-in-nature metamask wallet on a 4-chain confirmation. 
    
    Contact me at: admin@XXXX for issues with your transfers. We are currently in the process of building a UI that allows you to view tokens you have earned. Until then, check contribution chart and contact admin.

''')





image_path = "chimp.png" 
st.image(image_path, caption="I FIND YOUR LACK OF FAITH DISTURBING.", use_column_width=True)





st.write('''
    **Top 3 contributors receive $250 + $275 + $330 in goodies/redeemable tokens/ethereum every month.**

    Further content on this can be found via accessing our project scrum on:

    xxxxxxxx.live (revisit this page on 13_N0V_2023)

    Contact admin. See you on day 33.

    ///

    For the first deliverables, we would require a ui/ux clone of craigslist. The world is a massive mosh-pit of night creatures who’re looking to push the frontiers of what is currently being perceived as intelligence – need I remind you again, the foundation to what we are currently architecturing for supply-chain management of life-essential-salt across one of the most politically conflicted regions in the world is but 'fingers-crossed-oracled' to become something that will disrupt and bring us closer to the AI God...

    Now, get on your commodores, back-door the firmware as we pop nodes around the globe for what will start as a project that will open-source a clone-model of craigslist...

    [keep checking this page every 33 days for updates]

    \\

    == Your references for now: www.craigslist.org  _** we require something with the communication functionality(ies) of craigslist to start with...**%
    contact @admin for more details_

    ---------------
    Check back on day 33 for updated contributions to the chain.
    This is a private chain that will be made public to reasonable contributors – this is to reduce spamming in our project.
     
''')
