require(e1071)

c1 = c(7,1,5,2,3,1,6)

#media
mean(c1)

#mediana
median(c1)

#moda
as.numeric(names(table(c1))[table(c1) == max(table(c1))])

#Histograma
hist(c1)

#Densidade
hist(c1,probability = T)

# Inserindo a linha
lines(density(c1))

# Skewness
skewness(c1)

# Kurtosis
kurtosis(c1)

#summary
summary(c1)

######## Medidas de dispersão
#Dataset IRIS
iris
View(iris)

#Amostra
a0 = iris$Sepal.Length

#Tamanho da amostra
length(a0)

#Amplitude amostral
h = diff(range(a0))

#Variancia amostral
var(a0)

# Varianca populacional
var(a0) * (length(a0) - 1) / length(a0)

# Desvio padrao amostral
sd(a0)

# Coeficiente de variacao amostral
cv = sd(a0) / mean(a0) * 100

# Tamanho das Petalas
a1 = iris$Petal.Length

# tamanho
length(a1)

#Amplitude
diff(range(a1))

#Variancia amostral
var(a1)

# Desvio Padrao
sd(a1)

# Coeficiente de variacao
cv1 = sd(a1) / mean(a1) * 100

# Comparacao com grafico de dispersao
plot(a0)

# Inserindo uma linha com a media
plot(a0)
abline(h=mean(a0))

plot(a1)
abline(h=mean(a1))