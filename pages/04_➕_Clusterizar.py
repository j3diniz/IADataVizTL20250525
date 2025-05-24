import streamlit as st
import webbrowser
from Utils.Utils import ReturnDf

### Page Configuration ###
st.set_page_config(
    page_title = 'Clusterizar',
    page_icon = '➕',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.etlipse.com',
        'Report a bug': 'http://www.etlipse.com',
        'About': 'Site desenvolvido pela eTLipse'
    }
)

st.markdown('## Clusterizar Dados')
st.markdown("### _Disponível_ em :red[breve!] :calendar:")

st.markdown(
    '''<p style="text-align: justify;">
    Utiliza Inteligência Artificial para esta tarefa. Permite criar categorias de faixa de valores para os preços. 
    Exemplo, definifir padrões 'Baixo', 'Médio' e 'Alto' para os imóveis baseado nos preços.
    </p>'''
    , unsafe_allow_html = True)

# Sidebar
st.sidebar.markdown('##### Desenvolvido pela [eTLipse](https://www.etlipse.com/)')
