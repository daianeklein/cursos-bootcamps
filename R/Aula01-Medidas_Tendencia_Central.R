# Instalando pacote
install.packages("e1071")
require(e1071)

# Criando primeiro vetor
c0 = c(2,3,6,9)

# Calculando a media
mean(c0)

# Calculando a mediana
median(c0)

# Sumarizando os resultados
summary(c0)

# "dividindo" a tela
par(mfrow=c(2,2))

# Grafico de Barras
barplot(c0)

# Histograma
hist(c0)

# Frequencia relativa
hist(c0, probability = T)

# Inserindo linha
lines(density(c0))

# Skewness
skewness(c0)

# Kurtosis
kurtosis(c0)