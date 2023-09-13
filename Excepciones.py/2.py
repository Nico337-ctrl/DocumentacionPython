#creando una excepcion propia

class MiExcepcion(Exception):
    def __init__(self, error):
        print(f'Impresionante, cometiste el siguiente error: {error}')

#lanzando mi propia excepcion
#raise MiExcepcion('askdjñfaklsdjf persona poco culta')
try:
    raise MiExcepcion('persona poco oculta')
except:
    print('como vas a cometer este error')