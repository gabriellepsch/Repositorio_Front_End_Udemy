import re

def verifica_cpf(num_cpf):    
    regex = r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$'
    return re.fullmatch(regex, num_cpf) is not None


def converte_cpf() 
while True:
    num_cpf = input('Digite o CPF a ser verificado: ')
    resultado = verifica_cpf(num_cpf)
    if resultado:
        print (f'O CPF é válido.') 
        break
    else:
        print (f'O CPF é inválido. Por favor digite o CPF novamente, certificando-se de digitar os pontos e traços corretamente.')  

cpf_original = num_cpf
num_cpf = verifica_cpf(num_cpf)
num_cpf = list(num_cpf)
n_numeros = [3, 6, 9]
for i in sorted(n_numeros):
    num_cpf.pop(i)        





import re

def verifica_e_processa_cpf():
    def verifica_cpf(num_cpf):    
        regex = r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$'
        return re.fullmatch(regex, num_cpf) is not None

    while True:
        num_cpf = input('Digite o CPF a ser verificado: ')
        if verifica_cpf(num_cpf):
            print('O CPF é válido.')
            break
        else:
            print('O CPF é inválido. Por favor, digite o CPF novamente, certificando-se de digitar os pontos e traços corretamente.')

    num_cpf = list(num_cpf)
    n_numeros = [3, 6, 9]
    
    for i in sorted(n_numeros, reverse=True):
        num_cpf.pop(i)        

    cpf_processado = ''.join(num_cpf)
    print(f'CPF processado (sem pontos e traços): {cpf_processado}')

verifica_e_processa_cpf()


    verif_cpf1 = []
    for i in range(len(num_cpf)-2):
            verif_cpf1.append((10 - i) * int(num_cpf[i])) 
    
    soma1 = 0
    for i in range(len(verif_cpf1)):
        soma1 += verif_cpf1[i]
    
    pri_digito = 0
    resto1 = soma1 % 11
    if resto1 > 1:
        pri_digito = 11 - (resto1)
    teste_cpf = num_cpf
    teste_cpf.pop(10)
    teste_cpf.pop(9)
    teste_cpf.append(pri_digito)
    
    verif_cpf2 = []
    for i in range(len(num_cpf)):
            verif_cpf2.append((11 - i) * int(num_cpf[i]))
    
    soma2 = 0
    for i in range(len(verif_cpf2)):
        soma2 += verif_cpf2[i]
    seg_digito = 0
    resto2 = soma2 % 11
    if resto1 > 1:
        seg_digito = 11 - (resto2)
    teste_cpf.append(seg_digito)

    print(cpf_original)
    print(num_cpf)
    cpf_original = list(cpf_original)
    n_numeros2 = [3, 6, 9]
    for i in sorted(n_numeros):
        cpf_original.pop(i)

    
    int_cpf_original = list(map(int, cpf_original))
    int_teste_cpf = list(map(int, teste_cpf))

    print(int_cpf_original)
    print(int_teste_cpf)

    if int_cpf_original == int_teste_cpf:
        print("O CPF digitado é válido")
    else:
        print("O CPF digitado é inválido")
    

        
        




    break
else:
    print(f'O CPF foi digitado incorretamente. Por favor, tente novamente (Digite os pontos e traços do CPF na ordem e posições corretos).')
'''