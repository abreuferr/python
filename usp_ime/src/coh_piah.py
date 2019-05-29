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
# funcoes utilizadas para calcular os tracos linguisticos de um texto.
#

# WAL - funcao utilizada para calcular o tamanho medio das palavras do texto.
# Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.
def tamanho_medio_palavra(texto):
    # array e variavel auxiliar
    frases = []
    palavras = []
    soma_caracteres_sentenca = 0
    soma_caracteres_frase = 0
    soma_palavra = 0

    # 1 - do texto, separar as sentencas.
    sentencas = separa_sentencas(texto)

    # 2 - das sentenca, separar as frases.
    for sentenca in sentencas:      
        soma_caracteres_sentenca = soma_caracteres_sentenca + len(sentenca)
        n_frases = separa_frases(sentenca)

        for f in n_frases:
            frases.append(f)
    
    # 3 - das frases, separar as palavras.
    for frase in frases:
        soma_caracteres_frase = soma_caracteres_frase + len(frase)
        n_palavras = separa_palavras(frase)

        for palavra in n_palavras:
            palavras.append(palavra)    

    for palavra in palavras:
        soma_palavra = soma_palavra + len(palavra)

    wal = soma_palavra / len(palavras)

    return wal

# TTR - funcao utilizada para calcular a relacao type-token do texto.
# Relacao Type-Token eh o numero de palavras diferentes dividido pelo numero total de palavras.
def relacao_type_token(texto):
    # array e variavel auxiliar
    frases = []
    palavras = []
    soma_caracteres_sentenca = 0
    soma_caracteres_frase = 0
    soma_palavra = 0

    # 1 - do texto, separar as sentencas.
    sentencas = separa_sentencas(texto)

    # 2 - das sentenca, separar as frases.
    for sentenca in sentencas:      
        soma_caracteres_sentenca = soma_caracteres_sentenca + len(sentenca)
        n_frases = separa_frases(sentenca)

        for f in n_frases:
            frases.append(f)
    
    # 3 - das frases, separar as palavras.
    for frase in frases:
        soma_caracteres_frase = soma_caracteres_frase + len(frase)
        n_palavras = separa_palavras(frase)

        for palavra in n_palavras:
            palavras.append(palavra)

    # calcular o valor TTR          
    ttr = n_palavras_diferentes(palavras) / len(palavras)

    return(ttr)   

# HLR - funcao utilizada para calcular a relacao hapax legomana do texto.
# Razao Hapax Legomana eh o numero de palavras que aparecem uma unica vez dividido pelo total de palavras.
def relacao_hapax_legomana(texto):
        # array e variavel auxiliar
    frases = []
    palavras = []
    soma_caracteres_sentenca = 0
    soma_caracteres_frase = 0
    soma_palavra = 0

    # 1 - do texto, separar as sentencas.
    sentencas = separa_sentencas(texto)

    # 2 - das sentenca, separar as frases.
    for sentenca in sentencas:      
        soma_caracteres_sentenca = soma_caracteres_sentenca + len(sentenca)
        n_frases = separa_frases(sentenca)

        for f in n_frases:
            frases.append(f)
    
    # 3 - das frases, separar as palavras.
    for frase in frases:
        soma_caracteres_frase = soma_caracteres_frase + len(frase)
        n_palavras = separa_palavras(frase)

        for palavra in n_palavras:
            palavras.append(palavra)

    # calcular o valor de HLR
    hlr = n_palavras_unicas(palavras)/len(palavras)
    
    return hlr

# SAL - funcao utilizada para calcular o tamanho medio da sentenca do texto.
# Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças.
def tamanho_medio_sentenca(texto):
    # array e variavel auxiliar
    frases = []
    soma_caracteres_sentenca = 0

    # 1 - do texto, separar as sentencas.
    sentencas = separa_sentencas(texto)

    # 2 - das sentenca, separar as frases.
    for sentenca in sentencas:      
        soma_caracteres_sentenca = soma_caracteres_sentenca + len(sentenca)
        n_frases = separa_frases(sentenca)

        for f in n_frases:
            frases.append(f)

    # calcular valor de SAL.
    sal = soma_caracteres_sentenca / len(sentencas)

    return sal

# SAC - funcao utilizada para calcular a complexidade medio da sentenca do texto.
# Complexidade de sentença eh o numero total de frases divido pelo numero de sentencas.
def complexidade_media_sentenca(texto):
        # array e variavel auxiliar
    frases = []
    palavras = []
    soma_caracteres_sentenca = 0
    soma_caracteres_frase = 0
    soma_palavra = 0

    # 1 - do texto, separar as sentencas.
    sentencas = separa_sentencas(texto)

    # 2 - das sentenca, separar as frases.
    for sentenca in sentencas:      
        soma_caracteres_sentenca = soma_caracteres_sentenca + len(sentenca)
        n_frases = separa_frases(sentenca)

        for f in n_frases:
            frases.append(f)
    
    # 3 - das frases, separar as palavras.
    for frase in frases:
        soma_caracteres_frase = soma_caracteres_frase + len(frase)
        n_palavras = separa_palavras(frase)

        for palavra in n_palavras:
            palavras.append(palavra)    

    # calcula valor de SAC
    sac = len(frases) / len(sentencas)

    return (sac)

# PAL - funcao utilizada para calcular o tamanho medio da frase do texto.
# Tamanho médio de frase = (soma do número de caracteres em cada frase) / (número de frases no texto).
def tamanho_medio_frase (texto):
    # array e variavel auxiliar
    frases = []
    palavras = []
    soma_caracteres_sentenca = 0
    soma_caracteres_frase = 0
    soma_palavra = 0

    # 1 - do texto, separar as sentencas.
    sentencas = separa_sentencas(texto)

    # 2 - das sentenca, separar as frases.
    for sentenca in sentencas:      
        soma_caracteres_sentenca = soma_caracteres_sentenca + len(sentenca)
        n_frases = separa_frases(sentenca)

        for f in n_frases:
            frases.append(f)
    
    # 3 - das frases, separar as palavras.
    for frase in frases:
        soma_caracteres_frase = soma_caracteres_frase + len(frase)
        n_palavras = separa_palavras(frase)

        for palavra in n_palavras:
            palavras.append(palavra)
    
    # calcular valor de PAL
    pal = soma_caracteres_frase / len(frases)

    return pal

#
# funcoes desenvolvidas pelo programador
#

# Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade 
# nas assinaturas.
def compara_assinatura(as_a, as_b):
    # variavel auxiliar.
    soma_temporaria = 0
    sab = 0

    # soma temporaria = somatoria(fia - fib)
    for i in range(0,6):
        soma_temporaria = soma_temporaria + (abs(as_a[i] - as_b[i]))
    
    # calcula o valor de sab que eh a SOMATORIA dos varios valores
    # de soma_temporaria.
    sab = soma_temporaria / 6

    # retorna com o valor de sab.
    return sab

# Essa funcao recebe um texto e deve devolver a assinatura do texto.
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

# Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com 
# maior probabilidade de ter sido infectado por COH-PIAH.
def avalia_textos(textos, ass_cp):
    # os resultados das analises dos 03 textos serao armazenados no array ASS.
    ass = []

    # existem 03 textos dentro da variavel TEXTOS, entao eh necessario calcular a 
    # assinatura de cada texto.
    for texto in textos:
        # calcula as assinaturas dos 03 textos presentes na variavel TEXTOS.
        assinatura_texto = calcula_assinatura(texto)
        # chamada da funcao compara_assinatura e armazena os resultados no array ASS.
        ass.append(compara_assinatura(assinatura_texto, ass_cp))

    # comparar os 03 textos e encontrar o texto infectado
    menor = ass[0]
    texto_infectado = 1

    # for para identificar qual eh o texto infectado.
    for i in range(1, len(ass)):
        if (menor < ass[i]):
            texto_infectado = i
    
    # retornar para a funcao main() com a identificacao
    # do texto infectado.
    return texto_infectado

#
# funcao main()
#
def main():

    # texto para trabalho.
    texto = "NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência."
    # calcular os valores do traco linguistico do texto e exibir esses valores.
    assinatura_texto = calcula_assinatura(texto)

    # 03 textos.
    textos = ['Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.', 'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.', 'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.']
    # 01 assinatura.
    ass_cp = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
    texto_infectado = avalia_textos(textos,ass_cp)

    # exibe uma mensagem indicando qual eh o texto que esta contaminado.
    print("O autor do texto {} está infectado com COH-PIAH".format(texto_infectado))

    main()