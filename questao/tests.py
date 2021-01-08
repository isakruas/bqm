import requests

headers = {'Authorization': 'Token 299d40e62de6311775a2b246f735b0a11ee4c264'}
url = 'http://bq.mat.br/api/v1/questao/'

a = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 101,
    "nivel_de_dificuldade": 1,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=a)
    print(f'a - {i}')
    i = i + 1

b = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 101,
    "nivel_de_dificuldade": 2,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=b)
    print(f'b - {i}')
    i = i + 1

c = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 101,
    "nivel_de_dificuldade": 3,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=c)
    print(f'c - {i}')
    i = i + 1

d = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 102,
    "nivel_de_dificuldade": 1,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=d)
    print(f'd - {i}')
    i = i + 1

e = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 102,
    "nivel_de_dificuldade": 2,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=e)
    print(f'e - {i}')
    i = i + 1

f = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 102,
    "nivel_de_dificuldade": 3,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=f)
    print(f'f - {i}')
    i = i + 1

g = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 103,
    "nivel_de_dificuldade": 1,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=g)
    print(f'g - {i}')
    i = i + 1

h = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 103,
    "nivel_de_dificuldade": 2,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=h)
    print(f'h - {i}')
    i = i + 1

j = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 103,
    "nivel_de_dificuldade": 3,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=j)
    print(f'j - {i}')
    i = i + 1

k = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 104,
    "nivel_de_dificuldade": 1,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=k)
    print(f'k - {i}')
    i = i + 1

l = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 104,
    "nivel_de_dificuldade": 2,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=l)
    print(f'l - {i}')
    i = i + 1

m = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 104,
    "nivel_de_dificuldade": 3,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=m)
    print(f'm - {i}')
    i = i + 1

n = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 105,
    "nivel_de_dificuldade": 1,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=n)
    print(f'n - {i}')
    i = i + 1

o = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 105,
    "nivel_de_dificuldade": 2,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=o)
    print(f'o - {i}')
    i = i + 1

p = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 105,
    "nivel_de_dificuldade": 3,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=p)
    print(f'p - {i}')
    i = i + 1

q = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 106,
    "nivel_de_dificuldade": 1,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=q)
    print(f'q - {i}')
    i = i + 1

r = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 106,
    "nivel_de_dificuldade": 2,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=r)
    print(f'r - {i}')
    i = i + 1

s = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 106,
    "nivel_de_dificuldade": 3,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=s)
    print(f's - {i}')
    i = i + 1

u = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 107,
    "nivel_de_dificuldade": 1,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=u)
    print(f'u - {i}')
    i = i + 1

x = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 107,
    "nivel_de_dificuldade": 2,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=x)
    print(f'x - {i}')
    i = i + 1

y = {
    "status": 2,
    "etapa": 5,
    "ano": 6,
    "unidade_tematica": 26,
    "objeto_de_conhecimento": 107,
    "nivel_de_dificuldade": 3,
    "imagem": 0,
    "pergunta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "resposta": "Para fazer traduções de textos para o inglês, um tradutor \\(A\\)cobra um valor inicial de R$ 16,00 mais R$0,78 por linha traduzida, e um outro tradutor, \\(B\), cobra um valor inicial de R$ 28,00 mais R$ 0,48 por linha traduzida. Qual a quantidade mínima de linhas de um texto a ser traduzido para o inglês, de modo que o custo seja menor se for realizado pelo tradutor \\(B\)?",
    "cadastro_pelo_usuario": 5
}

i = 0
while i < 100:
    requests.post(url=f'{url}', headers=headers, data=y)
    print(f'y - {i}')
    i = i + 1
