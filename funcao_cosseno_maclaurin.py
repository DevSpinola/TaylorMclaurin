def funcao_cosseno_maclaurin(x, precisao_desejada):
    import numpy as np
    import math 

    k = 0
    # número de termos da série de Maclaurin considerados até o momento

    f = 0
    #Estimativa da função que queremos calcular, inicializada como 0

    cont=0
    #Contador para cálculo dentro da função genérica
    while True:          
 
        if(k%2==0): # As potências ímpares não aparecem, logo se considera apenas as pares
            f += (math.pow(-1,cont)/math.factorial(2*cont))*math.pow(x,2*cont) # Valor genérico da função cos(x) em MacLaurin
            cont+=1 
        print("-----------------------------------------------------------")                    
        if (1/math.factorial(k+1))* math.pow(np.abs(x),k+1)<= precisao_desejada:            
            break ## Irá quebrar o laço while quando o Resto for menor à precisão desejada           
        print("Resto:", (1/math.factorial(k+1)) * math.pow(np.abs(x),k+1))         
        k += 1
        # Enquanto a precisão desejada não tiver sido alcançada, 
        # incrementamos o valor de k e adicionamos novos termos ao
        # polinômio.             
        
    return [f,k]