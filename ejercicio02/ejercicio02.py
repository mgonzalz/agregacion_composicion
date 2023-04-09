class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin()
yang = Yang()
yin.yang = yang #Agrega el objeto yang a la clase yin

print(yang) 

print(yang is yin.yang)

del(yang)

print("?")


'''
El objeto yang se atribuye a la clase yin, en la línea 8. Al ejecutar __del__(), se ejecuta del(yang), que elimina el objeto yang. Sin embargo, el objeto yang sigue existiendo en la clase yin, por lo que no se elimina instantáneamente. Entonces cuando se ejecuta print("?"), todavia se está ejecutando el método del.

Para conseguir que se muestre antes el mensaje de Yang destruido, habria que establecer antes del print("?") la siguiente línea de código: yin.yang = None; debido a que al establecer el atributo de la clase yin a None, se elimina el objeto yang de la clase yin, por lo que se ejecuta el método del.

'''
