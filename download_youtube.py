# importamos las librerias necesarias
from tkinter import *
from pytube import YouTube
import os
from moviepy.editor import *

# funcion para mostrar el fram de inicio y poder llamarlo cuando se quiera
def inicio(frame=None):
    # si no hay frame lo crea, sino usa la funcion quitar_botones() para eliminar el frame dado en los argumentos
    if frame != None:
        quitar_botones(frame)
    
    # creamos el frame
    inicioF = Frame()

    # cramos la interfaz grafica del nuevo frame
    btn_yb = Button(inicioF, text="Descargar Video YouTube", command=lambda: descargar_youtube(inicioF))
    btn_yb.grid(row=1, column=3, padx=10, pady=10)

    btn_aud = Button(inicioF, text="Descargar Audio YouTube", command=lambda: descargar_audio(inicioF))
    btn_aud.grid(row=2, column=3, padx=10, pady=10)

    # y lo mostramos
    inicioF.pack()



def descargar_youtube(frameV):
    '''
    Función que permite descargar el video de un vídeo en formato mp3 a partir de su URL.
    Se llama cuando se pulsa el botón "Descargar Video YouTube".
    '''
    # quitamos el frame  anterior
    quitar_botones(frameV)

    def descargar():
        '''
        Llama a la función download del módulo pyTube para realizar la descarga
        '''
        status_label = Label(frameYT, text="")
        status_label.grid(row=3, column=1, columnspan=3)
        try:
            # hacemos conexion con youtube  y obtenemos los streams del video
            yt = YouTube(url.get())
            # indicamos la ruta final en donde se guarda el audio que se desea descargar
            yt.streams.get_highest_resolution().download(output_path="./descargas")
            # eliminamos el contenido del campo entry para poder meter más enlaces tras descargar el anterior
            status_label.config(text=f"Titulo: {yt.title}")
            # eliminamos el contenido del campo entry para poder meter más enlaces tras descargar el anterior
            url.delete(0, END)
        except Exception as e:
            status_label.config(text=f"Error: {e}")
            print(e)


    # le ponemos un nuevo frame
    frameYT = Frame()
    
    # cramos la interfaz grafica del nuevo frame
    label = Label(frameYT, text="Introduzca la URL")
    label.grid(row=0, column=2, padx=15, pady=15, columnspan=10)

    url = Entry(frameYT)
    url.grid(row=1, column=2, padx=20, pady=10, columnspan=10)

    btn_des = Button(frameYT, text="Descargar", command=descargar)
    btn_des.grid(row=2, column=3, columnspan=4)
    btn_inicio = Button(frameYT, text="Inicio", command=lambda: inicio(frameYT))
    btn_inicio.grid(row=2, column=8, columnspan=4)

    # y lo mostramos
    frameYT.pack()



def descargar_audio(frameV):
    '''
    Función que permite descargar el audio de un vídeo en formato mp3 a partir de su URL y muestra los progresos por consola.
    Se llama cuando se pulsa el botón "Descargar Audio YouTube".
    '''
    def descargar_aud():
            # indicamos la ruta raiz de en donde se va a descargar
            parent_dir = "./descargas"
            try:
                # hacemos conexion con youtube  y obtenemos los streams del video
                yt = YouTube(url.get())
                status_label = Label(frameAudio, text=yt.title)
                status_label.grid(row=4, column=1, columnspan=3)
                # indicamos la ruta final en donde se guarda el audio que se desea descargar
                ruta_fin = yt.streams.get_audio_only().download(parent_dir + '/audio')
                # indireectamente se usa otra libreria para mostrar la barra de progreso en la consola
                audioclip = AudioFileClip(ruta_fin)
                # convertimos al formato mp3 y lo salvamos en la carpeta correspondiente
                audioclip.write_audiofile(audioclip.filename.replace('.mp4', '.mp3'))

                # mostramos mensaje de éxito si todo ha funcionado, tambien ponemos el nombre del video
                os.remove(audioclip.filename)
                status_label.config(text="Descargando audio...")
                #yt.streams.get_highest_resolution().download(output_path="./downloads")
                status_label.config(text=f"Audio descargado correctamente!\nTitulo: {yt.title}")
                # eliminamos el contenido del campo entry para poder meter más enlaces tras descargar el anterior
                url.delete(0, END)
            except Exception as e:
                # sacamos un mensaje de erro y cual es el fallo
                status_label.config(text=f"Error: {e}")

    # quitamos el frame  anterior
    quitar_botones(frameV)
    
    # le ponemos un nuevo frame
    frameAudio = Frame()

    # cramos la interfaz grafica del nuevo frame
    label = Label(frameAudio, text="Introduzca la URL")
    label.grid(row=0, column=2, padx=15, pady=15, columnspan=10)
    
    url = Entry(frameAudio)
    url.grid(row=1, column=2, padx=20, pady=10, columnspan=10)
    
    btn_des = Button(frameAudio, text="Descargar", command=descargar_aud)
    btn_des.grid(row=3, column=3, columnspan=4)
    btn_inicio = Button(frameAudio, text="Inicio", command=lambda: inicio(frameAudio))
    btn_inicio.grid(row=3, column=8, columnspan=4)

    # y lo mostramos
    frameAudio.pack()



def quitar_botones(frame):
    '''Esta función destruye el frame indicado en el argumento'''
    # destruimos le frame dado en el argumento
    frame.destroy()



# creamos una ventana
ventana = Tk()

# le damos  un titulo a la ventana
ventana.title(u"Descargar videos/audio desde YouTube")

# le damos un tamaño a la ventana
ventana.geometry("450x350")

# llamamos a la funcion inicio() para mostrar el frame
inicio()

# bucle de la aplicación
ventana.mainloop()