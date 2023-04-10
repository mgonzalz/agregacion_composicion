class Yin: pass

class Yang:
    def __del__(self):
        print("Yang destruido")

yin = Yin()

yang = Yang()

yin.yang = yang

print(yang) # Output: <__main__.Yang object at 0x0000026D658CBDF0>

print(yang is yin.yang) # Output: True

yin.yang = None

del(yang)

print("?")

'''
Output: Yang destruido
        ?
'''
