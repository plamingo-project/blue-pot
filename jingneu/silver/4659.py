#이미 푼 문제여서 ... 나중에 다시 풀어보는 것도 좋을듯~

moeum = ['a', 'e', 'i', 'o', 'u']

def convert_char(char, moeum):
    return 'm' if char in moeum else 'j'

while True:
    password = input()
    if (password == 'end'):
        break
    password_list = list(password)
    
    #1 
    num = 0
    for i in moeum:
        if (i in password):
            num+=1
    if(num == 0): 
        print("<{0}> is not acceptable.".format(password))
        continue
    
    #2
    
    new_list = ''.join(list(map(lambda char: convert_char(char, moeum),password_list)))
    
    if('jjj' in new_list or 'mmm' in new_list):
        print("<{0}> is not acceptable.".format(password))
        continue
    
    #3
    
    none = False
    
    for j in range(len(password)-1):
        if ((password[j+1] == password[j]) and (password[j+1] not in ['e', 'o'])):
            none = True
            break
    
    if(none): 
        print("<{0}> is not acceptable.".format(password))
        continue
    
    print("<{0}> is acceptable.".format(password))
    continue