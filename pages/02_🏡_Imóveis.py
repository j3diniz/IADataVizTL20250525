import pandas as pd
import streamlit as st
import altair as alt
from Utils.Utils import ReturnDf

### Page Configuration ###
st.set_page_config(
    page_title = 'Avaliações de Imóveis',
    page_icon = '🏘️',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items = {
        'Get Help': 'http://www.etlipse.com',
        'Report a bug': 'http://www.etlipse.com',
        'About': 'Site desenvolvido pela eTLipse'
    }
)

st.markdown('## Dados Imóveis')
st.markdown('## São Luís - MA')

if 'data' not in st.session_state:
    dfActual = ReturnDf('./Models/DataBase/ImoveisVendasSaoLuisMA20250305.csv', separator = ';', encoder = 'utf-8')
    st.session_state['data'] = dfActual

dfActual = st.session_state['data']

# Map values type into emojis
emojiTypeMap = {
    'Casa': '🏡',
    'Terreno': '🌳',
    'Apartamento': '🏢'
}
dfActual['Tipo'] = dfActual['Tipo'].map(emojiTypeMap).fillna(dfActual['Tipo'])

# Exclude the ID column
if 'ID' in dfActual.columns:
    dfActual = dfActual.drop(columns=['ID'])

# Format the column value type
dfActual['Valor total'] = dfActual['Valor total'].astype(float)
dfActual['Valor unitário'] = dfActual['Valor unitário'].astype(float)

# Create the DataFrame wiht special format for same datass
# columns = ['Valor total', 'Valor unitário', 'Tipo']
# dfActual[columns],
st.dataframe(
    dfActual,
    column_config={
        'Valor total': st.column_config.ProgressColumn(
            'Valor Total', format='R$ %f', min_value = 0, max_value = dfActual['Valor total'].max()
        ),
        'Valor unitário': st.column_config.ProgressColumn(
            'Valor Unitário', format='R$ %f', min_value = 0, max_value = dfActual['Valor unitário'].max()
        )
    }
)

# Sidebar
st.sidebar.markdown('##### Desenvolvido pela [eTLipse](https://www.etlipse.com/)')
