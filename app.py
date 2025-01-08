import streamlit as st # type: ignore
import pandas as pd # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore

dados = pd.read_csv('pizzas.csv')
modelo = LinearRegression()

x = dados[['diametro']]
y = dados[['preco']]

modelo.fit(x ,y)

st.title('Prevendo o valor de uma pizza')
st.divider()

diametro = st.number_input('digite o tamanho do diametro da pizza:')

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f'O valor da pizza com o diametro de {diametro:.2f} é de R${preco_previsto:.2f}.')