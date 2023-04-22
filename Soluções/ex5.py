def ordenar_strings(strings):
    return sorted(strings, key=str.lower)

if __name__ == '__main__':
    strings = ["Banana", "maçã", "Laranja", "Pera"]
    strings_ordenadas = ordenar_strings(strings)
    print(strings_ordenadas)
