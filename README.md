# Manipulação de Strings em Python

Este repositório contém a resolução dos exercícios de manipulação de strings usando a linguagem Python (versão 3.8.5).

## Menu

- ### [Classe e Funções da aplicação](#modulos-e-funções)
- ### [Interface da aplicação](#interface)
- ### [Funções da aplicação:](#funções-disponíveis)
- ### [Testes com Unittest](#testes)
- ### [Executar a aplicação](#execução)
- ### [Observações da aplicação](#observações)

## Modulos e Funções

- `TelaApp.py`: Modulo que define a interface principal do programa.
- `executar_exercicio`: Função que executa o exercício selecionado com a entrada fornecida.
- `inverter_palavras`: Função que reverte a ordem das palavras em uma frase.
- `remover_duplicados`: Função que remove caracteres duplicados de uma string.
- `maior_palindrome`: Função que encontra a substring palindrômica mais longa em uma string.
- `formatar_frase`: Função que coloca em maiúscula a primeira letra de cada frase em uma string.
- `anagrama_palindrome`: Função que verifica se uma string é um anagrama de um palíndromo.

## Interface

A interface principal do programa é definida pela modulo `TelaApp.py`. Nesta interface, é possível selecionar um
exercício e inserir uma entrada para executá-lo alem de poder realizar os testes do modulo `FuncoesTest.py`.

<img src='/IMG/TelaApp.png' alt="Tela Inicio" width="598" height="328" title="Tela">

## Funções Disponíveis

- #### [`Inverter Palavras`](#reverter-a-ordem-das-palavras)[`Remover Duplicados`](#remover-caracteres-duplicados)[`Maior Palindrome`](#encontrar-a-substring-palindrômica)[`Formatar Frase`](#colocar-em-maiúscula-a-primeira-letra-de-cada-frase)[`Anagrama Palindrome`](#verificar-se-é-um-anagrama-de-um-palíndromo)

1. ### **Validar Entrada do usuario**:
    - **Função:** `validar_entrada(valor)`
    - **Descrição:** Esta função verifica se um valor de entrada é válido. Ela conta com uma função Auxiliar `caracteres_permitidos` para verificar a presença de caracteres permitidos. Ela recebe um valor como entrada e retorna
      `True` se o valor for inválido e `False` se o valor for válido. Um valor é considerado inválido se comprimento for igual a ***zero*** ou se não conter caracteres permitidos.
   
    ```python
    def validar_entrada(valor):
        return len(valor.strip()) == 0 or not caracteres_permitidos(valor)


    def caracteres_permitidos(valor):
        padrao = r"^[\w\s.,!?-]*$"
        return re.match(padrao, valor)
    ```

2. ### **Reverter a ordem das palavras**:
    - **Função:** `inverter_palavras(sentence)`
    - **Descrição:** Esta função inverte a ordem das palavras em uma frase. Ela recebe uma frase como entrada e retorna
      a frase com as palavras invertidas.
   ```python
      def inverter_palavras(sentence):
            words = sentence.split()
            reversed_words = ' '.join(words[::-1])
            return reversed_words
   ```

3. ### **Remover caracteres duplicados**:
    - **Função:** `remover_duplicados(sentence)`
    - **Descrição:** Esta função remove todos os caracteres duplicados de uma frase. Ela recebe uma frase como entrada
      e retorna uma nova frase com os caracteres duplicados removidos.
   ```python
      def remover_duplicados(string):
            unique_chars = ''.join(char for i, char in enumerate(string) if char not in string[:i])
            return unique_chars
   ```

4. ### **Encontrar a substring palindrômica**:
    - **Função:** `maior_palindromo(string)`
    - **Descrição:** Esta função encontra a maior substring palindrômica em uma string. Ela verifica todas as substrings
      possíveis na string de entrada e retorna a maior substring que é um palíndromo. Um palíndromo é uma sequência de
      caracteres que permanece a mesma quando lida da esquerda para a direita e da direita para a esquerda.
   ```python
      def maior_palindromo(string):
            longest_palindromo = max((string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1)
                              if string[i:j] == string[i:j][::-1]), key=len, default='')
            return longest_palindromo
   ```

5. ### **Colocar em maiúscula a primeira letra de cada frase**:
    - **Função:** `formatar_frase(frase)`
    - **Descrição:** Esta função coloca em maiúscula a primeira letra de cada palavra em uma frase. Ela recebe uma frase
      contendo uma ou mais palavras e retorna a mesma frase, mas com a primeira letra de cada palavra convertida para
      maiúscula. As palavras são identificadas com base em pontuações como ponto final (.), ponto de exclamação (!),
      ponto
      de interrogação (?) e dois pontos (:).
   ```python
      def formatar_frase(frase):
            pontuacoes_conhecidas = ['.', '!', '?', ':']
            palavras = frase.split()
            nova_frase = [palavra.capitalize() if (i == 0 or palavras[i - 1][-1] in pontuacoes_conhecidas) else palavra for
                           i, palavra in enumerate(palavras)]
            return ' '.join(nova_frase)
   ```

6. ### **Verificar se é um anagrama de um palíndromo**:
    - **Função:** `anagrama_palindromo(string)`
    - **Descrição:** Esta função verifica se uma string é um anagrama de um palíndromo. Ela recebe uma string como
      entrada e determina se a string pode ser rearranjada de tal forma que forme um palíndromo. Para isso, ela verifica
      se todos os caracteres na string têm um número par de ocorrências, com exceção de no máximo um caractere, que pode
      ter um número ímpar de ocorrências. A função retorna ***"true"*** se a string for um anagrama de um palíndromo e
      ***"
      false"*** caso contrário.
   ```python
      def anagrama_palindromo(string):
            char_count = {char: string.count(char) for char in set(string)}
            odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
            return 'true' if odd_count <= 1 else 'false'
   ```

## Testes

Os testes para as funções de manipulação de strings foram implementados na classe `MyTestCase` utilizando a biblioteca
de testes `unittest`. Os testes verificam se as funções estão produzindo os resultados esperados.

**Importando funções da classe Funcoes:**

   ```python
   from Funcoes import inverter_palavras, remover_duplicados, maior_palindromo, anagrama_palindromo, formatar_frase
   ```

1. **Reverter a ordem das palavras:**
   ```python
      def test_inverter_palavras(self):
            self.assertEqual(inverter_palavras("Hello, World! OpenAI is amazing."),
                         "amazing. is OpenAI World! Hello,")
   ```

2. **Remover caracteres duplicados:**
   ```python
      def test_remover_duplicados(self):
            self.assertEqual(remover_duplicados("Hello, World!"), "Helo, Wrd!")
   ```

3. **Encontrar a substring palindrômica**:
   ```python
      def test_maior_palindromo(self):
            self.assertEqual(maior_palindromo("babad"), "bab")
   ```

4. **Colocar em maiúscula a primeira letra de cada frase**:
   ```python
      def test_capitalize_frase(self):
            self.assertEqual(formatar_frase("hello. how are you? i'm fine, thank you."),
                        "Hello. How are you? I'm fine, thank you.")
   ```

5. **Verificar se é um anagrama de um palíndromo**:
   ```python
      def test_anagrama_palindromo(self):
            self.assertEqual(anagrama_palindromo("racecar"), "true")
   ```

## Execução

* Sites Externos : [`myCompiler`](https://www.mycompiler.io/view/LTQTMygLH8s) [`Google Colab`](https://colab.research.google.com/drive/1oQ5LlPIqKyOsuIxpS_pwFz0vTnjMr2TL?usp=sharing)
  * #### ***Observação: Os exercicios apresentados nos sites acima foram devidamente alterados para ser executado no ambiente disponivel no site.***

* Clone esse repositorio em sua maquina e execute a classe **TelaApp.py** na sua **IDE** Favorita.
* Execute o arquivo `TelaApp.exe` localizado em **/dist/TelaApp.exe**.


Certifique-se de ter o Python (versão 3.8.5) ou supeior e as dependências necessárias instaladas no ambiente.

## Observações

* ### *Nessa Aplicação foi usado o Tkinter para a criação da Interfaçe grafica e o Pyinstaller para criar o executavel*

    -
        * Tkinter: O Tkinter é uma biblioteca padrão do Python para criação de interfaces gráficas. Não são necessárias
          dependências adicionais para usar o Tkinter, pois ele vem pré-instalado com o Python. Ele oferece uma ampla
          gama de
          recursos para criar aplicativos com interfaces de usuário interativas.<br><br>

    -
        * Pyinstaller: O PyInstaller é uma ferramenta usada para criar executáveis independentes de plataformas para
          aplicativos
          Python. Ele permite empacotar um programa Python junto com todas as suas dependências em um único arquivo
          executável,
          tornando mais fácil distribuir e executar o aplicativo em diferentes sistemas operacionais sem a necessidade
          de
          instalar o Python ou quaisquer bibliotecas adicionais.
    -
        * Para instalar o Pyinstaller execute `pip install pyinstaller`


* As classes e funções estão definidas em arquivos separados, conforme a organização recomendada.


* O programa utiliza a formatação de strings do Python para manipulação de textos.


* Os exercícios estão implementados utilizando abordagens simples e eficientes.


* Os testes foram implementados para garantir o correto funcionamento das funções de manipulação de strings.


* Para todos os itens foi presumido que a string de entrada conterá apenas caracteres alfabéticos, espaços e sinais de
  pontuação.


* A saída para cada tarefa foi retornada como uma string.
