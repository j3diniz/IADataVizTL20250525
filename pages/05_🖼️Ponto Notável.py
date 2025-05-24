import streamlit as st
import webbrowser
from Utils.Utils import ReturnDf

### Page Configuration ###
st.set_page_config(
    page_title = 'Ponto Notável',
    page_icon = '🖼️',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.etlipse.com',
        'Report a bug': 'http://www.etlipse.com',
        'About': 'Site desenvolvido pela eTLipse'
    }
)

st.markdown('## Ponto Notável')

st.markdown(
    '''<p style="text-align: justify;">
    Permite definir pontos notáveis que podem explicar a valorização ou desvalorização de um imóvel.
    Por exemplor um shopping, parque, ponto turísitco, praia, etc. Uma coluna nova informa a distância de cada registro para o ponto notável definido.
    </p>'''
    , unsafe_allow_html = True)

# Sidebar
st.sidebar.markdown('##### Desenvolvido pela [eTLipse](https://www.etlipse.com/)')
