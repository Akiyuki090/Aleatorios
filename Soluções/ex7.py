def verifica_argumentos(*tipos):
    def decorador(func):
        def wrapper(*args):
            if len(args) != len(tipos):
                raise TypeError(
                    f"{func.__name__}() recebeu {len(args)} argumentos, mas esperava {len(tipos)}")
            for i, (arg, tipo) in enumerate(zip(args, tipos)):
                if not isinstance(arg, tipo):
                    raise TypeError(
                        f"O argumento {i+1} de {func.__name__}() deve ser do tipo {tipo.__name__}")
            return func(*args)
        return wrapper
    return decorador


if __name__ == '__main__':
    @verifica_argumentos(int, int)
    def soma(a, b):
        return a + b

'''
Explicação:

. O decorador verifica_argumentos é definido com *tipos como argumento. O asterisco antes do nome tipos indica que a função aceitará um número variável de argumentos. No caso desse decorador, esses argumentos são os tipos dos argumentos que a função decorada espera receber.
. Dentro do decorador verifica_argumentos, outro decorador aninhado decorador é definido, que recebe a função original func como argumento.
. Dentro do decorador decorador, é definido outro wrapper aninhado wrapper que aceita um número variável de argumentos com a sintaxe *args.
. O wrapper wrapper verifica se o número de argumentos recebidos é igual ao número de tipos especificados no decorador verifica_argumentos. Se não forem iguais, um erro TypeError é levantado com uma mensagem que informa quantos argumentos foram recebidos e quantos eram esperados.
. Se o número de argumentos for o correto, o wrapper wrapper faz um loop com enumerate através dos argumentos passados para a função. Para cada argumento, ele verifica se o tipo do argumento é igual ao tipo especificado no decorador verifica_argumentos. Se algum argumento tiver um tipo diferente do esperado, um erro TypeError é levantado com uma mensagem que informa o número do argumento e o tipo esperado.
. Se todos os argumentos forem do tipo correto, a função original func é chamada com os argumentos passados usando a sintaxe return func(*args) e o resultado é retornado.
. Por fim, o decorador decorador é retornado para que possa ser usado para decorar outras funções. O decorador verifica_argumentos é retornado para que possa ser usado para decorar outras funções com diferentes tipos de argumentos.
'''