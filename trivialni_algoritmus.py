# pole = [1,3,4,8,9,14]

def hledani_cisla(pole,a):
    for i in pole:
        if i == a:
            return True
    
    return False

# cislo_se_nachazi = hledani_cisla(2)

# if cislo_se_nachazi == True:
#     print('ano')
# else:
#     print('ne')

# hledani_cisla(3)