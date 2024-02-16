def max(a,b):
    if(a>b):
        print('f{es mayor a: }',a)
    else:
        print('f{es mayor b: }',b)
    return 

print(max(4,6))

def max_of_three(a,b,c):
    if(a>b and a>c):
         return print(f'El valor mas alto es: A: {a}')
      
    elif(b>c and b>a):
       return  print(f'El valor mas alto es: B: {b}')
        
    elif(c>a and c>b):
       return print(f'El valor mas alto es: B {c}') 
    else:
        return print('NO SE PUEDEN INGRESAR VALORES NEGATIVOS O IGUALES')

print(max_of_three(2,2,2))

def is_vocal(caracter):
    list_vocal = ['a','b','c','d','e']
    if caracter in list_vocal:
        return True
    else:
        return False
    
print(is_vocal('z'))


def sum(lista):
    result = 0

    for n in lista:
        result = result + (n)

    print(result)

sum([2,2,2])    

def mult(lista):
    result = lista[0]
    i = 1

    while i in range(1,len(lista)):
        result = result * lista[i]
        i+=1
        print(result)

mult([2,2,2])        