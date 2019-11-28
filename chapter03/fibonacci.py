def fibonacci(limit: int = 10) -> int:
        lista = [[0,1],1]
        while limit > 0:
            x = lista[-2][1]+lista[-1];
            lista.append([lista[-2][1],lista[-1]])
            lista.append(x)
            limit -=1

        i = 0
        while i < len(lista):
            print(lista[i],lista[i+1])
            i+=2
            
fibonacci(10)
