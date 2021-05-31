#Exercicio 03
valores_obs = c(6.8, 7.1, 5.9, 7.5, 6.3, 6.9, 7.2, 7.6, 6.6, 6.3)
mu0 = 7.4
xbar = mean(valores_obs)
alpha = 0.01
var = sqrt(1.3)
std0 = var
n = length(valores_obs)

z = (xbar - mu0)/(std0/sqrt(n))
z

z.half.alpha = qnorm(1 - alpha)
c(-z.half.alpha, -z.half.alpha )



