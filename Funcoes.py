import re


def validar_entrada(valor):
    return len(valor.strip()) == 0 or not caracteres_permitidos(valor)


def caracteres_permitidos(valor):
    padrao = r"^[\w\s.,!?-]*$"
    return re.match(padrao, valor)


def inverter_palavras(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])


def remover_duplicados(sentence):
    unique_chars = ''.join(char for i, char in enumerate(sentence) if char not in sentence[:i])
    return unique_chars


def maior_palindrome(string):
    longest_palindrome = max((string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)
                              if string[i:j] == string[i:j][::-1]), key=len, default='')
    return longest_palindrome


def formatar_frase(frase):
    pontuacoes_conhecidas = ['.', '!', '?', ':']
    palavras = frase.lower().split()
    nova_frase = [palavra.capitalize() if (i == 0 or palavras[i - 1][-1] in pontuacoes_conhecidas) else palavra for
                  i, palavra in enumerate(palavras)]
    return ' '.join(nova_frase)


def anagrama_palindrome(string):
    char_count = {char: string.count(char) for char in set(string)}
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    return 'true' if odd_count <= 1 else 'false'
