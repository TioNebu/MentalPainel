import praw
import pandas as pd
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def coletar_reddit():
    """
    Conecta-se à API do Reddit, coleta os posts mais recentes de subreddits específicos,
    calcula uma pontuação de relevância e retorna os 3 posts mais relevantes.
    """
    try:
        # Autenticação na API do Reddit usando as credenciais do .env
        reddit = praw.Reddit(
            client_id=os.getenv("CLIENT_ID"),
            client_secret=os.getenv("CLIENT_SECRET"),
            user_agent=os.getenv("USER_AGENT")
        )

        subreddits = ["depression", "SuicideWatch", "mentalhealth"]
        posts = []

        for sub_name in subreddits:
            subreddit = reddit.subreddit(sub_name)
            # Coleta os 50 posts mais recentes de cada subreddit
            for post in subreddit.new(limit=50):
                # Filtra posts que têm texto (não apenas imagens ou links) e um tamanho mínimo
                if post.selftext and len(post.selftext) > 50:
                    posts.append({
                        "subreddit": sub_name,
                        "title": post.title,
                        "text": post.selftext,
                        "score": post.score,
                        "comments": post.num_comments,
                        "author": str(post.author),
                        "url": post.url,
                        "created": datetime.fromtimestamp(post.created_utc, timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                    })

        # Se encontrou posts, cria um DataFrame e calcula a relevância
        if posts:
            df = pd.DataFrame(posts)
            # A relevância é a soma dos upvotes + o dobro do número de comentários
            df["relevance"] = df["score"] + df["comments"] * 2
            # Ordena pela relevância e pega os 3 melhores
            top_posts = df.sort_values("relevance", ascending=False).head(3)
            return top_posts.reset_index(drop=True)
        else:
            # Retorna um DataFrame vazio se não encontrar nada
            return pd.DataFrame()
            
    except Exception as e:
        print(f"Erro ao conectar ou processar dados do Reddit: {e}")
        # Retorna um DataFrame vazio em caso de erro
        return pd.DataFrame()