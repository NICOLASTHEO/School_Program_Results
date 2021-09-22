# Com base nas 4 notas trimestrais de Um ALuno queremos a média desse aluno.

name=str(input("Informe o nome do/a Aluno/a: "))
a=float(input("nota {name} 1ª trimestre: ".format(name=name)))
if a > 10:
    a=float(input("Você digitou algo errado. Lance novamente a nota 1º trim: "))
b=float(input("nota {name} 2ª trimestre: ".format(name=name)))
if b >10:
    b=float(input("Você digitou algo errado. Lance novamente a nota 2ºtrim: "))   
c=float(input("nota {name} 3ª trimestre: ".format(name=name)))
if c>10:
    c=float(input("Você digitou algo errado. Lance novamente a nota 3º trim: "))
d=float(input("nota {name} 4ª trimestre: ".format(name=name)))
if d>10:
   d=float(input("Você digitou algo errado. Lance novamente a nota 4º trim: "))

media=(a + b + c + d)/4


if a>10 or b>10 or c>10 or d>10:
    print('alguma nota foi lançada errada, refaça o processo.')
else:
    print("a média {name} ".format(name=name) + str(media))
    if media >=7:
        print('Dê os parabéns para {name}'.format(name=name) + ", ano concluído com sucesso.")
    elif media >4:
        print('{name}'.format(name=name) + ", deve estudar mais, pois está de Recuperação.")
    else:
        print('Infelizmente {name}'.format(name=name) + ' REPROVOU de ano.')

    print("\n"'Estaremos aqui esperando ansiosamente pelo ano que vem! \n'
    "Nossa paixão é ensinar!")