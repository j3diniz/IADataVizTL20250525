import streamlit as st
import webbrowser
from Utils.Utils import ReturnDf

### Page Configuration ###
st.set_page_config(
    page_title = 'eTLipse',
    page_icon = '💻',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.etlipse.com',
        'Report a bug': 'http://www.etlipse.com',
        'About': 'Site desenvolvido pela eTLipse.'
    }
)

if 'data' not in st.session_state:
    dfActual = ReturnDf('./Models/DataBase/ImoveisVendasSaoLuisMA20250305.csv', separator = ';', encoder = 'utf-8')
    st.session_state['data'] = dfActual


st.markdown('## eTLipse - Computação, Engenharia e Responsabilidade Social')



btn = st.button('Acesse nosso site!')
if btn:
    webbrowser.open_new_tab('http://www.etlipse.com')

st.markdown(
    '''<div style="text-align: justify;">
    <strong>Soluções Computacionais:</strong><br>
    ✓ Desenvolvimento de Software<br>
    ✓ Plugins para Integração com Sistemas e Softwares Existentes<br>
    ✓ Ferramentas Personalizadas<br>
    ✓ Customização de Relatórios e Dashboards<br>
    ✓ Soluções para Indústria AEC, especialmente BIM<br>
    <br>
    <strong>Soluções com Inteligência Artificial:</strong><br>
    ✓ Visão Computacional<br>
    ✓ Agentes Autônomos de Inteligência Artificial<br>
    ✓ Soluções Personalizadas com Inteligência Artificial<br>
    ✓ Sistemas Inteligentes de apoio à Gestão<br>
    ✓ Sistema que apresenta resumos e informações inferidas de base de dados privadas usando Inteligência Artificial
    </div>'''
    , unsafe_allow_html = True)

# Sidebar
st.sidebar.markdown('##### Desenvolvido pela [eTLipse](https://www.etlipse.com/)')