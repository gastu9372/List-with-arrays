playlist = {} #Diccionario vacio
playlist ['Cancniones'] = [] #Lista vacia de canciones

#Funcion principal
def app():

    #Agregar a la playlist
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input ('Como quiere nombrar la playlist\r\n')
        if nombre_playlist:
            playlist['Nombre'] = nombre_playlist
            #Ya tenemos nombre, por eso se desactiva el True
            agregar_playlist = False
           
            #Mandar a llamar la funcion para agregar canciones
            agregar_canciones()

def agregar_canciones():
    #Bandera para agregar canciones
    agregar_cancion = True
    while agregar_cancion:
        #Pregunta que cancion agregar
        nombre_playlist = playlist['Nombre']
        pregunta = f'Agrega canciones para {nombre_playlist}: \r\n'
        pregunta += 'Escribe X para dejar de agreagar canciones\r\n'
        
        cancion = input(pregunta)
        if cancion == 'X':
            #Deja de agregar canciones
            agregar_cancion = False
            print('Finalizando...')

            #Mostrar resumen de la playlist
            mostrar_resumen() 
        else:
            #Agregar canciones a la playlist
            playlist ['Cancniones'].append(cancion)
            
def mostrar_resumen():
    nombre_playlist = playlist['Nombre'] 
    print(f'Playlist: {nombre_playlist}\r\n')
    print(f'Canciones:\r\n')
    for cancion in playlist['Cancniones']:
        print(cancion)


app()
