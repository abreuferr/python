# AUTORES    : Caio Abreu Ferreira <abreuferr (a) gmail.com>
# DESCRIÇÃO  : programa utilizado para verificar se o texto eh um plagio ou nao

#
# funcoes fornecidas pelo curso
#

import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

# A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
def separa_sentencas(texto):  
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

# A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

# A funcao recebe uma frase e devolve uma lista das palavras dentro da frase
def separa_palavras(frase):  
    return frase.split()

# Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez
def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

# Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas
def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

#
# funcoes desenvolvidas pelo programador
#

# IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
def compara_assinatura(as_a, as_b):
    wal_total = as_a[0] - as_b[0]
    ttr_total = as_a[1] - as_b[1]
    hlr_total = as_a[2] - as_b[2]
    sal_total = as_a[3] - as_b[3]
    sac_total = as_a[4] - as_b[4]
    pal_total = as_a[5] - as_b[5]

    sab = (wal_total - ttr_total - hlr_total - sal_total - sac_total - pal_total) / 6

    return sab

# IMPLEMENTADO. Essa funcao recebe um texto e deve devolver a assinatura do texto.
def calcula_assinatura(texto):
    # chamada da funcao para calcular o tamanho medio das palavras
    wal = tamanho_medio_palavra(texto)

    # chamada da funcao para calcular a relacao type token
    ttr = relacao_type_token(texto)

    # chamada da funcao para calcular a relacao hapax legomana
    hlr = relacao_hapax_legomana(texto)

    # chamada da funcao para calcular o tamanho medio sentenca
    sal = tamanho_medio_sentenca(texto)

    # chamada da funcao para calcular a complexidade media da sentenca
    sac = complexidade_media_sentenca(texto)

    # chamada da funcao para calcular o tamanho medio frase
    pal = tamanho_medio_frase(texto)

    return [wal, ttr, hlr, sal, sac, pal]

# IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.
def avalia_textos(textos, ass_cp):
    pass

#
# funcoes utilizadas para calcular os tracos linguisticos de um texto.
#

# WAL - funcao utilizada para calcular o tamanho medio das palavras do texto.
# Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
def tamanho_medio_palavra(texto):
    # definico das variaveis.
    tamanho_palavras = 0
    caractere_indesejado = 0

    # enviar as palavras do texto para uma lista de nome lista_palavras.
    # atraves da funcao separa_palavras()
    lista_palavras = separa_palavras(texto)

    # contar a quantidade de palavras presentes na lista lista_palavras.
    numero_palavras = len(lista_palavras)

    # varrer a lista lista_palavras para calcular o tamanho das palavras.
    for i in lista_palavras:
        # calcular a quantidade de letras presentes em cada palavra do lista_palavras e
        # armazena o valor total de letras presentes no texto.
        tamanho_palavras = tamanho_palavras + len(i)

    # varrer a lista lista_palavras a procura de caracteres.
    for k in lista_palavras:
        # verificar se o caractere eh um caractere indesejado.
        if ( '.' in k or ',' in k or ';' in k  or " " in k or "'" in k or "'" in k or ':' in k or "!" in k or '?' in k or "..." in k):
            # calcular a quantidade de caracters presentes na lista lista_palavras.
            caractere_indesejado = caractere_indesejado + 1

    # calcular o valor WAL
    wal = (tamanho_palavras - caractere_indesejado) / numero_palavras

    return wal

# TTR - funcao utilizada para calcular a relacao type-token do texto.
# Relacao Type-Token eh o numero de palavras diferentes dividido pelo numero total de palavras.
def relacao_type_token(texto):
    # atraves da funcao separa_palavra, o texto eh inserido em uma lista.
    # essa lista eh enviada para a funcao n_palavras_diferentes para calcular
    # a frequencia com que as palavras se repetem.
    numero_palavras_diferentes = n_palavras_diferentes(separa_palavras(texto))

    # calcular o valor TTR                      
    ttr = numero_palavras_diferentes / len(separa_palavras(texto))
    return(ttr)   

# HLR - funcao utilizada para calcular a relacao hapax legomana do texto.
# Razao Hapax Legomana eh o numero de palavras que aparecem uma unica vez dividido pelo total de palavras.
def relacao_hapax_legomana(texto):
    # calcular o valor de HLR
    hlr = n_palavras_unicas(separa_palavras(texto))/len(separa_palavras(texto))
    
    return hlr

# SAL - funcao utilizada para calcular o tamanho medio da sentenca do texto.
# Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças.
def tamanho_medio_sentenca(texto):
    # definicao das variaveis
    numero_caractere = 0
    
    # calcular o numero de sentencas que o texto possui
    lista_sentencas = separa_sentencas(texto)
    numero_sentencas = len(lista_sentencas)

    # obter as palavras 
    lista_palavras = separa_palavras(texto)

    # calcular o numero de caracteres que o texto possui.
    for i in lista_palavras:
        numero_caractere = numero_caractere + len(i)

    # calcular valor de SAL.
    sal = numero_caractere / numero_sentencas

    return sal

# SAC - funcao utilizada para calcular a complexidade medio da sentenca do texto.
# Complexidade de sentença eh o numero total de frases divido pelo numero de sentencas.
def complexidade_media_sentenca(texto):

    # calcula valor de SAC
    sac = len(separa_frases(texto)) / len(separa_sentencas(texto))

    return (sac)

# PAL - funcao utilizada para calcular o tamanho medio da frase do texto.
# Tamanho médio de frase = (soma do número de caracteres em cada frase) / (número de frases no texto).
def tamanho_medio_frase (texto):
    # definicao das variaveis.
    numero_caracteres = 0
    caractere_indesejado = 0

    # obter o numero de frases do texto.
    numero_frases = len(separa_frases(texto))

    # obter o numero de caracteres que as fases possuem.
    lista_palavras = separa_palavras(texto)
    for i in lista_palavras:
        numero_caracteres = numero_caracteres + len(i)

        # verificar se o caractere eh um caractere indesejado, ','.
        if (',' in i):
            # calcular a quantidade de caracters presentes na lista lista_palavras.
            caractere_indesejado = caractere_indesejado + 1

    # calcular valor de PAL
    pal = (numero_caracteres - caractere_indesejado) / numero_frases

    return pal

#
# funcao main()
#

#### IMPLEMENTADO ####

# texto para trabalho.
#texto_a = "Navegadores antigos tinham uma frase gloriosa: Navegar é preciso; viver não é preciso. Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade. É a forma que em mim tomou o misticismo da nossa Raça."
#texto_b = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."

# calcular os valores do traco linguistico dos textos texto_a e texto_b. 
#as_a = calcula_assinatura(texto_a)
#as_b = calcula_assinatura(texto_b)

# compara a similaridade dos textos.
#compara_assinatura(as_a, as_b)

#### IMPLEMENTADO ####
# texto para trabalho.

# type-token esperado: 0.743; recebido: 0.7567567567567568
texto = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."

# tam. médio palavra esperado: 4.507; recebido: 4.523809523809524
#texto = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."

# tam. médio palavra esperado: 4.409; recebido: 4.869565217391305
#texto = "Navegadores antigos tinham uma frase gloriosa: Navegar é preciso; viver não é preciso .Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."

# calcular os valores do traco linguistico do texto e exibir esses valores.
assinatura_texto = calcula_assinatura(texto)

print(assinatura_texto)

#### IMPLEMENTADO ####
# texto para trabalho.
#texto_1 = "Navegadores antigos tinham uma frase gloriosa: Navegar é preciso; viver não é preciso. Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade. É a forma que em mim tomou o misticismo da nossa Raça."
#texto_2 = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."
#texto_3 = "Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto"