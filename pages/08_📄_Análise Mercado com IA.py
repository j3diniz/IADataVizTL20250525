import streamlit as st
import webbrowser
from Utils.Utils import ReturnDf

### Page Configuration ###
st.set_page_config(
    page_title = 'Análise de Mercado com IA',
    page_icon = '📄',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.etlipse.com',
        'Report a bug': 'http://www.etlipse.com',
        'About': 'Site desenvolvido pela eTLipse'
    }
)

st.markdown('## Análise de Mercado com Inteligência Artificial')
st.markdown("### _Disponível_ em :red[breve!] :calendar:")

st.markdown(
    '''<p>
    Estudo de Caso:
    
    Utiliza Inteligência Artificial para definir um relatório de análise do mercado imobiliário.
    Funcionalidade que pode auxiliar na definição de laudos e avaliações de imóveis.
    '''
    , unsafe_allow_html = True)

# Sidebar
st.sidebar.markdown('##### Desenvolvido pela [eTLipse](https://www.etlipse.com/)')
