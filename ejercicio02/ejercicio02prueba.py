class Yin: pass

class Yang:
    def __del__(self):
        print("Yang destruido")

yin = Yin()

yang = Yang()

yin.yang = yang

print(yang)

print(yang is yin.yang)

yin.yang = None

del(yang)

print("?")


'''
<__main__.Yang object at 0x0000026D658CBDF0>
True
Yang destruido
?
'''
