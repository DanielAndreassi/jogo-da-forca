import random
des_forca = ['''
 +---+
 |   |
     |
     |
     |
     |   
=========''', '''
 +---+
 |   |
 O   |
     |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |    
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |    
=========
''']
# lista tec
professores_FIPP=['cristiane','fransisco','cezario','flavio','leandro']
linguagem_de_programacao=['javascript','python','java','php','typescript']

# lista conhecimentos gerais
carro=['fusca','opala','jetta','golf','corolla']
pais=['nova zelandia','vaticano','argelia','argentina','portugal']
alimento=['pizza','lasanha','macarrão','feijoada','churasco']

# dica computacao
dicasf=['jogo','fluxograma','pode pa','portas','alienigina']
dicasl=['front-end','facil','minecraft','full-stack','extensão do JavaScript']

dicasc=['indestrutivel','bebe muito','Volkswagen sedan','malandro',' carro de tio']
dicasp=['oceania','papa','deserto do saara','maradona','pastel de belem']
dicasa=['italia','camadas','domingo','feijão preto','sertanejo']

# variaves e array
palavra=''
sort=random.randint(0,4)  
jogo='s'
letras_usadas=''
chances=0
codificado=''
chutes=''
dica=''
pedirdica=''

# rep jogo
while jogo == 's':
    print('bem vindo ao jogo da forca\n')
    print('vamos as classes\n')
    print('computação-C\n')
    print('conhecimentos gerais-G\n')
    classe=input('qual classe voce deseja jogar? ').upper()
    # verificando classe
    if classe == 'C':
        print('agora vamos escolher a categoria\n')
        print('como voce escolheu a classe de computação temos como opções\n')
        print('Professores-FIPP-F')
        print('linguagens de programação-L\n')
        categoria=input('digite a categoria desejada ').upper()
        # verificando categoria
        if categoria == 'F':
            palavra=professores_FIPP[sort]
            codificado='_'*len(palavra)
            dica=dicasf[sort]
        if categoria == 'L':
            palavra=linguagem_de_programacao[sort]
            codificado='_'*len(palavra)
            dica=dicasl[sort]
    # verificando classe
    elif classe == 'G':
        print('agora vamos escolher a categoria\n')
        print('como voce escolheu a classe de conhecimentos gerais temos como opções\n')
        print('Carro-C\n')
        print('Pais-P\n')
        print('Alimento-A\n')
        categoria=input('digite a categoria desejada: ').upper()
        # verificando categoria
        if categoria == 'C':
            palavra=carro[sort]
            codificado='_'*len(palavra)
            dica=dicasc[sort]
        if categoria == 'P':
            palavra=pais[sort]
            dica=dicasp[sort]
            codificado='_'*len(palavra)
        if categoria == 'A':
            palavra=alimento[sort]
            codificado='_'*len(palavra)
            dica=dicasa[sort]
    # inicio jogo
    print('vamos ao jogo\n')
    print('voce tem apenas 1 dicas por rodada então use com sabedoria\n')
    while chances <=6:
        letra=input('digite uma letra: ').lower()
        indices=[]
        for i,a in enumerate(palavra):
            if a == letra:
                indices.append(i)
        if len(indices) > 0:
            for i in indices:
                codificado = codificado[:i] + letra + codificado[i + 1:]
        else:
            chances+=1
        letras_usadas=letras_usadas + ' ' +letra
        if chances == 0:
            print(des_forca[0])
        if chances == 1:
            print(des_forca[1])
        if chances == 2:
            print(des_forca[2])
        if chances == 3:
            print(des_forca[3])
        if chances == 4:
            print(des_forca[4])
            chute=input('deseja chutar a palavra?\n').lower()
            if chute == 's':
                chute=input('digite o chute')
                if chute == palavra:
                    print("Parabéns, você ganhou!")
                    print("          _____      ")
                    print("        '.=====.'     ")
                    print("     .-\\:      /-.    ")
                    print("    | (|:.     |) |    ")
                    print("     '-|:.     |-'     ")
                    print("       \\::.    /      ")
                    print("        '::. .'        ")
                    print("          ) (          ")
                    print("        .' '.        ")
                    print("       '-------'       ")
                    jogo=input('deseja jogar novamente?').lower()
                    break
                else:
                    print('voce errouuuu!!!')
                    jogo=input('deseja jogar novamente?').lower()
                    break
        if chances == 5:
            print(des_forca[5])
        if chances == 6:
            print(des_forca[6])
            print("VOCE PERDEU")
            jogo=input('deseja jogar de novo?-S\n').lower()
            break
        if codificado == palavra:
            print("Parabéns, você ganhou!")
            print("          _____      ")
            print("        '.=====.'     ")
            print("     .-\\:      /-.    ")
            print("    | (|:.     |) |    ")
            print("     '-|:.     |-'     ")
            print("       \\::.    /      ")
            print("        '::. .'        ")
            print("          ) (          ")
            print("         .' '.        ")
            print("       '-------'       ")
            print('a palavra correta')
            jogo=input('deseja jogar novamete?')
            break   
        print(codificado)
        print('letras usadas',letras_usadas)
        pedirdica=input('deseja usar a sua dica?').lower()
        if pedirdica == 's':
            print(dica)
print('OBRIGADO POR JOGAR')