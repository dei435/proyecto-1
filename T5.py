def buscar_y_en_x(x, y):
    cantidad =0
    maximo = x [0]
    for i in range(len(x)):
        if x [i] ==y:
            cantidad +=1
        if x[i] > maximo :
             maximo = x [i]
    if y == maximo :   
        es_maximo = True 
    else :
        es_maximo= False
    return cantidad, es_maximo

# ingrese la cantidad de numeros en "x" y el numero a buscar "y"
x =[1,2,9,4,2,8,2,1,3,6,8,7,8,9,6,5,2,4,4,4,4,5,2,3,9,2,9]
y= 9
cantidad, es_maximo=buscar_y_en_x(x,y)
print("cantidad de veces que se repite {}: {}".format(y, cantidad))
if es_maximo:
  print("{} es el maximo en el arreglo".format(y))
else:
    print("{} no es el maximo en el arreglo").format(y) 
    
    
    


    

