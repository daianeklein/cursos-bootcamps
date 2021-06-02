# importando dataset
df <- read.csv('/Users/daianeklein/Documents/Mackenzie/Documentos/Disciplinas/Módulo 03/Estatística/Aprofundamento 04/pib_gapminder.csv')
df

#Visualizando primeiros registros
head(df)

#tipos de variáveis
unlist(lapply(df,class))

#summarize
summary(df)

#count
sapply(df, function(x) length(unique(x)))

# Histograma
hist(df$pibPercap)

#tabelas
freq_simples = table(df$continente)
dados_simples = data.frame(freq_simples)
freq_acumulada = cumsum(freq_simples)
freq_relativa_simples=freq_simples/sum(freq_simples)
freq_relativa_acumulada=freq_acumulada/sum(freq_simples)

dados_simples$freq_acumulada=freq_acumulada
dados_simples$freq_relativa_simples=freq_relativa_simples
dados_simples$freq_relativa_acumulada=freq_relativa_acumulada

dados_simples

#barplot
barplot(table(df$continente))


#plot
ggplot(df, aes(y = pibPercap, x = expVida)) +
  geom_point()

#log PIBperCapita
df$lpibPercap =log(df$pibPercap)

#log lexpVida
df$lexpVida = log(df$expVida)

head(df)

hist(df$expVida)

#Analisando a correlacao
cor.test(df$lexpVida, df$lpibPercap)

# modelo
mod <- lm(lexpVida~lpibPercap, data=df)
summary(mod)

#plot
plot(df$lexpVida~df$lpibPercap)
abline(coef(mod))

#residual
e1 <- resid(mod)
round(e1,3) 
plot(mod$fitted,e1, pch=16)
abline(h=0, col=2, lty=2) 




