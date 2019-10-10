import argparse
parser = argparse.ArgumentParser(description = 'Um programa de exemplo.')
parser.add_argument('--frase', action = 'store', dest = 'frase',
                           default = 'Hello, world!', required = False,
                           help = 'A frase que deseja imprimir n vezes.')
parser.add_argument('-n', action = 'store', dest = 'n', required = True,
                           help = 'O número de vezes que a frase será impressa.')
arguments = parser.parse_args()
for i in range(0, int(arguments.n)):
    print(arguments.frase)
