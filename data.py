# import library

import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

# import data

df = pd.read_csv("MICRODADOS_ENEM_2020.csv", sep=';', encoding='ISO-8859-1')

# filter columns

df = df[['TP_FAIXA_ETARIA', 'TP_SEXO', 'TP_COR_RACA', 'TP_ST_CONCLUSAO', 'TP_ESCOLA', 'TP_PRESENCA_CN', 'Q001', 'Q002',
         'Q005', 'Q006', 'Q008', 'Q009', 'Q012', 'Q014', 'Q019', 'Q022', 'Q024', 'Q025']]

# rename columns
df = df.rename({"TP_FAIXA_ETARIA": "faixa_etaria", "TP_SEXO": "sexo", "TP_COR_RACA": "cor-raça",
                "TP_ST_CONCLUSAO": "situação ens.", "TP_ESCOLA": "tipo escola", "TP_PRESENCA_CN": "presença",
                "Q001": "ens.pai", "Q002": "ens.mãe", "Q005": "residentes", "Q006": "renda", "Q008": "banheiro",
                "Q009": "quartos", "Q012": "geladeira", "Q014": "máquina de lavar", "Q019": "TV", "Q022": "celular",
                "Q024": "computador", "Q025": "internet"}, axis=1)
# drop null data
df = df.dropna()

# sub values

df['sexo'] = df['sexo'].map({'F': 'FEMININO', 'M': 'MASCULINO'})
df['cor-raça'] = df['cor-raça'].map(
    {0: 'NÃO DECLARADO', 1: 'BRANCA', 2: 'PRETA', 3: 'PARDA', 4: 'AMARELA', 5: 'INDÍGENA'})
df['situação ens.'] = df['situação ens.'].map(
    {1: 'CONCLUIU', 2: 'ESTÁ CURSANDO', 3: 'ESTÁ CURSANDO', 4: 'EVASÃO'})
df['tipo escola'] = df['tipo escola'].map(
    {1: 'NÃO RESPONDEU', 2: 'PÚBLICA', 3: 'PRIVADA', 4: 'EXTERIOR'})
df['presença'] = df['presença'].map(
    {0: 'ELIMINADO', 1: 'PRESENTE', 2: 'ELIMINADO'})
df['faixa_etaria'] = df['faixa_etaria'].map(
    {1: '16', 2: '17', 3: '18', 4: '19', 5: '20', 6: '21', 7: '22', 8: '23', 9: '24', 10: '25', 11: '26-30',
     12: '31-35', 13: '36-40', 14: '41-45', 15: '46-50', 16: '51-55', 17: '56-60', 18: '61-65', 19: '66-70', 20: '>70'})

# group values by columns
df = df.groupby(
    ['faixa_etaria', 'sexo', 'cor-raça', 'situação ens.', 'tipo escola', 'presença', 'residentes']).size().reset_index()

# save fig by columns

fig_01 = px.histogram(df, x="cor-raça", y=0, color="faixa_etaria")

fig_02 = px.histogram(df, x="tipo escola", y=0, color="cor-raça")

fig_03 = px.histogram(df, x="sexo", y=0, color="cor-raça")

fig_04 = px.histogram(df, x="situação ens.", y=0, color="cor-raça")

fig_05 = px.histogram(df, x="faixa_etaria", y=0,
                      color="sexo", pattern_shape="presença")

fig_06 = px.histogram(df, x="faixa_etaria", y=0, color="sexo")

fig_07 = px.histogram(df, x="faixa_etaria", y=0, color="sexo")

fig_08 = px.histogram(df, x="faixa_etaria", y=0, color="cor-raça")

fig_09 = px.histogram(df, x="faixa_etaria", y="residentes")

fig_10 = px.histogram(df, x="faixa_etaria", y=0, color="cor-raça")

fig_11 = px.histogram(df, x="cor-raça", y=0, color="sexo")

fig_x = px.histogram(df, x="situação ens.", y=0, color="cor-raça")

hist_data = [df.residentes.values.tolist()]
x = hist_data
group_labels = ["#residentes"]
y = group_labels

fig_13 = ff.create_distplot(x, y)

fig_14 = go.Figure(
    data=[go.Histogram(x=df['faixa_etaria'],  histnorm='probability')])

presenca = list(df['faixa_etaria'].unique())
presenca.append("todos os candidatos")

cor_raca = list(df['cor-raça'].unique())
cor_raca.append("todos os candidatos")
