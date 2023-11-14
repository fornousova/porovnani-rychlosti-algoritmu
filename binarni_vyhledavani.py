# pole = [1,2,3,4,5]
# x = 1

def vyhledavani(pole, malé, velké, x):
    if velké >= malé:
        prostredek = (malé + velké) // 2
	    
        if pole[prostredek] == x:
            return True
        elif pole[prostredek] > x:
            return vyhledavani(pole, malé, prostredek - 1, x)
        else:
            return vyhledavani(pole, prostredek + 1, velké, x)
    else:
        return False
	
def binarni_vyhledavani(pole,x):
    return vyhledavani(pole, 0, len(pole)-1, x)
      
# print(binarni_vyhledavani(pole,x))
# if vysledek != False:
#    print('ano')
# else:
#     print('ne')
		

