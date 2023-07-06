def inverter_palavras(sentence):
    words = sentence.split()
    reversed_words = ' '.join(words[::-1])
    return reversed_words


def remover_duplicados(string):
    unique_chars = ''.join(char for i, char in enumerate(string) if char not in string[:i])
    return unique_chars


def maior_palindrome(string):
    longest_palindrome = max((string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)
                              if string[i:j] == string[i:j][::-1]), key=len, default='')
    return longest_palindrome


def capitalize_frase(string):
    sentences = string.split('. ')
    capitalized_sentences = [sentence.capitalize() for sentence in sentences if sentence]
    return '. '.join(capitalized_sentences)


def anagrama_palindrome(string):
    char_count = {char: string.count(char) for char in set(string)}
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    return 'true' if odd_count <= 1 else 'false'
