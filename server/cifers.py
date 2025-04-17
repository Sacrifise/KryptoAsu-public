from numpy import where, array

def define_the_language(text: str):  
    rus_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  
    eng_alph = 'abcdefghijklmnopqrstuvwxyz'  

    if len(text) < 3:  
        raise ValueError("Текст слишком короткий для определения языка")  

    rus_count = 0  
    eng_count = 0  

    for char in text[:3]:  
        if char in rus_alph:  
            rus_count += 1  
        elif char in eng_alph:  
            eng_count += 1  

    if rus_count > 0 and eng_count > 0:  
        raise ValueError("Текст не может содержать 2 алфавита")  

    if rus_count > eng_count:  
        return "rus"  
    elif eng_count > rus_count:  
        return "eng"  
    else:   
        raise ValueError("Язык не определен")   

def encrypt_polybius_cipher(text: str): 
    eng_alph = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]  
    rus_alph = [['а', 'б', 'в', 'г', 'д', 'е'], ['ё', 'ж', 'з', 'и', 'й', 'к'], ['л', 'м', 'н', 'о', 'п', 'р'], ['с', 'т', 'у', 'ф', 'х', 'ц'], ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь'], ['э', 'ю', 'я', 'а', 'б', 'в']]  

    eng_alph = array(eng_alph)  
    rus_alph = array(rus_alph)
     
    result = ""  
    alphabet = define_the_language(text) 
    if alphabet == "eng":
        alphabet = array(eng_alph)  
    elif alphabet == "rus":
        alphabet = array(rus_alph) 
    
    for char in text:  
        char = char.lower()   

        if char in alphabet:  
            rows, cols = where(alphabet == char)  
            if len(rows) > 0:  
               row = rows[0] + 1   
               col = cols[0] + 1  
               result += str(row) + str(col) + " "  
            else:  
                result += " "  

        else:  
            result += " "  


    return result  

def decrypt_polybius_cipher(text: str): 
    eng_alph = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y']]  
    rus_alph = [['а', 'б', 'в', 'г', 'д', 'е'], ['ё', 'ж', 'з', 'и', 'й', 'к'], ['л', 'м', 'н', 'о', 'п', 'р'], ['с', 'т', 'у', 'ф', 'х', 'ц'], ['ч', 'ш', 'щ', 'ъ', 'ы', 'ь'], ['э', 'ю', 'я', 'а', 'б', 'в']]  

    # alphabet = define_the_language(text) 
    # if alphabet == "eng":
    #     alphabet = array(eng_alph)  
    # elif alphabet == "rus":
    alphabet = array(rus_alph)
     
    result = ""  
     
    for i in range(0, len(text) - 1, 2):
        result += str(alphabet[int(text[i]) - 1][int(text[i + 1]) - 1])
    return result         

def caesar_cifer( text: str, shift: int):
    rus_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    eng_alph = 'abcdefghijklmnopqrstuvwxyz'
    
    result = ""
    alphabet = define_the_language(text)
    
    if alphabet == "rus":
        for alpha in text:
            if alpha not in rus_alph:
                result += alpha
            
            result += rus_alph[(rus_alph.find(alpha) + shift)% 33]
        return result
    if alphabet ==  "eng":
        for alpha in text:
            if alpha not in eng_alph:
                result += alpha
                
            result += eng_alph[(eng_alph.find(alpha) + shift)% 26]
        return result

def atbash_cifer(text: str):  
    rus_alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  
    eng_alph = 'abcdefghijklmnopqrstuvwxyz'  

    result = ''  
    try:  
        alphabet_type = define_the_language(text) 
    except ValueError as e:  
        return str(e)

    if alphabet_type == "rus":  
        alphabet = rus_alph  
    elif alphabet_type == "eng":  
        alphabet = eng_alph  
    else:  
        return "Неподдерживаемый язык"  

    alph_len = len(alphabet)  

    for alpha in text:  
        if alpha not in alphabet: 
            result += alpha 
        else:  
            result += alphabet[alph_len - alphabet.find(alpha) - 1]  

    return result  


