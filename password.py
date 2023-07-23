import random
import string

def add_character_randomly(string, character):
    random_index = random.randint(0, len(string))
    result_string = string[:random_index] + character + string[random_index:]
    return result_string

# 1
def num_pwd():
    num = string.digits
    n = int(input("Enter the length of password : "))
    pwd = ""
    for i in range(n):
        pwd += ''.join(random.choice(num))
    return pwd

# 2
def alphanum_LCC():
    lowercase_char = string.ascii_lowercase
    num = string.digits
    pas = lowercase_char + num
    n = int(input("Enter the length of password : "))
    pwd = ""
    for i in range(n):
        pwd += ''.join(random.choice(pas))
    return pwd

# 3
def alphanum_UCC():
    uppercase_char = string.ascii_uppercase
    num = string.digits
    pas = uppercase_char + num
    n = int(input("Enter the length of password : "))
    pwd = ""
    for i in range(n):
        pwd += ''.join(random.choice(pas))
    return pwd

# 4   
def alphanum():
    lowercase_char = string.ascii_lowercase
    uppercase_char = string.ascii_uppercase
    num = string.digits
    pas = uppercase_char + num + lowercase_char
    n = int(input("Enter the length of password : "))
    pwd = ""
    for i in range(n):
        pwd += ''.join(random.choice(pas))
    return pwd

# 5
def alpha_LU():
    lowercase_char = string.ascii_lowercase
    uppercase_char = string.ascii_uppercase
    pas = uppercase_char + lowercase_char
    n = int(input("Enter the length of password : "))
    pwd = ""
    for i in range(n):
        pwd += ''.join(random.choice(pas))
    return pwd

# 6   
def alphanumspsl_LCC():
    lowercase_char = string.ascii_lowercase
    num = string.digits
    pas = lowercase_char + num
    n = int(input("Enter the length of password : "))
    while True:
        spsl_chars = string.punctuation
        spsl_char = input("Enter the special characters that you want to use in your password : ")
        spl_char = ''
        for i in range(len(spsl_char)):
            if spsl_char[i] in spsl_chars:
                spl_char += spsl_char[i]
            else:
                print( spsl_char[i],"is not a special character.")
        if not spl_char:
            continue
        else:
            if len(spl_char)<n:
                break
            else:
                print("Special character lenght is greater then or equal to password legth.")
                print("Try again!!")
                continue
    
    pwd = ""
    for i in range(n-len(spl_char)):
        pwd += ''.join(random.choice(pas))
    
    return add_character_randomly(pwd, spl_char)

# 7
def alphanumspsl_UCC():
    uppercase_char = string.ascii_uppercase
    num = string.digits
    pas = uppercase_char + num
    n = int(input("Enter the length of password : "))
    while True:
        spsl_chars = string.punctuation
        spsl_char = input("Enter the special characters that you want to use in your password : ")
        spl_char = ''
        for i in range(len(spsl_char)):
            if spsl_char[i] in spsl_chars:
                spl_char += spsl_char[i]
            else:
                print( spsl_char[i],"is not a special character.")
        if not spl_char:
            continue
        else:
            if len(spl_char)<n:
                break
            else:
                print("Special character lenght is greater then or equal to password legth.")
                print("Try again!!")
                continue
    
    pwd = ""
    for i in range(n-len(spl_char)):
        pwd += ''.join(random.choice(pas))
    
    return add_character_randomly(pwd, spl_char)

# 8 
def alphanumspsl():
    lowercase_char = string.ascii_lowercase
    uppercase_char = string.ascii_uppercase
    num = string.digits
    pas = uppercase_char + num + lowercase_char
    n = int(input("Enter the length of password : "))
    while True:
        spsl_chars = string.punctuation
        spsl_char = input("Enter the special characters that you want to use in your password : ")
        spl_char = ''
        for i in range(len(spsl_char)):
            if spsl_char[i] in spsl_chars:
                spl_char += spsl_char[i]
            else:
                print( spsl_char[i],"is not a special character.")
        if not spl_char:
            continue
        else:
            if len(spl_char)<n:
                break
            else:
                print("Special character lenght is greater then or equal to password legth.")
                print("Try again!!")
                continue
    
    pwd = ""
    for i in range(n-len(spl_char)):
        pwd += ''.join(random.choice(pas))
    
    return add_character_randomly(pwd, spl_char)

# 9
def alpha_LU_spsl():
    lowercase_char = string.ascii_lowercase
    uppercase_char = string.ascii_uppercase
    pas = uppercase_char + lowercase_char
    n = int(input("Enter the length of password : "))
    while True:
        spsl_chars = string.punctuation
        spsl_char = input("Enter the special characters that you want to use in your password : ")
        spl_char = ''
        for i in range(len(spsl_char)):
            if spsl_char[i] in spsl_chars:
                spl_char += spsl_char[i]
            else:
                print( spsl_char[i],"is not a special character.")
        if not spl_char:
            continue
        else:
            if len(spl_char)<n:
                break
            else:
                print("Special character lenght is greater then or equal to password legth.")
                print("Try again!!")
                continue
    
    pwd = ""
    for i in range(n-len(spl_char)):
        pwd += ''.join(random.choice(pas))
    
    return add_character_randomly(pwd, spl_char)
# 10
def LCC_spsl():
    lowercase_char = string.ascii_lowercase
    pas = lowercase_char
    n = int(input("Enter the length of password : "))
    while True:
        spsl_chars = string.punctuation
        spsl_char = input("Enter the special characters that you want to use in your password : ")
        spl_char = ''
        for i in range(len(spsl_char)):
            if spsl_char[i] in spsl_chars:
                spl_char += spsl_char[i]
            else:
                print( spsl_char[i],"is not a special character.")
        if not spl_char:
            continue
        else:
            if len(spl_char)<n:
                break
            else:
                print("Special character lenght is greater then or equal to password legth.")
                print("Try again!!")
                continue
    
    pwd = ""
    for i in range(n-len(spl_char)):
        pwd += ''.join(random.choice(pas))
    
    return add_character_randomly(pwd, spl_char)
    
# 11
def UCC_spsl(): 
    uppercase_char = string.ascii_uppercase
    pas = uppercase_char
    n = int(input("Enter the length of password : "))
    while True:
        spsl_chars = string.punctuation
        spsl_char = input("Enter the special characters that you want to use in your password : ")
        spl_char = ''
        for i in range(len(spsl_char)):
            if spsl_char[i] in spsl_chars:
                spl_char += spsl_char[i]
            else:
                print( spsl_char[i],"is not a special character.")
        if not spl_char:
            continue
        else:
            if len(spl_char)<n:
                break
            else:
                print("Special character lenght is greater then or equal to password legth.")
                print("Try again!!")
                continue
    
    pwd = ""
    for i in range(n-len(spl_char)):
        pwd += ''.join(random.choice(pas))
    
    return add_character_randomly(pwd, spl_char)
    
# 12
def LCC():
    lowercase_char = string.ascii_lowercase
    pas = lowercase_char
    n = int(input("Enter the length of password : "))
    pwd = ""
    for i in range(n):
        pwd += ''.join(random.choice(pas))
    return pwd
 
# 13 
def UCC(): 
    uppercase_char = string.ascii_uppercase
    pas = uppercase_char
    n = int(input("Enter the length of password : "))
    pwd = ""
    for i in range(n):
        pwd += ''.join(random.choice(pas))
    return pwd
    
    
if __name__ == "__main__":
    while True:
        print("\n\n0 - To close this programe")
        print("1 - Number password")
        print("2 - Number with lowercase character password")
        print("3 - Number with uppercase character password")
        print("4 - Alphanumeric password")
        print("5 - Lowercase and uppercase character password")
        print("6 - Number with lowercase and special character password")
        print("7 - Number with uppercase and special character password")
        print("8 - Alphanumeric with special character password")
        print("9 - Lowercase and uppercase with special character password")
        print("10 - Lowercase with special character password")
        print("11 - Uppercase with special character password")
        print("12 - Lowercase character password")
        print("13 - Uppercase character password\n\n")
        pass_num = int(input("Enter the number that type of password you need : "))
        
        if pass_num == 0:
            break
        elif pass_num == 1:
            pwd = num_pwd()
        elif pass_num == 2:
            pwd = alphanum_LCC()
        elif pass_num == 3:
            pwd = alphanum_UCC()
        elif pass_num == 4:
            pwd = alphanum()
        elif pass_num == 5:
            pwd = alpha_LU()
        elif pass_num == 6:
            pwd = alphanumspsl_LCC()
        elif pass_num  == 7:
            pwd = alphanumspsl_UCC()
        elif pass_num == 8:
            pwd = alphanumspsl()
        elif pass_num == 9:
            pwd = alpha_LU_spsl()
        elif pass_num == 10:
            pwd = LCC_spsl()
        elif pass_num ==11:
            pwd = UCC_spsl()
        elif pass_num == 12:
            pwd = LCC()
        elif pass_num == 13:
            pwd = UCC()
        else:
            print("Enter a valid number.")
            continue
        
        print("Program generated password is ",pwd)
        yesno = input("Do you want to continue if YES enter Y/y, if NO enter N/n : ")
        if yesno.lower() == "y":
            continue
        else:
            break