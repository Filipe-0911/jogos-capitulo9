def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_",]
    enforcou = False
    acertou = False
    
    #enqto nao enforcou e nao acertou
    while not enforcou and not acertou:
        chute = input("Qual a letra? ")
        chute = chute.strip()
        
        for index, letra in enumerate(palavra_secreta):
            
            if chute.upper() == letra.upper():
                letras_acertadas.pop(index)
                letras_acertadas.insert(index, letra)
                # letras_acertadas[index] = letra
                
        
        print("Jogando...")
        print(letras_acertadas)
        
        # if len(letras_acertadas) == len(palavra_secreta):
        #     enforcou = True
        #     acertou = True


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
