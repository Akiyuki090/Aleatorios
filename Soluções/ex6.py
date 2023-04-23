import time


def tempo_execucao(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        tempo_total = fim - inicio
        print(f"Tempo de execução de {func.__name__}: {tempo_total:.6f} segundos.")
        return resultado
    return wrapper


if __name__=='__main__':
    @tempo_execucao
    def minha_funcao():
        print(3)

'''
Explicação:

. import time importa a biblioteca time, que fornece funções para trabalhar com o tempo.
. def tempo_execucao(func) define o decorador tempo_execucao, que aceita uma função func como argumento.
. def wrapper(*args, **kwargs) define a função wrapper que envolve a função original func e aceita um número arbitrário de argumentos posicionais *args e argumentos nomeados **kwargs.
. inicio = time.time() define a variável inicio com o tempo atual usando a função time.time().
. resultado = func(*args, **kwargs) chama a função original func com os argumentos passados para a função wrapper.
. fim = time.time() define a variável fim com o tempo atual usando a função time.time().
. tempo_total = fim - inicio calcula o tempo total de execução da função original subtraindo o tempo de início do tempo de fim.
. print(f"Tempo de execução de {func.__name__}: {tempo_total:.6f} segundos.") imprime o tempo total de execução da função original formatado na saída padrão, com o nome da função original usando func.__name__.
. return resultado retorna o resultado da função original.
. return wrapper retorna a função wrapper que envolve a função original func.

'''
