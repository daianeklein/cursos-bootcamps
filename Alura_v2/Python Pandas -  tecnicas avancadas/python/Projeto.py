# Databricks notebook source
#!/usr/bin/env python
# coding: utf-8


# COMMAND ----------

# MAGIC %md # PANDAS AVANÇADO

# COMMAND ----------

# ---

# **Python Pandas: técnicas avançadas**
# 
# Curso: <a href = 'https://cursos.alura.com.br/course/python-pandas-tecnicas-avancadas'> Alura </a>


# COMMAND ----------

# MAGIC %md # CARREGANDO OS DADOS

# COMMAND ----------

# ---


# COMMAND ----------

# MAGIC %md ## Configurações do projeto

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### Importando pacotes

# COMMAND ----------




import pandas as pd
import numpy as np


# In[ ]:






# COMMAND ----------

# MAGIC %md ### Opções de configuração

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html)



print(pd.get_option('display.max_rows')) #rows
print(pd.get_option('display.max_columns'))


# [Opções disponíveis](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html#available-options)



pd.describe_option('display.max_columns')




df = pd.DataFrame(np.arange(10000).reshape(100, 100))
df




pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 100)




df




#default configuration
pd.reset_option('display.max_rows')




df



# COMMAND ----------

# MAGIC %md ## Carregando os dados

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### Arquivos JSON - `read_json`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_json.html)
# 

# COMMAND ----------

# MAGIC %md ## JSON

# COMMAND ----------

# 
# JSON (**J**ava**S**cript **O**bject **N**otation - Notação de Objetos JavaScript) é uma formatação leve de troca de dados. Para seres humanos, é fácil de ler e escrever. Para máquinas, é fácil de interpretar e gerar. Está baseado em um subconjunto da linguagem de programação JavaScript, Standard ECMA-262 3a Edição - Dezembro - 1999. JSON é em formato texto e completamente independente de linguagem, pois usa convenções que são familiares às linguagens C e familiares, incluindo C++, C#, Java, JavaScript, Perl, Python e muitas outras. Estas propriedades fazem com que JSON seja um formato ideal de troca de dados.
# 
# [fonte](https://www.json.org/json-pt.html)
# 
# [Online JSON Viewer](http://jsonviewer.stack.hu/)



data_json = '{"A" : [1, 2, 3, 4], "B" : [5, 6, 7, 8], "C": [9, 10, 11, 12]}'
data_json




dados = pd.read_json(
    path_or_buf = data_json,
    orient = 'index')

dados




#default
dados = pd.read_json(
    path_or_buf = data_json,
    orient = 'columns')

dados




#default
dados = pd.read_json(
    path_or_buf = 'realestates.json',
    orient = 'columns')

dados



# COMMAND ----------

# MAGIC %md ### Arquivos EXCEL - `read_excel`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html)



bairros = pd.read_excel(
    io = 'bairros.xlsx',
    sheet_name = "Preço médio por tipo",
    usecols = "C:E", #colunas onde estnao os dados
    header = 2, #linha que começam os dados (considerar index = 0)
    index_col = [0,1],
    names = ['bairros', 'tipo', 'valor_m2_bairro']
) 




bairros.head()



# COMMAND ----------

# MAGIC %md # TRANSFORMANDO E TRATANDO OS DADOS

# COMMAND ----------

# ---


# COMMAND ----------

# MAGIC %md ## Transformando dados no formato JSON para uma tabela

# COMMAND ----------




dados



# COMMAND ----------

# MAGIC %md ### `json_normalize`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.json_normalize.html)



dados_normal = pd.json_normalize(data = dados.normal)
dados_normal




dados_normal['listings'].iloc[0]




type(dados_normal['listings'].iloc[0])




len(dados_normal['listings'].iloc[0])




dados_normal_listings = pd.json_normalize(data = dados_normal['listings'].iloc[0], sep = '_', max_level = 2)
dados_normal_listings




dados_normal_listings = pd.json_normalize(data = dados.normal, sep = '_', record_path = ['listings'])
dados_normal_listings




dados_highlights_listings = pd.json_normalize(data = dados.highlights, sep = '_', record_path = ['listings'])
dados_highlights_listings


# In[ ]:






# COMMAND ----------

# MAGIC %md ## Trabalhando com dados textuais

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### Transformando *strings* em listas do Python

# COMMAND ----------




dados_normal.listings.head(2)




lista_str = dados_normal_listings.loc[0, 'imovel_caracteristicas_propriedade']
lista_str




type(lista_str)



# COMMAND ----------

# MAGIC %md #### Métodos de *strings*

# COMMAND ----------

# 
# [Documentação](https://docs.python.org/3.6/library/stdtypes.html#string-methods)



lista_str[1:-1] #removendo colchetes




lista_str.strip("[]")




lista_str[1:-1].replace("'", "") #removendo aspas




lista = lista_str[1:-1].replace("'", "").split(",")
lista




type(lista)




texto = dados_normal_listings.loc[:, 'imovel_caracteristicas_propriedade']
texto


# In[ ]:






# COMMAND ----------

# MAGIC %md #### `str`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.html)



texto.str




texto.str[1:-1]




#texto.str[1:-1].replace("'", '')




texto.str[1:-1].str.replace("'", '')




texto = texto.str[1:-1].str.replace("'", '').str.split(", ")




texto




type(texto)




type(texto[0])



# COMMAND ----------

# MAGIC %md #### `filter`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.filter.html)



dados_normal_listings.filter(like = 'imovel_caracteristicas')




columns = dados_normal_listings.filter(like = 'imovel_caracteristicas').columns

for column in columns:
    dados_normal_listings[column] = dados_normal_listings[column].str[1:-1].str.replace("'", "").str.split(", ")
    dados_highlights_listings[column] = dados_highlights_listings[column].str[1:-1].str.replace("'", "").str.split(", ")




dados_normal_listings.loc[0, 'imovel_caracteristicas_propriedade']



# COMMAND ----------

# MAGIC %md # COMBINANDO CONJUNTOS DE DADOS

# COMMAND ----------

# ---



dados_normal_listings.columns == dados_highlights_listings.columns


# In[ ]:






# COMMAND ----------

# MAGIC %md ## Empilhando *DataFrames*

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### `append`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html)



dados_normal_listings.append(dados_highlights_listings)




dados_normal_listings.append(dados_highlights_listings, ignore_index = True)




dados_listings = dados_normal_listings.append(dados_highlights_listings, ignore_index = True)




dados_listings.head()



# COMMAND ----------

# MAGIC %md ### `concat`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html)



dados_listings = pd.concat([dados_normal_listings, dados_highlights_listings], ignore_index = True)




dados_listings.head()



# COMMAND ----------

# MAGIC %md ## Combinando *DataFrames* a partir de uma chave de ligação

# COMMAND ----------


# In[ ]:





# In[ ]:






# COMMAND ----------

# MAGIC %md ### Tratando a variável de ligação

# COMMAND ----------



# COMMAND ----------

# MAGIC %md #### Selecionando a variável de ligação nos dois *DataFrames*

# COMMAND ----------




bairros_amostra = dados_listings['imovel_endereco_bairro']
bairros_amostra


# [Documentação: `get_level_values`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.MultiIndex.get_level_values.html)



bairros_todos = bairros.index.get_level_values('bairros')
bairros_todos



# COMMAND ----------

# MAGIC %md #### Identificando e eliminando valores duplicados - `nunique` e `unique`

# COMMAND ----------

# 
# [Documentação: `nunique`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.nunique.html)
# 
# [Documentação: `unique`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html)



bairros_amostra.nunique()




bairros_amostra.unique()




bairros_amostra = pd.Series(bairros_amostra.unique())
bairros_amostra


# ---



bairros_todos.shape




bairros_todos.nunique()




bairros_todos = pd.Series(bairros_todos.unique())
bairros_todos



# COMMAND ----------

# MAGIC %md #### Verificando se existe correspondência entre as variáveis de ligação

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.isin.html)



bairros_amostra.isin(bairros_todos)




bairros.loc['Freguesia']




bairros.loc['Jacarepaguá']



# COMMAND ----------

# MAGIC %md #### Ajustando os valores

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.replace.html)



dados_listings['imovel_endereco_bairro'].replace('Freguesia (Jacarepaguá)', 'Freguesia', inplace = True)




bairros_amostra = pd.Series(dados_listings['imovel_endereco_bairro'].unique())
bairros_amostra




bairros_amostra.isin(bairros_todos)



# COMMAND ----------

# MAGIC %md ### Combinando os *DataFrames*

# COMMAND ----------



# COMMAND ----------

# MAGIC %md #### `merge`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html)
# 
# ```
# pandas.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes='_x', '_y', copy=True, indicator=False, validate=None)
# ```
# 
# **Parameters**
# 
# - **left**: DataFrame
# 
# 
# - **right**: DataFrame
#     
# 
# - **how**: {‘left’, ‘right’, ‘outer’, ‘inner’}, *default* ‘inner’
# 
#         Tipo de junção que será realizada.
# 
#         - left: usa apenas as chaves do DataFrame especificado no parâmetro left.
# 
#         - right: usa apenas as chaves do DataFrame especificado no parâmetro right.
# 
#         - outer: considera todos os registros dos DataFrames especificados nos parâmetros left e right, isto é, faz a união das chaves.
# 
#         - inner: considera apenas a interseção das chaves dos DataFrames especificados nos parâmetros left e right.
#     
# 
# - **on**: label ou list
# 
#         Nomes das colunas ou dos índices que serão utilizados na junção. Estes devem ser encontrados em ambos os DataFrames.
#         
# 
# - **left_on**: label ou list, or array-like
# 
#         Nomes das colunas ou dos índices do DataFrame especificado em left que serão utilizados na junção.
#         
# 
# - **right_on**: label or list, or array-like
# 
#         Nomes das colunas ou dos índices do DataFrame especificado em right que serão utilizados na junção.
#     
# 
# - **left_index**: bool, *default False*
# 
#         Indica se o índice do DataFrame especificado no parâmetro left deve ser utilizado como chave de junção.
#         
# 
# - **right_index**: bool, *default False*
# 
#         Indica se o índice do DataFrame especificado no parâmetro right deve ser utilizado como chave de junção.



dados_listings[['imovel_endereco_bairro', 'imovel_tipos_propriedade']]




dados_listings = pd.merge(
    left= dados_listings,
    right = bairros,
    left_on = ['imovel_endereco_bairro', 'imovel_tipos_propriedade'],
    right_index = True)

dados_listings



# COMMAND ----------

# MAGIC %md # ADICIONANDO INFORMAÇÕES

# COMMAND ----------

# ---


# COMMAND ----------

# MAGIC %md ## Criando as colunas `quartos`, `suites` e `banheiros`

# COMMAND ----------




dados_listings['anuncio_descricao'].head()



# COMMAND ----------

# MAGIC %md ### `str.extractall`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.extractall.html)



configuracao = dados_listings['anuncio_descricao'].str.extractall('(\d+)')
configuracao.head(9)



# COMMAND ----------

# MAGIC %md ### `unstack`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html)



configuracao = configuracao.unstack().rename(columns={0:'quartos',
                                      1: 'suites',
                                      2: 'banheiros'})

configuracao.head(9)




configuracao.columns



# COMMAND ----------

# MAGIC %md ### `droplevel`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.droplevel.html)



configuracao = configuracao.droplevel(level=0, axis = 1)




configuracao.head(9)




dados_listings = pd.merge(dados_listings, configuracao, left_index = True, right_index = True)
dados_listings.head()



# COMMAND ----------

# MAGIC %md ## Criando novas classificações

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### Com dados categóricos - `map`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html)



tipo_uso = {
    'Apartamento': 'Residencial',
    'Casa': 'Residencial',
    'Cobertura': 'Residencial',
    'Consultório': 'Comercial',
    'Imóvel Comercial': 'Comercial',
    'Loja': 'Comercial',
    'Sala Comercial': 'Comercial'
}




dados_listings.imovel_tipos_propriedade.map(tipo_uso)




imovel_tipos_uso = dados_listings.imovel_tipos_propriedade.map(tipo_uso)



# COMMAND ----------

# MAGIC %md #### `insert`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.insert.html)



dados_listings.insert(loc=0, column='imovel_tipo_uso', value = imovel_tipos_uso)




dados_listings.head()



# COMMAND ----------

# MAGIC %md ### Com dados numéricos - `cut`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.cut.html)



valor_minimo = dados_listings['anuncio_valores_venda'].min()




valor_maximo = dados_listings['anuncio_valores_venda'].max()




rotulos =['Popular', 'Padrao', 'Alto Padrao']



# COMMAND ----------

# MAGIC %md #### Utilizando classes fixas

# COMMAND ----------




pd.cut(x=dados_listings['anuncio_valores_venda'], bins = 3, labels = rotulos) #3 classes



# COMMAND ----------

# MAGIC %md #### Utilizando classes personalizadas

# COMMAND ----------




# é preciso N pontos para obter N - 1 classes
# para criar 3 classes, são necessários três pontos
classes = [valor_minimo, 400000, 2000000, valor_maximo]




pd.cut(x=dados_listings['anuncio_valores_venda'], bins = classes, labels = rotulos, include_lowest = True) 




dados_listings['classe_valor'] = pd.cut(x=dados_listings['anuncio_valores_venda'], bins = classes, labels = rotulos, include_lowest = True) 




dados_listings.head()



# COMMAND ----------

# MAGIC %md ## Novas colunas derivadas das informações existentes

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### Valor por m²

# COMMAND ----------




dados_listings['valor_m2'] = dados_listings['anuncio_valores_venda'] / dados_listings['imovel_area']




dados_listings[['anuncio_valores_venda', 'imovel_area', 'valor_m2']].iloc[16:19]



# COMMAND ----------

# MAGIC %md #### `apply`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html)



valor_m2 = lambda x: x['anuncio_valores_venda'] / x['imovel_area'] if x['imovel_area'] != 0 else 0




dados_listings['valor_m2'] = dados_listings.apply(valor_m2, axis = 1)




dados_listings[['anuncio_valores_venda', 'imovel_area', 'valor_m2']].iloc[16:19]



# COMMAND ----------

# MAGIC %md ### Piscina?

# COMMAND ----------




dados_listings['piscina'] = dados_listings['imovel_caracteristicas_condominio'].apply(lambda x: 'Piscina' in x)




dados_listings[['imovel_caracteristicas_condominio', 'piscina']].sample(10)



# COMMAND ----------

# MAGIC %md # TABULAÇÕES E SUMARIZAÇÕES

# COMMAND ----------

# ---


# COMMAND ----------

# MAGIC %md ## Agrupamentos

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### `aggregate`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.aggregate.html)



dados_listings[['anuncio_valores_venda', 'anuncio_valores_condominio', 'anuncio_valores_iptu']].aggregate(['sum','mean', 'std'])




dados_listings[['anuncio_valores_venda', 'anuncio_valores_condominio', 'anuncio_valores_iptu']].agg(['sum','mean', 'std'])



# COMMAND ----------

# MAGIC %md ### `groupby`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html)



grupamento = dados_listings[['imovel_tipos_propriedade', 'valor_m2']].groupby('imovel_tipos_propriedade')




grupamento.mean()




grupamento.agg(func=['min', 'mean', 'max', 'std'])




grupamento = dados_listings[['imovel_tipos_propriedade', 'classe_valor','valor_m2']]     .groupby(['imovel_tipos_propriedade', 'classe_valor'])




grupamento.mean().round()




grupamento.agg(func=['min', 'mean', 'max', 'std'])



# COMMAND ----------

# MAGIC %md ### `value_counts`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.value_counts.html)



dados_listings.value_counts(subset='imovel_tipos_propriedade')




dados_listings.value_counts(subset='imovel_tipos_propriedade', normalize = True)




dados_listings.value_counts(subset=['imovel_tipos_propriedade', 'classe_valor'])



# COMMAND ----------

# MAGIC %md #### `to_frame`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.to_frame.html)



dados_listings.value_counts(subset=['imovel_tipos_propriedade', 'classe_valor'], normalize = True)     .to_frame('percentual') * 100



# COMMAND ----------

# MAGIC %md ## Mudando o formato de um *DataFrame*

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### `unstack`

# COMMAND ----------

# 
# Faz a rotação ou o pivoteamento das linhas para as colunas.
# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html)



bairros.head()




bairros.unstack(level = -1)




bairros.unstack(level = 0)



# COMMAND ----------

# MAGIC %md ### `stack`

# COMMAND ----------

# 
# Faz a rotação ou o pivoteamento das colunas de um *DataFrame* para as linhas.
# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html)



grupamento = dados_listings[['imovel_tipos_propriedade', 'classe_valor','valor_m2']]     .groupby(['imovel_tipos_propriedade', 'classe_valor'])




tabelas_estatisticas = grupamento.agg(func=['min', 'mean', 'max', 'std'])
tabelas_estatisticas




tabelas_estatisticas.stack(dropna = False) 
tabelas_estatisticas


# In[ ]:






# COMMAND ----------

# MAGIC %md ## Criando tabelas dinâmicas

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### `pivot`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html)



grupamentos = dados_listings[['imovel_tipos_propriedade', 'classe_valor', 'valor_m2']]     .groupby(by=['imovel_tipos_propriedade', 'classe_valor'])

tabelas_estatisticas = grupamento.agg(func = ['min', 'mean', 'max', 'std']).round(2)
tabelas_estatisticas



# COMMAND ----------

# MAGIC %md #### `droplevel`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.droplevel.html)



tabelas_estatisticas = tabelas_estatisticas.droplevel(level = 0, axis = 'columns')
tabelas_estatisticas



# COMMAND ----------

# MAGIC %md #### `reset_index`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.reset_index.html)



tabelas_estatisticas = tabelas_estatisticas.reset_index()
tabelas_estatisticas




tabelas_estatisticas.pivot(
    index = 'imovel_tipos_propriedade',
    columns = 'classe_valor',
    values = 'mean')



# COMMAND ----------

# MAGIC %md ### `pivot_table`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html)



dados_listings.pivot_table(
    values = 'valor_m2',
    index = 'imovel_tipos_propriedade',
    columns = 'classe_valor',
    fill_value = '-',
    margins = True,
    margins_name = 'Media Geral',
    aggfunc = 'mean')




dados_listings.pivot_table(
    values = 'valor_m2',
    index = ['imovel_tipos_propriedade', 'classe_valor'],
    columns = ['anuncio_tipos_listagem', 'piscina'],
    fill_value = '-',
    margins = True,
    margins_name = 'Media Geral',
    aggfunc = 'mean',
    dropna = False)



# COMMAND ----------

# MAGIC %md # TABULAÇÕES E ESTILIZAÇÃO

# COMMAND ----------

# ---


# COMMAND ----------

# MAGIC %md ## Tabulações a partir de informações no formato de listas

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### `explode`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.explode.html)



caracteristica_propriedade = dados_listings['imovel_caracteristicas_propriedade']
caracteristica_propriedade




caracteristica_propriedade = caracteristica_propriedade.explode()
caracteristica_propriedade




caracteristica_propriedade.value_counts()




pd.merge(
    left = caracteristica_propriedade.value_counts(),
    right = caracteristica_propriedade.value_counts(normalize = True),
    left_index = True,
    right_index = True
)



# COMMAND ----------

# MAGIC %md #### `where`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.where.html)



caracteristica_propriedade.where(
    cond = caracteristica_propriedade!='',
    other = 'Sem caracteristicas',
    inplace = True)




pd.merge(
    left = caracteristica_propriedade.value_counts(),
    right = caracteristica_propriedade.value_counts(normalize = True),
    left_index = True,
    right_index = True
)



# COMMAND ----------

# MAGIC %md ## Estilizando um DataFrame

# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### `style`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.style.html)



tabela_frequencias = pd.merge(
    left = caracteristica_propriedade.value_counts(sort = False),
    right = caracteristica_propriedade.value_counts(normalize = True, sort = False),
    left_index = True,
    right_index = True
)

tabela_frequencias




tabela_frequencias.query("index != 'Sem caracteristicas'", inplace = True)




tabela_frequencias.rename(columns = {
    'imovel_caracteristicas_propriedade_x' : 'Frequencias',
    'imovel_caracteristicas_propriedade_y' : 'Percentual'}, inplace = True)

tabela_frequencias.rename_axis('caracteristicas', inplace = True)

tabela_frequencias



# COMMAND ----------

# MAGIC %md #### `format`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.format.html)



tabela_frequencias.style.format({'Percentual' : '{:.2%}'})



# COMMAND ----------

# MAGIC %md #### `bar`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.bar.html)



vmin = tabela_frequencias['Percentual'].min()

tabela_frequencias.style.format({'Percentual' : '{:.2%}'})     .bar(subset = 'Percentual', vmin=vmin, color = 'lightblue')



# COMMAND ----------

# MAGIC %md #### `applymap`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.applymap.html)



vmin = tabela_frequencias['Percentual'].min()

tabela_frequencias.style.format({'Percentual' : '{:.2%}'})     .bar(subset = 'Percentual', vmin=vmin, color = 'lightblue')     .applymap(lambda x: f"color : {'red' if x >= 35 else 'black'}", subset ='Frequencias')




vmin = tabela_frequencias['Percentual'].min()

tabela_frequencias.style.format({'Percentual' : '{:.2%}'})     .bar(subset = 'Percentual', vmin=vmin, color = 'lightblue')     .applymap(lambda x: f"color : {'red' if x >= 35 else 'black'}", subset ='Frequencias')     .applymap(lambda x: f"font-weight : {'bold' if x >= 35 else 'normal'}", subset ='Frequencias')


# In[ ]:






# COMMAND ----------

# MAGIC %md #### `highlight_max` e `highlight_min`

# COMMAND ----------

# 
# [Documentação: `highlight_max`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.highlight_max.html)
# 
# [Documentação: `highlight_min`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.highlight_min.html)



bairros




bairros.unstack()




bairros_zona_sul = ['Ipanema', 'Botafogo', 'Catete', 'Copacabana', 'Lagoa', 'Flamengo', 'Gávea',
                   'Glória', 'Leme', 'Urca', 'Leblon']




tabela_zona_sul = bairros.unstack().query("index in " + str(bairros_zona_sul)).droplevel(level = 0, axis = 1)
tabela_zona_sul




tabela_zona_sul.style.format('R$ {:,.2f}')     .highlight_max(color = 'lightgreen')     .highlight_min(color = '#C26161')




tabela_zona_sul



# COMMAND ----------

# MAGIC %md #### `background_gradient`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.background_gradient.html)



tabela_zona_sul[['Apartamento']].style     .format('R$ {:,.2f}')     .background_gradient(cmap = 'Reds')




tabela_zona_sul.style     .format('R$ {:,.2f}')     .background_gradient(subset = ['Apartamento'], cmap = 'Reds')     .background_gradient(subset = ['Cobertura'], cmap = 'Blues')


# In[ ]:






# COMMAND ----------

# MAGIC %md #### `to_excel`

# COMMAND ----------

# 
# [Documentação](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.io.formats.style.Styler.to_excel.html)

# In[ ]:






# COMMAND ----------

# MAGIC %md # ANEXOS

# COMMAND ----------

# ---


# COMMAND ----------

# MAGIC %md ### Opções para o parâmetro `cmap`

# COMMAND ----------

# 
# [Documentação](https://matplotlib.org/3.3.2/tutorials/colors/colormaps.html)



import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from collections import OrderedDict

cmaps = OrderedDict()




cmaps['Perceptually Uniform Sequential'] = [
            'viridis', 'plasma', 'inferno', 'magma', 'cividis']

cmaps['Sequential'] = [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

cmaps['Sequential (2)'] = [
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper']

cmaps['Diverging'] = [
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']

cmaps['Cyclic'] = ['twilight', 'twilight_shifted', 'hsv']

cmaps['Qualitative'] = ['Pastel1', 'Pastel2', 'Paired', 'Accent',
                        'Dark2', 'Set1', 'Set2', 'Set3',
                        'tab10', 'tab20', 'tab20b', 'tab20c']

cmaps['Miscellaneous'] = [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral',
            'gist_ncar']




nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps.items())
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))


def plot_color_gradients(cmap_category, cmap_list, nrows):
    fig, axes = plt.subplots(nrows=nrows)
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
    axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

    for ax, name in zip(axes, cmap_list):
        ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()


for cmap_category, cmap_list in cmaps.items():
    plot_color_gradients(cmap_category, cmap_list, nrows)

plt.show()


# In[ ]:




