def no_space(texto):
    nuevo_texto = ""
    for letra in texto:
        if letra != " ":
            nuevo_texto += letra
    return nuevo_texto

def reverse(texto):
    texto_al_reves = ""
    for letra in texto:
        texto_al_reves = letra + texto_al_reves
    return texto_al_reves

def palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()
 
print(palindromo("verificar si una palabra es palindromo"))
print(palindromo("anita lava la tina"))
print(palindromo("abba"))
print(palindromo("reconocer"))
print(palindromo("amo la paloma"))
print(palindromo("verificar si una palabra es palindromo"))