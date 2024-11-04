# Atividade 1: Retornar números ímpares
def filtrar_impares(lista):
    impares = []
    for numero in lista:
        if numero % 2 != 0:
            impares.append(numero)
    return impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
impares = filtrar_impares(numeros)
print(impares)  # [1, 3, 5, 7, 9]

# Atividade 2: Retornar números primos
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filtrar_primos(lista):
    primos = []
    for numero in lista:
        if eh_primo(numero):
            primos.append(numero)
    return primos

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primos = filtrar_primos(numeros)
print(primos)  # [2, 3, 5, 7, 11]

# Atividade 3: Elementos exclusivos em duas listas
def elementos_unicos(lista1, lista2):
    unica_lista1 = [item for item in lista1 if item not in lista2]
    unica_lista2 = [item for item in lista2 if item not in lista1]
    return unica_lista1 + unica_lista2

lista_a = [1, 2, 3, 4]
lista_b = [3, 4, 5, 6]
resultado = elementos_unicos(lista_a, lista_b)
print(resultado)  # [1, 2, 5, 6]

# Atividade 4: Encontrar o segundo maior valor
def segundo_maior(lista):
    if len(lista) < 2:
        return None
    unicos = list(set(lista))
    unicos.sort(reverse=True)
    if len(unicos) < 2:
        return None
    return unicos[1]

numeros = [10, 20, 20, 30, 40, 40, 50]
segundo = segundo_maior(numeros)
print(segundo)  # 40

# Atividade 5: Ordenar lista de tuplas pelo nome
def ordenar_por_nome(lista_tuplas):
    return sorted(lista_tuplas, key=lambda x: x[0].lower())

pessoas = [
    ("Ana", 30),
    ("carlos", 25),
    ("Bruna", 22),
    ("davi", 28)
]
ordenadas = ordenar_por_nome(pessoas)
print(ordenadas)  # [('Ana', 30), ('Bruna', 22), ('carlos', 25), ('davi', 28)]
