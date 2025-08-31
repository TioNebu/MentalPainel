# Painel da Solidão – Plataforma de Análise de Saúde Mental

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://paineldasolidao-ngdxz3oy3vrrqcfnvpacug.streamlit.app/) 


Uma plataforma interativa de análise e visualização de dados sobre depressão, construída com o objetivo de conscientizar sobre saúde mental através da união de contexto científico e experiências humanas reais.

---

###  Visão Geral do Projeto

O Painel da Solidão é um dashboard web que aborda o tema da depressão de forma ética e informativa. A aplicação integra matérias aprofundadas com fontes verificadas, dados de saúde pública do Brasil e relatos anônimos e em tempo real de comunidades online, proporcionando uma visão multifacetada sobre o impacto da saúde mental na sociedade contemporânea.

###  Principais Funcionalidades

*   **Conteúdo Informativo:** Artigos detalhados sobre a história da depressão, o impacto global e a relação com as redes sociais, com fontes acadêmicas e de organizações de saúde.
*   **Visualização de Dados:** Gráfico interativo com dados reais do DATASUS sobre a evolução de internações por transtornos mentais no Brasil.
*   **Integração com API em Tempo Real:** Coleta e exibe os relatos mais relevantes e recentes de comunidades de apoio do Reddit (como r/depression e r/SuicideWatch).
*   **Interface Ética e Responsável:** Implementação de um aviso de conteúdo sensível com um *checkbox* de consentimento, garantindo que o usuário tenha controle sobre a visualização de relatos potencialmente pesados.
*   **Recursos de Ajuda:** Seção de acesso rápido com contatos de emergência e apoio profissional, como o CVV e o CAPS.


###  Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

*   **Backend & Frontend:** Python, Streamlit
*   **Análise de Dados:** Pandas
*   **Visualização de Dados:** Plotly
*   **Coleta de Dados (API):** PRAW (Python Reddit API Wrapper)
*   **Versionamento:** Git & GitHub
*   **Deploy:** Streamlit Community Cloud

###  Como Executar Localmente

Para rodar este projeto em sua máquina local, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    cd SEU_REPOSITORIO
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    *   Crie um arquivo chamado `.env` na raiz do projeto.
    *   Adicione suas credenciais da API do Reddit neste arquivo:
    ```
    CLIENT_ID="SEU_CLIENT_ID"
    CLIENT_SECRET="SEU_CLIENT_SECRET"
    USER_AGENT="SeuUserAgent"
    ```

5.  **Execute a aplicação:**
    ```bash
    streamlit run app.py
    ```

###  Contato

**Flavio Amaral**

*   **Email:** Flavio4567@proton.me
*   **LinkedIn:** [linkedin.com/in/flavio-amaral46](https://linkedin.com/in/flavio-amaral46)

---