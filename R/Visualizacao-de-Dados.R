# renomeando as colunas
duracao <- rename(duracao, replace = c("user_id"="aluno", "course_id" = "curso", "timeToFinish" = "dias"))

#plotando grafico
plot(duracao$dias)

# Plotando histograma
hist(duracao$dias)
