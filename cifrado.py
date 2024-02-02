alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

def cifrar(palabra):
    palabra = palabra.lower()
    cifrado = ""
    for letra in palabra:
        if letra in alph:
            cifrado += alph[-alph.index(letra)-1]
        else:
            cifrado += letra
    return cifrado

print(cifrar("GSVUOZTRHHZBDVINXIZAB"))

