import streamlit as st
import pandas as pd
import plotly.express as px
from ColetarDados import coletar_reddit

# -------------------------
# Configuração e Cabeçalho da Página
# -------------------------
st.set_page_config(page_title="Painel da Solidão", layout="wide")

st.title("Painel da Solidão – Plataforma de Análise e Visualização de Saúde Mental")

st.markdown("""
**Sobre o Projeto**

O Painel da Solidão é uma aplicação de análise e visualização de dados sobre depressão, com foco em saúde mental, tecnologia e impacto social. 
Aqui integramos artigos de referência e relatos reais do Reddit, criando um espaço que une contexto científico e experiência humana.

**Objetivo:** usar dados para conscientizar sobre saúde mental e abrir espaço para análise crítica.
""")
st.divider()


# -------------------------
# Matéria Unificada sobre Depressão
# -------------------------
st.header("Matérias sobre depressão")
# (Esta seção continua a mesma, sem alterações)
with st.container(border=True):
    st.subheader("A Depressão: Uma Jornada Histórica e Seus Desafios Contemporâneos")
    st.markdown("""
    A compreensão da depressão remonta à Antiguidade, quando Hipócrates, no século IV a.C., introduziu o termo "melancolia", derivado do grego mêlas (negro) e khole (bile), associando-a ao excesso de bile negra no corpo. Essa concepção perdurou por séculos, sendo reinterpretada ao longo do tempo conforme avanços na medicina e na psicologia.

    Durante a Idade Média, as explicações para os transtornos mentais eram predominantemente de natureza sobrenatural, com tratamentos que incluíam práticas como sangrias e o uso de substâncias como aloés e heléboro negro, na tentativa de restaurar o equilíbrio corporal.

    Foi no século XIX que a melancolia começou a ser reconhecida como uma condição médica. O psiquiatra francês Jean-Étienne Dominique Esquirol introduziu o conceito de "lipemania", destacando a natureza afetiva da doença, o que representou um avanço significativo na compreensão da depressão como transtorno mental.
    
    ##### **Avanços no Século XX**
    O século XX marcou uma transformação na abordagem da depressão. No início do século, o psiquiatra alemão Emil Kraepelin desenvolveu um sistema diagnóstico que classificava os transtornos mentais com base em suas características clínicas e curso da doença, influenciando profundamente a psiquiatria moderna.

    Com o tempo, a compreensão da depressão passou a integrar fatores biológicos, psicológicos e sociais. A introdução de medicamentos antidepressivos e terapias psicológicas proporcionou novas perspectivas de tratamento, embora ainda existam desafios no acesso e na eficácia desses tratamentos para todos os pacientes.

    ##### **A Realidade Atual: Um Desafio Global**
    Atualmente, a depressão é reconhecida como uma das principais causas de incapacidade no mundo. Estima-se que mais de 300 milhões de pessoas sejam afetadas por transtornos mentais, sendo a depressão um dos mais prevalentes.

    No Brasil, a situação é alarmante. De acordo com dados da Organização Pan-Americana da Saúde (OPAS), o país apresenta uma das maiores taxas de prevalência de depressão na América Latina. Fatores como desemprego, violência e desigualdade social contribuem significativamente para esse cenário.

    A pandemia de COVID-19 exacerbou ainda mais esse quadro. Um estudo da Organização Mundial da Saúde (OMS) revelou que, no primeiro ano da pandemia, a prevalência global de ansiedade e depressão aumentou em 25%, com jovens e mulheres sendo os grupos mais afetados.

    ##### **O Impacto Digital: Depressão, Jovens e Redes Sociais**
    Nos últimos anos, o uso de redes sociais entre jovens se tornou massivo, mas junto com a conexão constante, crescem também os efeitos negativos na saúde mental. Estudos mostram que passar muitas horas online, comparando-se a padrões irreais de vida e aparência, pode aumentar sentimentos de inadequação, ansiedade e tristeza persistente.

    O ambiente digital, apesar de conectar pessoas, muitas vezes intensifica o isolamento, pois substitui interações presenciais por contatos superficiais. Além disso, o fenômeno do cyberbullying e a pressão por validação — curtidas, seguidores e comentários — ampliam o impacto psicológico, tornando o jovem mais vulnerável a transtornos depressivos.

    Pesquisas recentes indicam que adolescentes que passam mais de três horas por dia em redes sociais têm significativamente mais risco de apresentar sintomas de depressão. A exposição constante a conteúdos que reforçam padrões de perfeição e sucesso irreal contribui para a baixa autoestima e sentimentos de inadequação.

    É essencial que jovens e responsáveis estejam conscientes desses riscos. Limitar o tempo de uso das redes, priorizar interações reais e buscar apoio quando necessário são medidas fundamentais para preservar a saúde mental nesse contexto hiperconectado.
    """)
    
    st.markdown("""
    ---
    **Fontes e Referências:**
    - Organização Pan-Americana da Saúde (OPAS/OMS). *Depressão e outros transtornos mentais comuns*.
    - World Health Organization (WHO). *Mental Health and COVID-19: Early evidence of the pandemic’s impact*. 2022.
    - Twenge, J. M., & Campbell, W. K. (2019). *Associations between screen time and lower psychological well-being among children and adolescents: Evidence from a population-based study*. JAMA Pediatrics.
    """)
st.divider()

# -------------------------
# Seção de Dados do SUS com Gráfico
# -------------------------
# (Esta seção continua a mesma, sem alterações)
st.header("Análise de Dados: A Situação no Brasil")
with st.container(border=True):
    st.subheader("Evolução das Internações por Transtornos Mentais e Comportamentais (SUS)")
    st.markdown("""
    Os dados a seguir, obtidos do DATASUS, mostram o número total de internações hospitalares na rede pública brasileira cuja principal causa foi diagnosticada como transtorno mental ou comportamental. 
    Embora os números mostrem flutuações, incluindo uma queda durante o auge da pandemia de COVID-19 (provavelmente devido a barreiras de acesso), a tendência geral indica uma demanda consistentemente alta por cuidados intensivos em saúde mental no país.
    """)
    
    try:
        df_sus = pd.read_csv("dados_sus.csv")
        fig = px.bar(df_sus, 
                      x='Ano', 
                      y='Internacoes',
                      title='Número de Internações/Ano (CID-10 Cap. V)',
                      labels={'Internacoes': 'Total de Internações', 'Ano': 'Ano'},
                      text_auto=True)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Fonte: Ministério da Saúde - Sistema de Informações Hospitalares do SUS (SIH/SUS)")
    except FileNotFoundError:
        st.error("Arquivo 'dados_sus.csv' não encontrado. Certifique-se de que ele está na mesma pasta do projeto.")

st.divider()


# --------------------------------------------------------
# NOVA SEÇÃO DO REDDIT - COM CAIXA DE AVISO E CHECKBOX
# --------------------------------------------------------
st.header("Histórias que Precisam Ser Ouvidas")

# O container com borda cria a "caixinha cinza" para o aviso
with st.container(border=True):
    st.warning("Atenção: Conteúdo Sensível")
    st.markdown("""
    Os relatos a seguir são extraídos de comunidades de apoio e podem conter descrições de sofrimento psicológico, depressão e pensamentos suicidas. 
    Prossiga com cautela.
    """)
    # O checkbox controla a exibição do conteúdo
    show_posts = st.checkbox("Eu entendo os riscos e quero ver os relatos.")

# Os posts só são carregados e exibidos SE o checkbox for marcado
if show_posts:
    st.markdown("---") # Adiciona um separador visual
    
    # Chama a função para coletar os dados do Reddit
    df_reddit = coletar_reddit()

    if df_reddit.empty:
        st.info("Nenhum post relevante encontrado no momento. Tente novamente mais tarde.")
    else:
        # Itera sobre cada linha do DataFrame para criar um card
        for index, row in df_reddit.iterrows():
            with st.container(border=True):
                st.markdown(f"**r/{row['subreddit']}** • Postado por u/{row['author']}")
                st.subheader(f"{row['title']}")
                st.write(f"{row['text'][:600]}...")
                
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.text(f"⬆️ {row['score']}  💬 {row['comments']}")
                with col2:
                    st.link_button("Ver post completo no Reddit", row['url'])
                
                st.caption(f"🕒 {row['created']}")
# --------------------------------------------------------
# FIM DA SEÇÃO MODIFICADA
# --------------------------------------------------------

st.divider()

# -------------------------
# Seção Twitter (Futuro)
# -------------------------
st.header("Twitter - relatórios futuros")
st.info("Em breve, tweets relevantes sobre depressão serão integrados aqui.")
st.divider()

# -------------------------
# Recursos de Ajuda
# -------------------------
with st.container(border=True):
    st.subheader("Precisa de ajuda? Você não está sozinho.")
    st.error("""
    Se você está passando por um momento difícil, procurar ajuda é um ato de coragem.
    Aqui estão alguns contatos importantes e gratuitos:

    - **Centro de Valorização da Vida (CVV):** Ligue **188** (ligação gratuita, 24h) ou acesse [cvv.org.br](https://www.cvv.org.br) para chat.
    - **CAPS e Unidades Básicas de Saúde (SUS):** Procure o Centro de Atenção Psicossocial (CAPS) mais próximo ou sua Unidade Básica de Saúde.
    - **Emergência:** Em caso de risco imediato à vida, ligue para o **SAMU (192)** ou procure o pronto-socorro mais próximo.
    """)
st.divider()

# -------------------------
# Contato do Desenvolvedor
# -------------------------
st.header("Contato do Desenvolvedor")
st.markdown("""
**Flavio Amaral**  
Email: Flavio4567@proton.me  
LinkedIn: [linkedin.com/in/flavio-amaral46](https://www.linkedin.com/in/flavio-amaral46)  
GitHub: [github.com/TioNebu](https://github.com/TioNebu)
""")