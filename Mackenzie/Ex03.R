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

#mod 02
head(df)

df$Lprice =log(df$price)

hist(df$Lprice)
hist(df$price)

mod02 = lm(Lprice~horsepower, data = df)
summary(mod02)

plot(df$horsepower, df$Lprice)
abline(coef(mod02))

#residual
e1 <- resid(mod02)
round(e1,3) 
plot(mod1$fitted,e1, pch=16)
abline(h=0, col=2, lty=2) 

#mod03
df$Lhorsepower = log(df$horsepower)
hist(df$horsepower)
hist(df$Lhorsepower)

mod03 = lm(Lprice~Lhorsepower, data = df)
summary(mod03)

plot(df$Lhorsepower, df$Lprice)
abline(coef(mod03))

#residual
e1 <- resid(mod03)
round(e1,3) 
plot(mod1$fitted,e1, pch=16)
abline(h=0, col=2, lty=2) 

#Shapiro
shapiro.test(mod1$resid)
shapiro.test(mod02$resid)
shapiro.test(mod03$resid)

#resultados
#mod 01: Yhat = -4630.70 + 173.13 * horsepower
#mod 02: log(Lprice) = 8.187207 + 0.0112502 * horsepower
#mod 03: log(Lprice) = 3.55712 + 1.26534 * logHorsepower

Yhat1 = -4630.70 + 173.13 * 127; Yhat1 # Previsao modelo 01
Yhat2 = (8.187207) + + 0.0112502 * 127; exp(Yhat2) # Previsao modelo 02
Yhat3 = 3.55712 + 1.26534 * (log(127)); exp(Yhat3) # Previsao modelo 03

  
