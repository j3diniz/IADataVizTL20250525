import streamlit as st
import webbrowser
from Utils.Utils import ReturnDf

### Page Configuration ###
st.set_page_config(
    page_title = 'Limpar Dados',
    page_icon = '🧹',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.etlipse.com',
        'Report a bug': 'http://www.etlipse.com',
        'About': 'Site desenvolvido pela eTLipse'
    }
)

st.markdown('## Limpar Dados')
st.markdown("### _Disponível_ em :red[breve!] :calendar:")

st.write('---') # Hotline
caseDescription = st.empty()

# Sidebar
st.sidebar.markdown('##### Desenvolvido pela [eTLipse](https://www.etlipse.com/)')

with caseDescription.container():
    st.markdown(
        '''<p>
        Estudo de Caso:
        
        Permite excluir dados com erros ou fora de padrão (outlier). Limitar dados dentro de um determinado intervalo de valores.
        Excluir dados indesejados. Resumir os dados para uma determinada pesquisa.
        '''
    , unsafe_allow_html = True)
