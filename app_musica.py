import streamlit as st

musicas = {
    "Brent faiyaz": {
        "Brent faiyaz": "https://www.youtube.com/watch?v=O8CKxlmkZtw",
    },
    "Rihanna": {
        "Rihanna": "https://www.youtube.com/watch?v=aaOjJWOJPRg",
        "wilmar fernandesc:": "https://www.youtube.com/watch?v=J105R93auAw",
    },
    "Billie Eilish": {
        "Birds of a Feather": "https://www.youtube.com/watch?v=V9PVRfjEBTI&list=RDV9PVRfjEBTI"
    },
}

st.sidebar.image("logo.png")
artista = st.sidebar.selectbox("selecione o artista",musicas.keys())
musicas_artista = musicas[artista]
st.title(artista)
video,sobre = st.tabs(['video','sobre'])
with video:
 for musica in musicas_artista.items():
    titulo,link = musica
    st.subheader(titulo)
    st.video(link)
with sobre:
  if artista == "Rihanna":
    st.markdown("""
# 👑 Ficha Completa: Rihanna (Robyn Rihanna Fenty)

---

## 🌎 Perfil Geral
* **Nome Completo:** Robyn Rihanna Fenty
* **Data de Nascimento:** 20 de fevereiro de 1988
* **Local de Nascimento:** Saint Michael, Barbados 🇧🇧
* **Profissões:** Cantora, compositora, empresária, estilista e atriz
* **Status Atual:** Bilionária, considerada uma das mulheres *self-made* mais ricas e influentes do planeta.

---

## 🎤 1. Carreira Musical & Recordes
Descoberta em Barbados pelo produtor Evan Rogers em 2003, Rihanna mudou-se para os Estados Unidos e construiu uma das trajetórias mais vitoriosas da história da música Pop, R&B e Dancehall.

### Principais Marcos:
* **O Início (2005):** Estreou com o single *"Pon de Replay"* no álbum *Music of the Sun*.
* **A Virada de Chave (2007):** Com o álbum *Good Girl Gone Bad* e o megahit mundial **"Umbrella"** (com Jay-Z), adotou uma imagem mais madura e transformou-se num ícone global.
* **Maiores Sucessos (Hits Nº 1):** Acumulou 14 singles no topo da Billboard Hot 100, incluindo:
  * *"Don't Stop the Music"*
  * *"Rude Boy"*
  * *"Only Girl (In the World)"*
  * *"We Found Love"* (com Calvin Harris)
  * *"Diamonds"*
  * *"Stay"*
  * *"Work"* (com Drake)
* **Premiações:** Vencedora de **9 prémios Grammy**.
* **Retorno aos Palcos (2023):** Parou o mundo ao protagonizar o show do intervalo do **Super Bowl LVII**, uma das transmissão mais vistas da história da televisão.

> 💿 **Álbuns Essenciais:** *Good Girl Gone Bad* (2007) para a perfeição pop; *Loud* (2010) pela energia e cores; e *ANTI* (2016), aclamado pela crítica como a sua obra-prima artística.

---

## 💄 2. O Império de Negócios (Fenty)
Rihanna revolucionou a indústria global ao colocar a **diversidade e a inclusão** no centro dos seus negócios, transformando-se numa empresária de sucesso estratosférico.

* **Fenty Beauty (2017):** Marca de maquilhagem que revolucionou o mercado ao lançar inicialmente 40 tons de base (hoje são mais), atendendo a peles negras e retintas negligenciadas por outras marcas (fenómeno conhecido como "Efeito Fenty").
* **Savage X Fenty:** Linha de lingerie focada na diversidade de corpos, tamanhos e géneros, celebrada por desfiles altamente inclusivos.
* **Fenty Skin:** Linha de cuidados com a pele focada em fórmulas limpas, veganas e sustentáveis.

---

## 🎬 3. Cinema & Impacto Cultural
* **Atriz:** Participou em produções de Hollywood como *Battleship* (2012), na aclamada série *Bates Motel* e no filme de assalto *8 Mulheres e Um Segredo* (2018). Em 2025, deu voz à Smurfette no filme de animação *The Smurfs*.
* **Filantropia:** Criou a *Clara Lionel Foundation*, que financia programas de educação, saúde e resposta a emergências climáticas pelo mundo.
* **Heroína Nacional:** Em 2021, foi declarada oficialmente **Heroína Nacional de Barbados**, recebendo o título de Embaixadora Extraordinária e Plenipotenciária do seu país natal.

---

## 👶 4. Vida Pessoal & Família
Rihanna mantém uma relação com o rapper **A$AP Rocky** desde 2020. O casal construiu uma família com três filhos:
1. **RZA Athelston Mayers** (nascido em maio de 2022)
2. **Riot Rose Mayers** (nascido em agosto de 2023)
3. **Rocki Irish Mayers** (nascida em setembro de 2025)

---

## ✨ 5. Atualidade (2026)
* **Ícone de Estilo:** Continua a dominar a cultura pop e a moda. No **MET Gala 2026** (com o tema *"Fashion Is Art"*), parou a passadeira vermelha com um look arquitetónico escultural da Maison Margiela, adornado com mais de 115 mil joias e cristais bordados à mão.
* **Expectativa Musical:** Embora esteja plenamente dedicada à maternidade e à gestão das suas marcas bilionárias, os fãs aguardam com grande expectativa o seu nono álbum de estúdio (apelidado de *R9*), especialmente com o álbum *ANTI* a completar o seu 10.º aniversário.
""")
  elif artista == "Brent faiyaz":
   st.markdown("""
# 🎤 Ficha Completa: Brent Faiyaz

---

## 🌎 Perfil Geral
* **Nome de Batismo:** Christopher Brent Wood
* **Data de Nascimento:** 19 de setembro de 1995
* **Local de Nascimento:** Columbia, Maryland, EUA 🇺🇸
* **Profissões:** Cantor, compositor e produtor musical
* **Estilo Musical:** R&B Contemporâneo, Neo-Soul e R&B Alternativo
* **Diferencial:** Conhecido por sua voz de falsete suave e letras honestas, cruas e introspectivas sobre relacionamentos modernos e fama.

---

## 🎶 1. Carreira Musical & Sucessos
Brent começou a fazer música em 2013, inicialmente lançando batidas experimentais no SoundCloud antes de se consolidar como vocalista.

### Principais Marcos:
* **A Virada de Chave (2016):** Ganhou enorme destaque mundial ao cantar o refrão marcante do hit *"Crew"* (do rapper GoldLink com Shy Glizzy), que lhe rendeu uma indicação ao Grammy.
* **Projetos Independentes:** Ele é um dos artistas mais bem-sucedidos a manter sua independência na indústria musical através do seu próprio selo, o *Lost Kids*.
* **Álbuns Marcantes:**
  * *Sonder Son* (2017): Seu álbum de estreia solo.
  * *Fuck the World* (2020): O projeto que o consolidou na cena underground e crítica de R&B.
  * *Wasteland* (2022): Estreou em #2 na Billboard 200, trazendo hits gigantescos e participações de peso como Drake, Tyler, The Creator e Alicia Keys.
  * *Larger Than Life* (2023): Uma mixtape com estética muito inspirada no R&B do final dos anos 90 e início dos anos 2000.

---

## 🎧 2. Músicas Mais Famosas (Por Onde Começar)
Se você quer conhecer o som do Brent Faiyaz, estas são as faixas essenciais:

* **"All Mine"** – Uma das baladas de R&B mais famosas e românticas de sua discografia.
* **"Dead Man Walking"** – Um dos seus maiores sucessos solo, com uma batida marcante e atmosfera envolvente.
* **"Trust"** – Faixa acústica e suave que viralizou globalmente.
* **"Clouded"** – Uma música curta e profunda sobre crises existenciais e o legado da fama.
* **"Gravity"** (com DJ Dahi e Tyler, The Creator) – Uma colaboração leve, com uma vibe nostálgica perfeita.
* **"Crew"** (GoldLink feat. Brent Faiyaz) – O hino que colocou sua voz no mapa do mundo.

---

## 👥 3. O Coletivo "Sonder"
Além de sua carreira solo, Brent faz parte do trio de R&B/Soul chamado **Sonder**, formado em 2016 com os produtores Dpat e Atu. O grupo é aclamado por músicas como *"Too Fast"* e traz um som focado em guitarras melancólicas e vocais profundos.

---

## ✨ 4. Atualidade
* **Turnês e Festivais:** Brent consolidou sua reputação como um dos principais nomes da nova geração do R&B, lotando arenas ao redor do mundo de forma totalmente independente.
* **Moda:** Conhecido por seu estilo marcante, ele se tornou uma figura frequente nas principais semanas de moda globais (como Paris e Milão) e colaborações com marcas de roupas urbanas (*streetwear*).
""")
   
  elif artista == "Billie eilish":
    import streamlit as st

st.markdown("""
# 🥑 Ficha Completa: Billie Eilish

---

## 🌎 Perfil Geral
* **Nome Completo:** Billie Eilish Pirate Baird O'Connell
* **Data de Nascimento:** 18 de dezembro de 2001
* **Local de Nascimento:** Los Angeles, Califórnia, EUA 🇺🇸
* **Profissões:** Cantora, compositora e musicista
* **Estilo Musical:** Pop Alternativo, Indie Pop e Electropop
* **Status Atual:** Uma das artistas mais premiadas, influentes e aclamadas de sua geração, fazendo história na música e no cinema.

---

## 🎵 1. Carreira Musical & Recordes Históricos
Billie começou a ganhar destaque em 2015, quando lançou a música *"Ocean Eyes"* no SoundCloud, escrita e produzida por seu irmão e principal colaborador, **Finneas O'Connell**.

### Principais Marcos:
* **O Fenômeno (2019):** Lançou seu álbum de estreia *When We All Fall Asleep, Where Do We Go?*, que estreou em #1 e trouxe o megahit mundial **"bad guy"**.
* **História no Grammy (2020):** Tornou-se a artista mais jovem a vencer as quatro principais categorias do Grammy na mesma noite (*Álbum, Gravação, Música do Ano e Melhor Artista Revelação*). Hoje, ela acumula mais de 9 gramofones.
* **A Realeza do Oscar:** Billie fez história ao se tornar a pessoa mais jovem a ganhar **dois Oscars** de *Melhor Canção Original*: o primeiro em 2022 por *"No Time to Die"* (do filme de James Bond) e o segundo por *"What Was I Made For?"* (do filme *Barbie*).
* **Consolidação Artística:** Seus álbuns seguintes, *Happier Than Ever* (2021) e *HIT ME HARD AND SOFT*, foram aclamados pela crítica e mantiveram seu status no topo das paradas globais.

---

## 🎧 2. Músicas Mais Famosas (Por Onde Começar)
Se você quer conhecer o som de Billie Eilish, estas são as faixas essenciais:

* **"bad guy"** – O hit irreverente e dançante que a levou ao topo do mundo.
* **"What Was I Made For?"** – A emocionante e delicada balada piano-pop feita para o filme *Barbie*.
* **"Happier Than Ever"** – Uma música que começa como uma balada folk suave e explode em um rock de arena catártico.
* **"lovely"** (com Khalid) – Uma colaboração melancólica e poderosa que se tornou um dos seus maiores sucessos de streaming.
* **"Ocean Eyes"** – A canção poética e etérea que deu início a tudo.
* **"everything i wanted"** – Uma bela homenagem à sua forte conexão e parceria com seu irmão Finneas.

---

## 🍃 3. Impacto Cultural & Ativismo
* **Sustentabilidade:** Billie é uma das vozes mais ativas da música em prol do meio ambiente. Ela organiza suas turnês mundiais focando na redução da pegada de carbono e incentiva o consumo de moda consciente.
* **Estilo Único:** No início de sua carreira, ficou mundialmente conhecida por suas roupas largas e cabelos coloridos para evitar a sexualização de seu corpo pela mídia, tornando-se um ícone de estilo para a Geração Z.

---

## ✨ 4. Atualidade
* **Turnês Globais:** Continua lotando arenas e estádios ao redor do mundo com performances ao vivo conhecidas por sua alta energia e vocais impecáveis.
* **Parceria Familiar:** Mantém a parceria de sucesso com Finneas, mostrando que a produção feita de forma independente dentro de casa pode conquistar o topo do planeta.
""")