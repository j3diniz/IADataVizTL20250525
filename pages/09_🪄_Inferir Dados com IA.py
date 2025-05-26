import streamlit as st
import webbrowser
from Utils.Utils import ReturnDf

### Page Configuration ###
st.set_page_config(
    page_title = 'Inferir Dados com IA',
    page_icon = '🪄',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.etlipse.com',
        'Report a bug': 'http://www.etlipse.com',
        'About': 'Site desenvolvido pela eTLipse'
    }
)

st.markdown('## Inferência de Dados com Inteligência Artificial')
st.markdown("### _Disponível_ em :red[breve!] :calendar:")

st.markdown(
    '''">
    Estudo de Caso:
    
    Utiliza Inteligência Artificial para inferir dados de textos, como o do resumo descritivo do imóvel, 
    onde é possível extrair características do imóvel, como quantidade de quartos, área, etc.
    '''
    , unsafe_allow_html = True)

# Sidebar
st.sidebar.markdown('##### Desenvolvido pela [eTLipse](https://www.etlipse.com/)')
