# Texto base
s = "Python é uma linguagem poderosa e versátil."

# 1. s.find(subtexto, ini, fim)
#  A. subtexto (obrigatório): A substring que você deseja localizar.
#  B. ini (opcional): O índice inicial onde a busca deve começar. O padrão é 0.
#  C. fim (opcional): O índice final onde a busca deve terminar (não inclusivo). O padrão é o comprimento da string.

# Procurando a palavra "linguagem" entre as posições 10 e 40
posicao = s.find("linguagem", 10, 40)
print(f"Posição de 'linguagem' entre 10 e 40: {posicao}")

# Retorna o índice da primeira ocorrência de subtexto dentro do intervalo especificado (ini até fim).
# Retorna -1 se a substring não for encontrada.

# ----------------------------------------------------------------------------------------------------------

# 2. s.format(x1, ..., xn)
# é usado para formatar strings substituindo espaços reservados na string pelos valores fornecidos como argumentos ().
#  A. Espaços reservados: os espaços reservados na cadeia de caracteres são indicados por chaves.{}
#  B. Argumentos posicionais: Você pode usar , , etc., para se referir à posição dos argumentos.{0}{1}
#  C. Argumentos de palavra-chave: você pode usar espaços reservados nomeados como e passar valores usando argumentos de palavra-chave.{name}
#  D. Opções de formatação: Você pode especificar opções de formatação (por exemplo, alinhamento, largura, precisão) dentro dos espaços reservados.

# A. Uso básico - Usando format para inserir valores em uma string:
nome = "Maicon"
curso = "Análise e Desenvolvimento de Sistemas"
mensagem = "Olá, {}! Bem-vindo ao curso de {}.".format(nome, curso)
print(mensagem)

# Mais utilizado
print(f"Olá, {nome}! Bem-vindo ao curso de {curso}.")

# B. Argumentos posicionais: 
mensagem = "Os numero são {0} e {1}.".format(10, 20)
print(mensagem)

# C. Argumentos de palavras-chave:
mensagem = "A capital da {país} é {capital}.".format(país="França", capital="Paris")
print(mensagem)

# D. Formatação de números:
pi = 3.14159
mensagem = "O valor de pi é aproximadamente {:.2f}.".format(pi)
print(mensagem)

# E+. Alinhamento e largura:
mensagem = "|{:<10}|{:^10}|{:>10}|".format("left", "center", "right")
print(mensagem)

# <: Alinhar à esquerda
# ^: Alinhamento central
# >: Alinhar à direita

# ----------------------------------------------------------------------------------------------------------

# 3. s.lower()
# Convertendo todas as letras para minúsculas
minusculo = s.lower()
print(f"Texto em minúsculas: {minusculo}")

# ----------------------------------------------------------------------------------------------------------

# 4. s.upper()
# Convertendo todas as letras para maiúsculas
minusculo = s.upper()
print(f"Texto em maiúsculas: {minusculo}")

# ----------------------------------------------------------------------------------------------------------

# 5. s.replace(antigo, novo, n)
# Substituindo "Python" por "Java" apenas na primeira ocorrência
substituido = s.replace("Python", "Java", 1)
print(f"Texto com substituição: {substituido}")

# ----------------------------------------------------------------------------------------------------------


'''
Lista de várias funções e métodos úteis para manipulação de strings em Python:

------------------------------------------------------------------------------------------------------------

### 🔍 Busca e verificação
- s.find(sub, start, end) – Retorna o índice da primeira ocorrência de sub; -1 se não encontrar. x
- s.index(sub, start, end) – Igual ao find, mas gera erro se não encontrar.
- s.startswith(prefix) – Verifica se a string começa com prefix.
- s.endswith(suffix) – Verifica se a string termina com suffix.
- sub in s – Verifica se sub está contido em s.

------------------------------------------------------------------------------------------------------------

### 🔤 Transformações de texto
- s.lower() – Converte todas as letras para minúsculas. x
- s.upper() – Converte todas as letras para maiúsculas. x
- s.title() – Converte para formato de título (primeira letra maiúscula de cada palavra).
- s.capitalize() – Apenas a primeira letra da string em maiúscula.
- s.swapcase() – Inverte maiúsculas e minúsculas.

------------------------------------------------------------------------------------------------------------

### ✂️ Remoção e substituição
- s.strip() – Remove espaços em branco do início e fim.
- s.lstrip() – Remove espaços do início.
- s.rstrip() – Remove espaços do fim.
- s.replace(old, new, count) – Substitui old por new, até count vezes. x

------------------------------------------------------------------------------------------------------------

### 🧩 Divisão e junção
- s.split(sep, maxsplit) – Divide a string em uma lista usando sep.
- s.rsplit(sep, maxsplit) – Divide a partir da direita.
- s.splitlines() – Divide a string em linhas.
- 'sep'.join(lista) – Junta os elementos da lista com o separador sep.

------------------------------------------------------------------------------------------------------------

### 🔢 Formatação
- s.format(x1, x2, ...) – Insere valores formatados na string. x
- f"texto {variavel:.2f}" – Formatação moderna com f-strings. x
- s.zfill(width) – Preenche com zeros à esquerda até atingir width.

------------------------------------------------------------------------------------------------------------

### 🧠 Informações sobre a string
- len(s) – Retorna o comprimento da string.
- s.count(sub) – Conta quantas vezes sub aparece.
- s.isalpha() – Verifica se todos os caracteres são letras.
- s.isdigit() – Verifica se todos os caracteres são dígitos.
- s.isalnum() – Verifica se são letras ou números.
- s.isspace() – Verifica se são apenas espaços.
- s.islower() / s.isupper() – Verifica se está todo em minúsculas ou maiúsculas.
------------------------------------------------------------------------------------------------------------
'''
