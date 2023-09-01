def funcao_cosseno_maclaurin(x, precisao_desejada):
    import numpy as np
    import math
    import time 

    precisao_desejada_alcancada = False
    #Booleana que determina se a estimativa atual está dentro da precisão
    #desejada ou não


    k = 0
    # número de termos da série de Maclaurin considerados até o momento

    f = 0
    #Estimativa da função que queremos calcular, inicializada como 0

    cont=0
    while not precisao_desejada_alcancada:
        if (1/math.factorial(k+1))<= precisao_desejada:            
            break            
        print("Condição:",1/math.factorial(k+1) )        
        # Aqui, vocês devem implementar o cálculo da função 'cosseno' a partir
        # da série de MacLaurin, bem como do resto (para verificar se a
        # precisão desejada foi alcançada)
        # Valor Genérico da Função:  
        if(k%2==0):
            f += (math.pow(-1,cont)/math.factorial(2*cont))*math.pow(x,2*cont)
            print("valor funcao:", f)
            print("Valor Real:", math.cos(x)) 
            cont+=1
            time.sleep(1)
            print("-----------------------------------------------------------")
        k += 1
        # Enquanto a precisão desejada não tiver sido alcançada, 
        # incrementamos o valor de k e adicionamos novos termos ao
        # polinômio.
      
   
         

        
    return [f,k]