import dash_bootstrap_components as dbc
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from dash import Dash, Input, Output, dcc, html

from data import (cor_raca, df, fig_01, fig_02, fig_03, fig_04, fig_05, fig_06,
                  fig_07, fig_08, fig_09, fig_10, fig_11, fig_13, fig_14,
                  fig_15, fig_x, group_labels, hist_data, presenca)

app = Dash(__name__)

app.layout = html.Div(className='row', children=[
    html.H1(children='EDA - ENEM 2020'),
    html.H2(children='Perfil socio-cultural-econômico'),
    dcc.Markdown('''
                [fonte de dados](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/enem)

                Abaixo você encontra gráficos com características sociais, como cor-raça, tipo de escola,
                sexo e situação do ensino.
                Todos os gráficos mostram essas características relacionadas à outras, como faixa_etaria dos participantes do exame.
                Escolha uma faiza etária por meio do botão dropdown acima de cada gráfico. Se deseja comparar mais de
                uma faixa_etaria, use a legenda ao lado de cada gráfico.
                Aproveite e utilize o zoom e outras funcinalidades que o gráfico pode oferecer, inclusive salvar e baixar imagens de suas análises.
                **Por meio desta análise, espera-se determinar quais fatores são significativos para justificar a ausência dos candidatos ao ENEM 2020.**
                '''),
    html.H2(children='Panorama geral Cor-raça com relação à faixa_etaria, tipo de escola, sexo e a escolaridade dos inscritos no exame:'),

    dcc.Tabs([

        dcc.Tab(label='Cor-Raça x faixa_etaria', children=[
            dcc.Dropdown(presenca, value='todos os candidatos',
                         id='situacao_01'),
            dcc.Graph(
                id='grafico_01',
                figure=fig_01
            ),
            dcc.Markdown('''
No gráfico **Raça-Cor x faixa_etaria**, observa-se que a maior parcela
de estudantes são classificadas como pardas. Os candidatos classificados como brancos
são a segunda maior parte de participantes do exame. Entre esses, a maior parte
de estudantes estão na faixa_etaria entre 17 e 20 anos de idade. Esse número volta a ser relevante
na faixa_etaria entre 26 e 30 anos. Talvez esse fato seja explicado pela de mudança de carreira
e/ou segunda graduação. O total de candidatos entre 17 e 20 anos é 2.693.113 e a porcentagem de
participantes nessa condição, em relção ao total, representa 46.57 %.
Fica evidente que o grupo que mais participa do exame é representado pelos que se declaram pardos e também os brancos nessa ordem, e depois os que se declaram pretos. Nesse, a maior parte dos candidatos encontram-se na faixa_etaria entre 17 e 18 anos.
'''
                         ),
        ]),

        dcc.Tab(label='Cor-Raça x Sexo', children=[
                dcc.Dropdown(cor_raca, value='todos os candidatos',
                             id='situacao_11'),
                dcc.Graph(
                    id='grafico_11',
                    figure=fig_11
                ),
                ]),

        dcc.Tab(label='Sexo x Cor-Raça', children=[
            dcc.Dropdown(cor_raca, value='todos os candidatos',
                         id='situacao_03'),
            dcc.Graph(
                id='grafico_03',
                figure=fig_03
            ),
        ]),

        dcc.Tab(label='Escolaridade x Cor-Raça', children=[
            dcc.Dropdown(cor_raca, value='todos os candidatos',
                         id='situacao_04'),
            dcc.Graph(
                id='grafico_04',
                figure=fig_04
            ),
        ]),

        dcc.Tab(label='Tipo de Escola x Cor-Raça', children=[
            dcc.Dropdown(cor_raca, value='todos os candidatos',
                         id='situacao_02'),
            dcc.Graph(
                id='grafico_02',
                figure=fig_02
            ),
            dcc.Markdown('''
                        Esses dados mostram-se irrelevantes diante do número expressivo de candidatos que não responderam (~4 milhões). Isso pode ter sido causado por um erro ou falha no sistema, pois há uma consistência das respostas em outras perguntas do questionário.
                        Entre aqueles que responderam, temos um total de  1.194.496 candidatos da rede pública de ensino e outros 201.331 da rede privada de ensino.
                        '''),
        ]),

    ]),

    html.H2(children='Panorama geral dos candidatos eliminados do exame:'),

    dcc.Tabs([

        dcc.Tab(label="sexo + faixa_etaria: histogram", children=[
                dcc.Dropdown(presenca, value='todos os candidatos',
                             id='situacao_05'),

                dcc.Graph(
                    id='grafico_05',
                    figure=fig_05,
                ),
                dcc.Markdown('''
                Nesta análise, considerou-se ausentes aqueles que faltaram em algum dia de provas. No primeiro dia, o número de ausentes foi de 3.024.590.
                O número máximo de ausentes foi de 3.184.243 candiatos que representa o número de ausentes no segundo dia de prova.
                Esse total de ausentes representa 55.06 % em relação ao total de candidatos (masculino + feminino). Analisando o gráfico é possível evidenciar que há uma diferença significativa
                entre o sexo masculino e feminino. O número de candidatas do sexo feminino ausentes foi 1.899.443 e o número de candidatos do sexo masculino foi de
                1.284.800, ou seja, o exame contou com um total de 539.866 candidatas do sexo feminino ausentes a mais em relação aos do sexo masculino.
                O número de candidatas do sexo feminino ausentes no segundo dia do exame foi de 1.899.443 que reprenta 32.84 % do total de candidatos inscritos no exame, e as candidatas do sexo feminino ausentes no segundo dia do exame representam 54.76 % em relação ao total de candidatas do mesmo grupo, istp é, em relação ao total de candidatas do sexo feminino.
                Com relação aos candidatos do sexo masculino, os ausentes no segundo dia do exame representam 1.284.800 do total, que reprenta 22.22 % do total de candidatos inscritos e 55.52 % em relação ao total de candidatos do sexo masculino.
                Há um crescimento importante na faixa_etaria entre 26 e 30 anos. Este fato pode ser explicado por ser uma faixa_etaria que busca uma segunda formação, uma decisão por mudança de carreira ou até aqueles que se evadiram do primeiro curso de graduação.
                Uma constatação sobre candidatos eliminados ocorre a partir da faixa_etaria de 19 anos em que há mais candidatos e candidatas eliminados do que presentes.
                '''),
                ]
                ),

        dcc.Tab(label='sexo + faixa_etaria: scatter', children=[
            dcc.Dropdown(presenca, value='todos os candidatos',
                         id='situacao_06'),
            dcc.Graph(
                id='grafico_06',
                figure=fig_06
            ),
        ]
        ),

        dcc.Tab(label='cor-raça + faixa_etaria: histogram', children=[
            dcc.Dropdown(presenca, value='todos os candidatos',
                         id='situacao_08'),
            dcc.Graph(
                id='grafico_08',
                figure=fig_08
            ),
        ]
        ),
    ]),

    # gráficos na mesma linha:

    # html.H1("Tips database analysis (First dashboard)"),
    # dcc.Dropdown(presenca, value='todos os candidatos', id='situacao_07'),
    # html.Div(children=[
    #     dcc.Graph(id="grafico_07", figure=fig_07,
    #               style={'display': 'inline-block'}
    #               ),
    #     dcc.Graph(id="grafico_08", figure=fig_08,
    #               style={'display': 'inline-block'}
    #               )
    # ]),

    dcc.Tabs([
        dcc.Tab(label='density heatmap', children=[
            dcc.Dropdown(presenca, value='todos os candidatos',
                         id='situacao_09'),
            dcc.Graph(
                id='grafico_09',
                figure=fig_09
            ),
        ]),
        dcc.Tab(label='density heatmap', children=[
            dcc.Dropdown(presenca, value='todos os candidatos',
                         id='situacao_10'),
            dcc.Graph(
                id='grafico_10',
                figure=fig_10
            ),
        ]),
    ]),

    dcc.Tab(label='Escolaridade x Cor-Raça', children=[
        dcc.Dropdown(presenca, value='todos os candidatos',
                     id='situacao_x'),
        dcc.Graph(
            id='grafico_x',
            figure=fig_x
        ),
    ]),

    dcc.Tab(label="Histogram", children=[
        dcc.Dropdown(presenca, value='todos os candidatos',
                     id='situacao_13'),

        dcc.Graph(
            id='grafico_13',
            figure=fig_13,
        ),
    ]
    ),

    dcc.Tab(label="Histogram", children=[
        dcc.Dropdown(presenca, value='todos os candidatos',
                     id='situacao_14'),
        dcc.Graph(
            id='grafico_14',
            figure=fig_14,
        ),
    ]
    ),
])


@app.callback(
    Output(component_id='grafico_01', component_property='figure'),
    Input(component_id='situacao_01', component_property='value'),
)
def update_output_div_01(value):
    if value == "todos os candidatos":
        fig_01 = px.histogram(df, x="cor-raça", y=0, color="faixa_etaria")
    else:
        tabela_filtrada = df.loc[df['faixa_etaria'] == value, :]
        fig_01 = px.histogram(tabela_filtrada, x="cor-raça",
                              y=0, color="faixa_etaria")
    return fig_01


@app.callback(
    Output(component_id='grafico_11', component_property='figure'),
    Input(component_id='situacao_11', component_property='value'),
)
def update_output_div_01(value):
    if value == "todos os candidatos":
        fig_11 = px.histogram(df, x="cor-raça", y=0, color="sexo")
    else:
        tabela_filtrada = df.loc[df['cor-raça'] == value, :]
        fig_11 = px.histogram(tabela_filtrada, x="cor-raça",
                              y=0, color="sexo")
    return fig_11


@app.callback(
    Output(component_id='grafico_03', component_property='figure'),
    Input(component_id='situacao_03', component_property='value'),
)
def update_output_div_03(value):
    if value == "todos os candidatos":
        fig_03 = px.histogram(df, x="sexo", y=0, color="cor-raça")
    else:
        tabela_filtrada = df.loc[df['cor-raça'] == value, :]
        fig_03 = px.histogram(tabela_filtrada, x="sexo",
                              y=0, color="cor-raça")
    return fig_03


@app.callback(
    Output(component_id='grafico_04', component_property='figure'),
    Input(component_id='situacao_04', component_property='value'),
)
def update_output_div_04(value):
    if value == "todos os candidatos":
        fig_04 = px.histogram(df, x="situação ens.", y=0, color="cor-raça")
    else:
        tabela_filtrada = df.loc[df['cor-raça'] == value, :]
        fig_04 = px.histogram(
            tabela_filtrada, x="situação ens.", y=0, color="cor-raça")
    return fig_04


@app.callback(
    Output(component_id='grafico_02', component_property='figure'),
    Input(component_id='situacao_02', component_property='value'),
)
def update_output_div_02(value):
    if value == "todos os candidatos":
        fig_02 = px.histogram(df, x="tipo escola", y=0, color="cor-raça")
    else:
        tabela_filtrada = df.loc[df['cor-raça'] == value, :]
        fig_02 = px.histogram(
            tabela_filtrada, x="tipo escola", y=0, color="cor-raça")
    return fig_02


@app.callback(
    Output(component_id='grafico_05', component_property='figure'),
    Input(component_id='situacao_05', component_property='value'),
)
def update_output_div_05(value):
    if value == "todos os candidatos":
        fig_05 = px.histogram(df, x="faixa_etaria", y=0,
                              color="sexo", pattern_shape="presença")
    else:
        tabela_filtrada = df.loc[df['faixa_etaria'] == value, :]
        fig_05 = px.histogram(tabela_filtrada, x="faixa_etaria",
                              y=0, color="sexo", pattern_shape="presença")
    return fig_05


@app.callback(
    Output(component_id='grafico_06', component_property='figure'),
    Input(component_id='situacao_06', component_property='value'),
)
def update_output_div_06(value):
    if value == "todos os candidatos":
        fig_06 = px.scatter(df, x="faixa_etaria", y=0, color="sexo", marginal_x="box", marginal_y="rug",

                            title="",

                            labels={
                                'faixa_etaria': 'faixa_etaria',
                                '0': 'Candidados'
                            }
                            )
    else:
        tabela_filtrada = df.loc[df['faixa_etaria'] == value, :]
        fig_06 = px.scatter(tabela_filtrada, x="faixa_etaria", y=0, color="sexo", marginal_x="box", marginal_y="rug",

                            title="TÍTULO",

                            labels={
                                'faixa_etaria': 'faixa_etaria',
                                '0': 'Candidados'
                            }
                            )
    return fig_06


# @app.callback(
#     Output(component_id='grafico_07', component_property='figure'),
#     Input(component_id='situacao_07', component_property='value'),
# )
# def update_output_div_07(value):
#     if value == "todos os candidatos":
#         fig_07 = px.histogram(df, x="faixa_etaria", y=0, color="sexo",
#                               title="TÍTULO",
#                               labels={
#                                   'faixa_etaria': 'faixa_etaria',
#                                   '0': 'Candidatos'
#                               }
#                               )
#     else:
#         tabela_filtrada = df.loc[df['faixa_etaria'] == value, :]
#         fig_07 = px.histogram(tabela_filtrada, x="faixa_etaria", y=0, color="sexo",
#                               title="TÍTULO",
#                               labels={
#                                   'faixa_etaria': 'faixa_etaria',
#                                   '0': 'Candidatos'
#                               }
#                               )
#     return fig_07
@app.callback(
    Output(component_id='grafico_08', component_property='figure'),
    Input(component_id='situacao_08', component_property='value'),
)
def update_output_div_08(value):
    if value == "todos os candidatos":
        fig_08 = px.histogram(df, x="faixa_etaria", y=0, color="cor-raça",

                              title="Título",

                              labels={
                                  'faixa_etaria': 'faixa_etaria',
                                  '0': 'Candidatos'
                              }
                              )
    else:
        tabela_filtrada = df.loc[df['faixa_etaria'] == value, :]
        fig_08 = px.histogram(tabela_filtrada, x="faixa_etaria", y=0, color="cor-raça",

                              title="Título",

                              labels={
                                  'faixa_etaria': 'faixa_etaria',
                                  '0': 'Candidatos'
                              }
                              )
    return fig_08


@app.callback(
    Output(component_id='grafico_09', component_property='figure'),
    Input(component_id='situacao_09', component_property='value'),
)
def update_output_div_09(value):
    if value == "todos os candidatos":
        fig_09 = px.density_heatmap(df, x="faixa_etaria", y="residentes", marginal_x="histogram", marginal_y="violin",

                                    title="Título",

                                    labels={
                                        'faixa_etaria': 'faixa_etaria',
                                        'residentes': 'Residentes'
                                    }
                                    )
    else:
        tabela_filtrada = df.loc[df['faixa_etaria'] == value, :]
        fig_09 = px.density_heatmap(tabela_filtrada, x="faixa_etaria", y="residentes", marginal_x="histogram",
                                    marginal_y="violin",

                                    title="Título",

                                    labels={
                                        'faixa_etaria': 'faixa_etaria',
                                        'residentes': 'Residentes'
                                    }
                                    )
    return fig_09


@app.callback(
    Output(component_id='grafico_10', component_property='figure'),
    Input(component_id='situacao_10', component_property='value'),
)
def update_output_div_10(value):
    if value == "todos os candidatos":
        fig_10 = px.density_heatmap(df, x="faixa_etaria", y="cor-raça", marginal_x="box", marginal_y="histogram",

                                    title="Título",

                                    labels={
                                        'faixa_etaria': 'faixa_etaria',
                                        '0': 'Candidatos'
                                    }
                                    )
    else:
        tabela_filtrada = df.loc[df['faixa_etaria'] == value, :]
        fig_10 = px.density_heatmap(tabela_filtrada, x="faixa_etaria", y="cor-raça", marginal_x="box",
                                    marginal_y="histogram",

                                    title="Título",

                                    labels={
                                        'faixa_etaria': 'faixa_etaria',
                                        '0': 'Candidatos'
                                    }
                                    )
    return fig_10


@app.callback(
    Output(component_id='grafico_x', component_property='figure'),
    Input(component_id='situacao_x', component_property='value'),
)
def update_output_div_x(value):
    if value == "todos os candidatos":
        fig = px.bar_polar(df, r="residentes", theta="faixa_etaria", color="sexo", template="plotly_dark",
                           color_discrete_sequence=px.colors.sequential.Plasma_r)
    else:
        tabela_filtrada = df.loc[df['faixa_etaria'] == value, :]
        fig = px.bar_polar(tabela_filtrada, r="residentes", theta="faixa_etaria", color="sexo", template="plotly_dark",
                           color_discrete_sequence=px.colors.sequential.Plasma_r)

    return fig


@app.callback(
    Output(component_id='grafico_13', component_property='figure'),
    Input(component_id='situacao_13', component_property='value'),
)
def update_output_div_13(value):
    return fig_13


@app.callback(
    Output(component_id='grafico_14', component_property='figure'),
    Input(component_id='situacao_14', component_property='value'),
)
def update_output_div_14(value):
    return fig_14


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)
