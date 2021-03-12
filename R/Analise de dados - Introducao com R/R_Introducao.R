# "mostrando" qual eh o arquivo
attach(aulas)

# Selecionando a variavel section_id do arquivo aulas
section_id

# Alterando a quantidade de dados "printados
options(max.print = 40000)

# Visualizando a variavel section_id com 40k de registros configurados
section_id

# Mostrando os primeiros registros
head(section_id)

# Ordenando do menor para o maior
sort(section_id)

#Substituindo um valor
# 33137 == a linha que o dado se encontra
# 3 == a coluna que o dado se encontra
aulas[33137, 3] <- 3255

# viz o arquivo (e nao a variavel armazenada)
sort(aulas$section_id)

# Executando somente um dado especifico
aulas[33137, 3]

# Visualizando os valores unicos
unique(aulas$section_id)

# Tamanho do dataset
# nesting (aninhamento) == funcao dentro de outra funcao
length(unique(aulas$section_id))

# Contando a qt de vezes que a aula foi assistida
table(aulas$section_id)

#ordenando por qt. de vezes que a aula foi assistida
sort(table(aulas$section_id))

# Instalando package
install.packages("plyr")

# Importando a biblioteca
library(plyr)

# Atribuindo na variavel 'auxiliar' a contagem do 'course_id'
auxiliar <- count(aulas, vars = 'course_id')

# Salvando o arquivo
write.csv(auxiliar, "popularidade.csv")
