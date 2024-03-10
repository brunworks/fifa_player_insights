import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime 

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    #Filters
    df_data_sorted = df_data[df_data["Contract Valid Until"] >= datetime.today().year] # Contrato Válido
    df_data_sorted = df_data[df_data["Value(£)"] > 0]
    df_data_sorted = df_data.sort_values(by="Overall", ascending=False)
    # Criar uma série booleana com base em algum critério
    condicao = df_data_sorted["Overall"] > 0
    # Usar a série booleana para filtrar o DataFrame
    df_data_filtrado = df_data_sorted[condicao]
    st.session_state["data"] = df_data_filtrado

st.markdown("# FIFA23 OFFICIAL DATA SET! ")
st.sidebar.markdown("Desenvolvido por [Bruno Gonzaga] (https://www.github.com/brunworks)")

btn = st.button("Acessar dados Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown(
    """
        Bem-vindo ao FIFA Player Insights

        Explore o fascinante mundo dos jogadores profissionais de futebol com o FIFA Player Insights. Nossa plataforma oferece acesso exclusivo a uma vasta gama de dados oficiais da FIFA, permitindo-lhe mergulhar profundamente nas estatísticas, desempenhos e perfis de jogadores de todo o mundo.

        Descubra o Universo do Futebol Profissional

        Com o FIFA Player Insights, você pode explorar informações detalhadas sobre os jogadores mais renomados e promissores do cenário do futebol internacional. De estrelas consagradas a talentos emergentes, nossa plataforma oferece uma visão completa do universo do futebol, fornecendo dados precisos e atualizados para satisfazer até os mais ávidos entusiastas do esporte.

        Análises Profundas e Personalizadas

        Aprofunde-se nos números e estatísticas que impulsionam o jogo com nossas análises profundas e personalizadas. Seja para acompanhar o desempenho de seu jogador favorito, avaliar o potencial de uma nova contratação para seu time ou simplesmente saciar sua curiosidade sobre os melhores jogadores do mundo, o FIFA Player Insights oferece ferramentas poderosas para explorar e compreender os dados como nunca antes.

        Confiabilidade e Credibilidade

        Nossa plataforma é alimentada por dados oficiais da FIFA, garantindo a confiabilidade e credibilidade de todas as informações apresentadas. Você pode confiar em nosso sistema para fornecer insights precisos e atualizados sobre os jogadores profissionais de futebol, apoiando suas decisões e análises com dados confiáveis diretamente da fonte oficial do esporte.

        Explore o FIFA Player Insights hoje e mergulhe no emocionante e dinâmico mundo do futebol profissional como nunca antes. Seja bem-vindo à plataforma definitiva para os verdadeiros aficionados do esporte mais popular do mundo        
    """
    )