# Capitulo 1

## O objeto nlp

No cerne da spaCy está o objeto nlp, que contém o fluxo de processamento. Por convenção, normalmente chamamos essa variável de "nlp".

Como exemplo, para criar o objeto nlp em inglês, importamos a biblioteca spacy e usamos spacy.blank para criar um fluxo de processamento (pipeline) vazio. Podemos utilizar o objeto nlp como se chamássemos uma função para analisar textos.

O objeto contém os diferentes componentes do fluxo de processamento do texto.

Ele também contém regras específicas de cada idioma para a toquenização do texto em palavras e pontuação. A spaCy oferece suporte para diversos idiomas.

## O objeto Doc

Quando você processa um texto com o objeto nlp, a spaCy cria um objeto Doc- abreviação de "documento". Através do Doc é possível acessar informações do texto de uma maneira estruturada, sendo que nenhuma informação é perdida.

O Doc se comporta de maneira semelhante a uma sequência do Python, permitindo a iteração nos tokens e o acesso a um token através do seu índice. Mas falaremos disso mais tarde!

## O objeto Token

O objeto Token representa uma parte do texto: uma palavra ou um caracter de pontuação.

Para acessar um token em uma posição específica, você pode indexar o objeto Doc.

Os objetos Token também contêm vários atributos que permitem acessar mais informações sobre os tokens. Por exemplo: o atributo .text retorna o texto verbatim.


## O objeto Partição (Span)

Um objeto partição Span é uma partição do documento consistindo de um ou mais tokens. É apenas um apontamento para o Doc e não contém dados em si mesmo.

Para criar uma partição, você pode usar a notação de partição do Python. Por exemplo, 1:3 criará uma partição do token na posição 1 até o token na partição 3, mas não incluindo este último.


## Atributos léxicos

Aqui você pode observar alguns dos atributos dos tokens disponíveis :

i é o índice do token no documento principal.

text retorna o texto do documento.

is_alpha, is_punct e like_num retornam valores boleanos (verdadeiro ou falso) indicando respectivamente se o token tem caracteres alfabéticos, se é uma pontuação ou se assemelha-se a um número, por exemplo, o token "10" – um, zero – ou a palavra "dez" – D,E,Z.

Esses atributos são também chamados de atributos léxicos: referem-se ao token em si e não dependem de nenhum contexto no qual o token está inserido.

## Fluxos (pipelines) de processamento treinados

### O que são fluxos (pipelines) de processamento treinados ?

Modelos que permitem que a spaCy faça previsões de atributos linguísticos em contexto:

-   Marcadores de classes gramaticais
-   Dependências sintáticas
-   Entidades nomeadas
    
-> São treinados com exemplos de textos rotulados.

-> Podem ser atualizados com mais exemplos para um ajuste fino das previsões.

```text
Algumas das análises mais interessantes são aquelas específicas a um contexto. Por exemplo: se uma palavra é um verbo ou se uma palavra é o nome de uma pessoa.

Os fluxos (pipelines) de processamento possuem modelos estatísticos que permitem que a spaCy faça previsões dentro de um contexto. Isso normalmente inclui marcadores de classes gramaticais, dependências sintáticas e entidades nomeadas.

Os fluxos (pipelines) de processamento são treinados em grandes conjuntos de dados com textos de exemplos já rotulados.

Os modelos podem ser atualizados com mais exemplos para fazer um ajuste fino nas previsões, como por exemplo, melhorar os resultados em um conjunto de dados específico.

```

### Pacotes dos fluxos (pipelines) de processamento


    Pesos binários
    Vocabulário
    Metadados
    Arquivo de configuração

A biblioteca spaCy oferece vários pacotes de fluxos (pipelines) de processamento que você pode baixar usando o comando spacy download. Por exemplo, o pacote "en_core_web_sm" é um fluxo de processamento pequeno em inglês que foi treinado com texto da internet e possui diversos recursos.

O método spacy.load carrega o pacote de um fluxo (pipeline) de processamento a partir do seu nome e retorna um objeto nlp.

O pacote contém os pesos binários que permitem que a spaCy faça as previsões.

Também inclui o vocabulário, metadados com informações sobre o fluxo (pipeline) de processamento e um arquivo de configuração utilizado para treiná-lo. Ele informa qual o idioma a ser utilizado e como configurar o fluxo de processamento (pipeline).


### Previsão dos marcadores de classe gramatical

Vamos dar uma olhada nas previsões do modelo. Neste exemplo, estamos usando a spaCy para prever as classes gramaticais, que são os tipos de palavras em seu contexto.

Primeiramente, carregamos o fluxo(pipeline) de processamento pequeno do Inglês no objeto nlp.

Em seguida, processamos o texto: "She ate the pizza".

Para cada token no doc, podemos imprimir o texto e o atributo .pos_, que é a classe gramatical prevista.

Na spaCy, atributos que retornam strings normalmente terminam com um sublinhado (underscore) e atributos sem o sublinhado retornam um inteiro.

Neste exemplo, o modelo previu corretamente "ate" como um verbo e "pizza" como um substantivo.


### Previsão de termos sintáticos

Em adição à previsão de classes gramaticais, podemos prever como as palavras estão relacionadas. Por exemplo, se uma palavra é o sujeito ou o predicado de uma sentença.

O atributo .dep_ retorna o marcador de dependência (ou termo sintático) previsto.

O atributo .head retorna o índice do token principal. Você pode pensar nele como o "pai" ao qual a palavra está conectada.

### Esquema dos marcadores de dependência ou termos sintáticos


Para descrever as dependências sintáticas, a spaCy usa um esquema com marcadores padronizados. Esse é um exemplo dos marcadores mais comuns:

O pronome (pronoun) "She" é um sujeito simples (nominal subject) relacionado com um verbo (verb), neste exemplo "ate".

O substantivo (noun) "pizza" é um objeto direto (direct object) relacionado ao verbo (verb) "ate". Ela é "eaten" pelo sujeito "she".

O adjunto adnominal (determiner) "the" está relacionado ao substantivo (noun) "pizza".


### Previsão de Entidades Nomeadas

Entidades nomeadas são "objetos do mundo real" que possuem um nome. Por exemplo: uma pessoa, uma organização ou um país.

A propriedade doc.ents permite o acesso às entidades nomedas identificadas (previstas) pelo modelo de reconhecimento de entidades nomeadas

Ela retorna um iterável de objetos do tipo Span, possibilitando o acesso ao texto e ao marcador através do atributo .label_.

Neste caso, o modelo previu corretamente "Apple" como uma organização, "U.K." como uma entidade geopolítica e "$1 billion" como dinheiro.


### Dica: o método spacy.explain

Uma dica: Para obter a definição dos marcadores mais comuns, você pode usar a função auxiliar spacy.explain.

Por exemplo, a sigla "GPE" para entidade geopolítica (geopolitical entity) não é muito intuitiva, mas o comando spacy.explain irá lhe explicar que se refere a países, cidades e estados.

O mesmo vale para marcadores de classes gramaticais e termos sintáticos.


