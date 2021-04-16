#install.packages(c("scales","tidyverse"))
require(ggplot2)
require(dplyr)
require(scales)
require(plotly)
require(gridExtra)
require(tidyverse)

View(iris)
dados = iris

# Histograma
View(iris)
dados=iris
grafico_hist = ggplot(dados,aes(x=Sepal.Length)) + 
  geom_histogram(color = "black",fill="lightblue",bins =30)+
  ggtitle("Gráfico histograma do tamanho da Sépala das Plantas")+
  xlab("Tamanho das Sépalas") +
  ylab("Frequência simples") +
  theme()

grafico_hist
ggplotly(grafico_hist)

#Grafico box-plot
dados=iris
grafico_boxplot = ggplot(dados, aes(x=Sepal.Length, y=Petal.Length,fill=Species)) + 
  geom_boxplot()+
  ggtitle("Gráfico de Box-plot do tamanho da Sépala vs o tamanho das Pétalas das Plantas")+
  xlab("Tamanho das Sépalas") +
  ylab("Tamanho das Pétalas")
grafico_boxplot

#Grafico de dispersao - cor especies
dados = iris
grafico_dispersao_cor = ggplot(dados, aes(x = Sepal.Length, y = Petal.Length, cols = Species)) +
  geom_point(size=4)+ 
  ggtitle('Grafico de dispersao do tamanho das sepalas das plantas') +
  xlab('Tamanho das Sepalas') +
  ylab('Tamanho das Petalas')

grafico_dispersao_cor
ggplotly(grafico_dispersao_cor)

#Grafico de dispersao - cor especies e tamanho especies
dados = iris
grafico_dispersao_tamanho = ggplot(dados, aes(x=Sepal.Length, y= Petal.Length, col = Species)) +
  geom_point(aes(size=Species)) +
  ggtitle('Grafico de dispersao do tamanho da Sepala x o tamanho das petalas') +
  xlab('Tamanho das Sepalas') +
  ylab('Tamanho das petalas')

grafico_dispersao_tamanho
ggplotly(grafico_dispersao_tamanho)

#Gráfico de Dispersão por Spécie
dados=iris
grafico_dispersao_especie = ggplot(dados, aes(x=Sepal.Length, y=Petal.Length,col=Species)) + 
  geom_point(size=4)+
  ggtitle("Gráfico de Dispersão do tamanho da Sépala vs o tamanho das Pétalas das Plantas")+
  xlab("Tamanho das Sépalas") +
  ylab("Tamanho das Pétalas") +
  facet_wrap(~Species)
grafico_dispersao_especie


#Gráfico de linhas do desemprego nos Estados Unidos de 1967 a 2015 - Economics

dados2=economics
grafico_linhas=ggplot(economics, aes(x=date, y=unemploy)) + 
  geom_line(col="red") + 
  xlab("Ano") + 
  ylab("Desemprego (em milhares)") + 
  ggtitle("Desemprego nos Estados Unidos de 1967 a 2015 - Economics")
grafico_linhas               
ggplotly(grafico_linhas)

#Agrupando os gráficos na mesma janela com ggplot2
grid.arrange(
  grafico_hist,
  grafico_boxplot,
  grafico_dispersao_cor,
  grafico_dispersao_tamanho,
  grafico_dispersao_especie,
  grafico_linhas,
  nrow=3,ncol=2)