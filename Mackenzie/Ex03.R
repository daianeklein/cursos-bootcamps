require(dplyr)
library(plyr)
library(psych)
require(ggplot2)


# Exercicio 03
df <- read.csv('/Users/daianeklein/Documents/Mackenzie/Documentos/Disciplinas/Módulo 03/Estatística/Aprofundamento 04/autos.csv',
               sep = ";")

#tipos de variáveis
unlist(lapply(df,class))

#dtype
df[, c(9, 10, 11, 17, 18)] <- sapply(df[, c(9, 10, 11, 17, 18)], 
                                     as.numeric)

#summarize
summary(df)

#count
sapply(df, function(x) length(unique(x)))

#variaveis numericas
nums <- unlist(lapply(df, is.numeric))  
nums <- df[ , nums]

multi.hist(nums[,sapply(nums, is.numeric)])

#variaveis categoricas

ggplot(df, aes(x = make, y = price)) +
  geom_boxplot()


#Selecionando as variaveis de interesse
df <- select(df, c('horsepower', 'price'))
head(df)

ggplot(df, aes(x = horsepower, y = price)) +
  geom_point()

#correlacao
cor.test(df$price, df$horsepower)

# mod1
mod1 = lm(price~horsepower, data = df)
summary(mod1)

plot(df$horsepower, df$price)
abline(coef(mod1))

#residual
e1 <- resid(mod1)
round(e1,3) 
plot(mod1$fitted,e1, pch=16)
abline(h=0, col=2, lty=2) 

