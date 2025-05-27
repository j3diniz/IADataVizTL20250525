import streamlit as st
import webbrowser
from Utils.Utils import ReturnDf

### Page Configuration ###
st.set_page_config(
    page_title = 'Dashboards - Gráficos',
    page_icon = '📈',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.etlipse.com',
        'Report a bug': 'http://www.etlipse.com',
        'About': 'Site desenvolvido pela eTLipse'
    }
)

st.markdown('## Dashboards - Gráficos')
st.markdown("### _Disponível_ em :red[breve!] :calendar:")

st.write('---') # Hotline
st.markdown(
    '''<p>
    Estudo de Caso:
    
    Diversos dashboards / gráficos para facilitar a visualização e análise dos dados.
    '''
    , unsafe_allow_html = True)

# Sidebar
st.sidebar.markdown('##### Desenvolvido pela [eTLipse](https://www.etlipse.com/)')
