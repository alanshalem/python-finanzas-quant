# NUMEROS AL AZAR
import random

# VALOR FLOTANTE AL AZAR ENTRE 0 y 1
print(random.random())

# VALOR FLOTANTE ENTRE MIN Y MAX
print(random.uniform(2, 3))

# VALOR ENTRE MIN Y MAX DEFINIENDO INTERVALO O "STEP"
min = 0
max = 100
paso = 2
print(random.randrange(min, max, paso))

# NUMEROS ALEATORIOS EN UNA DISTRIBUCION
# DISTRIBUCION NORMAL
mu = 0
sigma = 1
print(random.normalvariate(mu, sigma))

# OTRAS DISTRIBUCIONES POSIBLES
# random.betavariate(alfa, beta)
# random.gamavariate(alfa, beta)
# random.expovariate(lambda)
# random.lognormalvariate(mu, sigma)
# random.paretovariate(alfa)
# random.weibullvariate(alfa, beta)
