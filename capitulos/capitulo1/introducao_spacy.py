# importando a biblioteca scaCY
import spacy


# Criar um objeto nlp vazio da lingua portuguesa
nlp = spacy.blank("pt")


# Criado após processar um texto com o objeto nlp
doc = nlp("Olá mundo!")

# Iterando nos tokens do doc
for token in doc:
    print(token.text)

# Indexar o Doc para obter um Token
token = doc[1]


# Obter o texto do token através do atributo.text
print(token.text)

# Um pedaço do Doc é um objeto Particao (Span)
span = doc[1:3]

# Obter o texto da particao com atributo text
print(span.text)

