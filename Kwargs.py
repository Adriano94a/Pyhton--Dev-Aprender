# ** kwargs (Keyword arguments)
def concatenar(**palavras):
    frase= ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar(a='Nós', b='Somos', c='Pythonistas', d='Profissionais')