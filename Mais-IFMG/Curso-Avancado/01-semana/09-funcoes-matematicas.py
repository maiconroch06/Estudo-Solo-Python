import math

n = float(input('Informe um número: '))
x = n * math.pi

print('x = n * pi = ', n)
print('Teto de x =', math.ceil(x)) # math.ceil: 
print('Piso de x =', math.floor(x)) # math.floor: 
print('Parte inteira de x =', math.trunc(x)) # math.trunc: 
print('Euler de x =', math.exp(x)) # math.exp: retorna e^x
print('Log de x na base 10 =', math.log(x, 10)) # math.log: calcula o logaritimo 
print('Raiz de x =', math.sqrt(x)) # math.sqrt: calcula raiz quadrada

''' 
Lista de várias funções matemáticas em Python:

------------------------------------------------------------------------------------------------------------
import math

### 🔢 Funções básicas
- 'abs(x)' – Valor absoluto.
- 'round(x, n)' – Arredonda 'x' com 'n' casas decimais.
- 'pow(x, y)' – Potência: x^y.
- 'math.sqrt(x)' – Raiz quadrada.

------------------------------------------------------------------------------------------------------------

### 🧮 Funções trigonométricas
- 'math.sin(x)' – Seno de 'x' (em radianos).
- 'math.cos(x)' – Cosseno.
- 'math.tan(x)' – Tangente.
- 'math.asin(x)' – Arco seno.
- 'math.acos(x)' – Arco cosseno.
- 'math.atan(x)' – Arco tangente.
- 'math.radians(x)' – Converte graus para radianos.
- 'math.degrees(x)' – Converte radianos para graus.

------------------------------------------------------------------------------------------------------------

### 📐 Funções logarítmicas e exponenciais
- 'math.exp(x)' – Exponencial: e^x.
- 'math.log(x)' – Logaritmo natural (base e).
- 'math.log10(x)' – Logaritmo na base 10.
- 'math.log2(x)' – Logaritmo na base 2.

------------------------------------------------------------------------------------------------------------

### 📊 Funções estatísticas (módulo 'statistics')
import statistics

- 'statistics.mean(lista)' – Média.
- 'statistics.median(lista)' – Mediana.
- 'statistics.mode(lista)' – Moda.
- 'statistics.stdev(lista)' – Desvio padrão.
- 'statistics.variance(lista)' – Variância.

------------------------------------------------------------------------------------------------------------

### 🧠 Outras funções úteis
- 'math.ceil(x)' – Arredonda para cima.
- 'math.floor(x)' – Arredonda para baixo.
- 'math.fabs(x)' – Valor absoluto como float.
- 'math.factorial(x)' – Fatorial de 'x'.
- 'math.isfinite(x)' – Verifica se é finito.
- 'math.isinf(x)' – Verifica se é infinito.
- 'math.isnan(x)' – Verifica se é NaN (não é número).
- 'math.gcd(a, b)' – Máximo divisor comum.

------------------------------------------------------------------------------------------------------------
'''