
import numpy as np
from numpy import sin, cos, tan, arcsin, arccos, arctan, pi

from tkinter import *
from tkinter import ttk, messagebox, filedialog

import os
from os import path, kill, getppid, _exit

def ayuda():

    v5=Toplevel(v0)

    texto='''
                        ###############
                        ## TerraBola ##
                        ###############
      Programa para la simulación de la curvatura terrestre.


1.- PROPÓSITO Y FUNDAMENTOS.

El programa muestra esquemáticamente lo que vería un observador que mira al horizonte de la tierra, suponiendo que ésta fuese una esfera de 6371km de radio. La altura del observador respecto a tierra se puede ajustar desde un mínimo de 2m. La visualización proporciona además un "objeto", representado por un rectángulo plano cuyas dimensiones altitud y distancia son también ajustables.

La imagen principal tiene 720x720 pixels, y se forma mediante *proyección plana* de los elementos a visualizar, que son el horizonte y el objeto rectangular. El método de proyección plana es comúnmente aceptado como el que proporciona una representación más parecida a la manera en la que el ojo humano percibe el mundo, y es ampliamente usado en dibujo, videojuegos etc. El centro de proyección es el ojo del observador y el plano de proyección es perpendicular a la línea de visión (que va del ojo al punto medio del horizonte visible). La distancia del plano de proyección al centro de proyección es de unos 21cm para zoom nulo y aumenta hasta unos 412m en zoom máximo. Se ha implementado una amplitud de visión (sin zoom) de 120º, que el zoom puede estrechar hasta 0.1º.


2.- LA INTERFAZ DE USUARIO.

A la izquierda se encuentra el visor principal, que muestra el horizonte y el objeto. El rectángulo que representa al objeto siempre está "de pie", es decir en un plano que pasa por el centro de la tierra y que queda definido por su distancia al observador (ver más adelante). En la parte inferior se indican los parámetros tanto del observador como del objeto a los que corresponde la imagen. 

A su derecha hay dos deslizadores verticales que permiten ajustar el zoom (equivalente a un catalejo) y la altura del observador respecto a tierra. Para valores suficientes de éste último parámetro comenzará a apreciarse la curvatura del horizonte. Recuerde que en todo caso el observador mira hacia el punto del horizonte que tiene enfrente.

La parte superior derecha muestra una vista lateral del observador (ojo) con su campo de visión vertical (lineas punteadas rojas), la esfera que representa la tierra (en negro), la línea de visión junto con el radio al punto del horizonte correspondiente (azul oscuro), un plano paralelo al de proyección (azul claro), y la posición del objeto marcada por un pequeño aspa azul.

Debajo de la vista anterior están los deslizadores para ajustar los parámetros del objeto. El primero de ellos ajusta la distancia del objeto al observador, que se mide sobre la tierra (entre las verticales del objeto y del observador, independientemente de que uno o ambos estuviesen a alguna altitud sobre tierra). Puede aumentar este parámetro para llevar el objeto más allá del horizonte. El segundo ajusta la altitud del objeto sobre la tierra, medida desde la base del objeto. Los dos últimos ajustan el tamaño del objeto con un límite de 16km en cada dimensión.

A continuación se encuentra un campo informativo que puede cambiar durante el uso, y que avisará si se produce alguna configuración indeseable en la perspectiva. 

Los dos botones inferiores presentan esta ayuda y cierran el programa, respectivamente. 


3.- ALGUNOS PARÁMETROS ORIENTATIVOS.

A buen seguro querrá usted comparar lo que ve en el mundo real con lo que muestra el programa. La comparación es por supuesto pertinente, pero tenga en cuenta que los siguientes hechos podrían modificar ligeramente su percepción:
    - La distancia a la que nuestra atmósfera cotidiana deja ver un objeto a la luz del día en condiciones totalmente óptimas es de unos 50km. Esta distancia se reduce significativamente en presencia de humedad y similares (brumas, contaminación etc).
    - Cuando usted mira el horizonte con sus aproximadamente 120º de amplitud de visión (la misma que ofrece el programa sin zoom), ve "con el rabillo del ojo" las zonas extremas, mientras que al mirar la interfaz del programa usted estará usando solo unos 20º centrales de su visión ocular. Esto puede producir que aprecie más fácilmente curvaturas del horizonte en el programa que en el mundo real. 
    - Al mirar por la ventanilla de un avión su ángulo de visión del horizonte se reduce, dificultando apreciar su curvatura. En el programa puede ajustar ese parámetro con el zoom, quizá a un valor del orden de 90º. Por otra parte el cristal puede producir distorsiones, especialmente si fuese curvo en algunas zonas.

Para mayor utilidad, el objeto se representa esté o no detrás del horizonte. La interfaz informa del caso de varias formas:
    - La primera línea de información sobre el objeto que aparece en el visor principal indicará "ante horizonte" o "tras horizonte".
    - El objeto interrumpirá la linea del horizonte si se encuentra delante de éste (y su posición se interpone). En otro caso no ocultará el horizonte.
    - Consulte los valores de su distancia hasta el objeto y y hasta el horizonte (ambas medidas se dan sobre tierra). Así sabrá de inmediato cuál está más cerca.

En la lista siguiente puede encontrar la dimensión en altura, y en su caso la altitud de operación típica, de algunos objetos:

- La Santa María (carabela de Colón). Altura 19m.
- Barco-ciudad de vacaciones. Altura 72m.
- Estatua de la Libertad. Altura 93m.
- Torre Eiffel. ALtura 324m.
- Empire State Building. Altura 381m.
- Globo aerostático. Altura 23m. Altitud 900m.
- Helicóptero. Altura 4m. Altitud 2000m.
- Jumbo. Altura 12m. Altitud 9000m (9km).
- Aurora boreal. Altitud 100km.
- Naves orbitales. Altitud 300km.
- Satélite. Altura 30m. Altitud 700km.


Espero que TerraBola despierte su curiosidad por comparar lo que usted aprecia en sus viajes con lo que cabe esperar matemáticamente. 

                                                El autor:
                                                Juan Carlos del Caño
                                                _____________________
    '''

    ttk.Label(v5, text='Ayuda',
        font=('', 16)).grid(row=0, column=0, columnspan=2, pady=5)

    tcaja = Text(v5, width=65, height=30,wrap='word', font=('Mono',9),
        background='#D9D9D9', foreground='green', border=None, padx=20, pady=12)
    tcaja.grid(column=0, row=1, padx=8, sticky=(N,W,E,S))
    tcaja.insert('1.0',texto)

    scb = ttk.Scrollbar(v5, orient=VERTICAL, command=tcaja.yview)
    scb.grid(column=1, row=1, sticky='ns')
    
    tcaja['yscrollcommand'] = scb.set

    ttk.Button(v5, text='Entendido', width=9, command=v5.destroy).grid(
        column=0, row=2, pady=4, columnspan=2)

    tcaja['state']='disabled'

    v5.grid_columnconfigure(0, weight=1)
    v5.grid_rowconfigure(0, weight=1)
    v5.grid_rowconfigure(1, weight=4)
    v5.grid_rowconfigure(2, weight=1)
    v5.geometry('+250+70')

    v5.focus()
    v5.mainloop()
    
    
    
    
def calcula_pto(x_Q, y_Q, z_Q): 
    ''' Es para la vista principal (frame_lienzo).
        Entrada: coordenadas cartesianas xyz del pto Q a representar
        Usa como globales:  
                 mi altura h, 
                 R Radio de la tierra,
                 angulo del pto de tangencia en rad: fi_t 
                 distancia ojo-plano de vision: vision_d  
        Salida:
                 coordenadas en px del pto de interseccion en ejes aa,bb: lamda_3, lambda_2 
    '''
    
    AQ_tt = x_Q*cos(fi_t)-(y_Q-R-h)*sin(fi_t)
    AQ_bb = x_Q*sin(fi_t)+(y_Q-R-h)*cos(fi_t)
    AQ_aa = z_Q
    modAQ= np.linalg.norm([AQ_tt, AQ_bb, AQ_aa])
    
    lambda_1 = vision_d * modAQ / AQ_tt
    lambda_2 = lambda_1 * AQ_bb / modAQ
    lambda_3 = lambda_1 * z_Q / modAQ

    # pasamos a px las lambdas. 
    lambda_3 = int(1000*lambda_3) 
    lambda_2 = int(1000*lambda_2) 
    # y los transformamos a coordenadas del canvas
    lambda_3 = aa_px/2 + lambda_3
    lambda_2 = bb_px/2 - lambda_2 

    return ( lambda_3, lambda_2, lambda_1)


def update_h(hlog_strv):
    global h, fi_t
    ''' Tras cambiar h cambia el angulo de tangencia fi_t
        Devuelve ese fi_t en radianes 
    '''
    h = 2.**float(hlog_strv)
    fi_t = arccos(1. /(1.+h/R))
    pinta_gui()


def update_vision(vision_aa_strv):
    global vision_aa, vision_bb, vision_d
    ''' El slide cambia vision_aa (lo da en grados enteros)
        Dependen directamente los dos del global
    '''
    vision_aa= float(vision_aa_strv)
    vision_aa *= cte # a radianes
    vision_bb = vision_aa * bb_px/aa_px
    vision_d = aa_px / (2000.* tan(vision_aa))
    pinta_gui()


def update_globo_d(globo_dlog_strv):
    global globo_d
    globo_d = 2.**(float(globo_dlog_strv))
    pinta_gui()
    
def update_globo_h(globo_hlog_strv):
    global globo_h
    globo_h = 2.**(float(globo_hlog_strv))
    pinta_gui()
    
def update_globo_dimx(globo_dimxlog_strv):
    global globo_dimx
    globo_dimx= 2.**(float(globo_dimxlog_strv))
    pinta_gui()
    
def update_globo_dimy(globo_dimylog_strv):
    global globo_dimy
    globo_dimy= 2.**(float(globo_dimylog_strv))
    pinta_gui()
    
    
def pinta_gui(): # intento optimizar para rapidez
    global paca_anterior, relleno, globo_aviso_strv, globo_aviso_lbl
    
    # pintar el horizonte en frame_lienzo
    
    frame_lienzo.delete('all')
    puntos1, puntos2, inc_teta = [], [], vision_aa/31.
    teta = 0.
    aa_P = 22 # por decir algo 0->720

    while aa_P <= aa_px and teta<pi :
        x_Q = R*sin(fi_t)*cos(teta)
        y_Q = R*cos(fi_t)
        z_Q = R*sin(fi_t)*sin(teta)
        
        aa_P, bb_P, kk = calcula_pto(x_Q, y_Q, z_Q)
        puntos1.append(aa_P)
        puntos1.append(bb_P)
        puntos2.append(aa_px-aa_P)
        puntos2.append(bb_P)
        teta += inc_teta
    frame_lienzo.create_line(puntos1, width=1)
    frame_lienzo.create_line(puntos2, width=1)

    frame_lienzo.create_text(260, 630, text='Tú:', anchor='e')

    frame_lienzo.create_text(260, 650, text='Altitud desde tierra=', anchor='e')
    frame_lienzo.create_text(265, 650, text=f'{str(int(h))} m', anchor='w')

    frame_lienzo.create_text(260, 670, text='Visión horizontal=', anchor='e')
    frame_lienzo.create_text(265, 670, text='{:.1f} º'.format(2*vision_aa/cte), anchor='w')

    frame_lienzo.create_text(260, 690, text='Dist. al horizonte (en tierra)=', anchor='e')
    horizonte_d= fi_t * R
    frame_lienzo.create_text(265, 690, text=f'{str(int(horizonte_d))} m', anchor='w')

    texto='ante' if globo_d < horizonte_d else 'tras' 
    frame_lienzo.create_text(430, 630, text= f'Objeto:  {texto} horizonte.', anchor='w')

    frame_lienzo.create_text(560, 650, text='Distancia (en tierra)=', anchor='e')
    frame_lienzo.create_text(565, 650, text=f'{str(int(globo_d))} m', anchor='w')

    frame_lienzo.create_text(560, 670, text='Altitud=', anchor='e')
    frame_lienzo.create_text(565, 670, text='{:.1f} m'.format(globo_h), anchor='w')

    frame_lienzo.create_text(560, 690, text='Dimensiones=', anchor='e')
    frame_lienzo.create_text(565, 690, 
        text=f'{str(int(globo_dimx))} x {str(int(globo_dimy))} m', anchor='w')


    # actualizar frame_delado (tiene 300x500, hago R=200px, centro [40,390])
    
    frame_delado.delete('all')
    x_px= lambda x:  int(x*scal_delado) +40
    y_px= lambda y: -int(y*scal_delado) +490
    
    frame_delado.create_arc(-160,291,240,690, start=0., extent=100., style='arc') # 291: 1px tonto
    frame_delado.create_line(40,490,280,490, arrow='last')
    frame_delado.create_line(40,490,40,104, arrow='last')
    
    cf,sf = cos(fi_t), sin(fi_t)
    A_px= ( 40, y_px(R+h) )
    B_px= (x_px(R*sf), y_px(R*cf) )
    M_px= (x_px(vision_d*cf), y_px(R+h-vision_d*sf) )
    
    frame_delado.create_line(40,490, B_px[0], B_px[1], fill='blue')
    frame_delado.create_line(A_px[0],A_px[1], B_px[0], B_px[1], fill='blue')
    frame_delado.create_line(B_px[0],B_px[1], B_px[0]+ 110*cf, 
                                              B_px[1]+ 110*sf, fill='blue')
    # puntos para el rango de vision (vertice en A)
    cf,sf = cos(-fi_t-vision_bb), sin(-fi_t-vision_bb)
    pto1=(x_px(cf*R) , y_px(R+h+ R*sf))
    cf,sf = cos(-fi_t+vision_bb), sin(-fi_t+vision_bb)
    pto2=(x_px(cf*R) , y_px(R+h+ R*sf))
    frame_delado.create_line(A_px[0],A_px[1], pto1[0],pto1[1], dash=(5,3), fill='red')
    frame_delado.create_line(A_px[0],A_px[1], pto2[0],pto2[1], dash=(5,3), fill='red')
    frame_delado.create_line(pto1[0],pto1[1], pto2[0],pto2[1], fill='#D6EFFF', width=3)
    
    # un ojo indicativo
    if fi_t>0.61: 
        img=ojo_img45
    elif fi_t>0.17:
        img=ojo_img20
    else:
        img=ojo_img00
    frame_delado.create_image(38, A_px[1], image=img, anchor='e')
    
    # pintar el objeto (llamado globo):
    
    # dibujo crucecilla en frame_delado:
    globo_fi = globo_d/R
    seno= sin(globo_fi) # lo uso luego varias veces
    Q= ( (R+globo_h)*seno, (R+globo_h)*cos(globo_fi) )
    Q_px= (40+Q[0]*scal_delado, 490-Q[1]*scal_delado)
    frame_delado.create_line(Q_px[0]-1,Q_px[1]-1, Q_px[0]+1,Q_px[1]+1 , fill='#18CFFD',width=8)
    frame_delado.create_line(Q_px[0]-1,Q_px[1]+1, Q_px[0]+1,Q_px[1]-1 , fill='#18CFFD',width=8)
    
    # pinto el objeto en frame_lienzo, proyectando los 4 vertices
    # la altitud del objeto es la de su linea inferior
    # Q va a ser el pto medio inferior y superior por turno. Por ej
    # el lado inferior tiene bb & tt ctes, y los vertices se obtienen
    # con +- el semiancho como coordenada z.
    globo_aviso_strv.set(avisos[0])
    globo_aviso_lbl.background='white'
    ptos, k, kk = [], False, False
    
    RR= R + globo_h
    x_Q = RR*sin(globo_fi)
    y_Q = RR*cos(globo_fi)
    z_Q = globo_dimx/2.
    a,b,c= calcula_pto(x_Q, y_Q, z_Q)  # primer vertice
    if c<0. : 
        a= aa_px -a
        kk=True
    if a>aa_px or a<0 or b>bb_px or b<0: k=True
    ptos.append(a)
    ptos.append(b)
    a,b,c= calcula_pto(x_Q, y_Q, -z_Q) # segundo vertice
    if c<0. : 
        a= aa_px -a
        kk=True
    if a>aa_px or a<0 or b>bb_px or b<0: k=True
    ptos.append(a)
    ptos.append(b)
    
    RR= R + globo_h + globo_dimy
    x_Q = RR*sin(globo_fi)
    y_Q = RR*cos(globo_fi)
    a,b,c= calcula_pto(x_Q, y_Q, -z_Q)  # tercer vertice
    if c<0. : 
        a= aa_px-a
        kk=True
    if a>aa_px or a<0 or b>bb_px or b<0: k=True
    ptos.append(a)
    ptos.append(b)
    a,b,c= calcula_pto(x_Q, y_Q, z_Q)   # cuarto vertice
    if c<0. : 
        a= aa_px-a
        kk=True
    if a>aa_px or a<0 or b>bb_px or b<0: k=True
    ptos.append(a)
    ptos.append(b)
    
    # Control de aberraciones.
    # si lambda_1<0 -> kk=True, el punto Q está detrás del plano de vision; habra
    # aberracion -> avisar
    if kk:
        globo_aviso_strv.set(avisos[2])
        #globo_aviso_lbl.config(bg='#FFC5BF') # aviso rojo
    # si el punto se sale del campo de vision puede haber ligera aberracion:
    elif k:
        globo_aviso_strv.set(avisos[1])
        #globo_aviso_lbl.config(bg='#D9D9D9') # aviso gris entorno
    else:
        globo_aviso_strv.set(avisos[0])
        #globo_aviso_lbl.config(bg='#D9D9D9') # gris entorno
    
    relleno='white' if globo_d < horizonte_d else '' 
    frame_lienzo.create_polygon(ptos, outline='blue', fill=relleno)

    return





# el zoom se hara cambiando los grados de vision: 60 -> 2 o menos?
# son semiangulos; el amplio de vision a zoom 0 sera  120º
# la pantalla (frame) de vision cambiara su distancia al ojo de forma que 
# sus dimensiones sean las mismas: aa_px/1000, bb_px/1000, en metros!
# -> eso crea equivalencia  1 pixel = 1 mm
# -> la pantalla de vision sera algo como 0.72m x 0.72m siempre
# -> hare que los ptos u objetos a representar nunca esten a menos de 10m
# La distancia desde el ojo al frame de vision sera: 
#  vision_d = aa_px /( 2000*tg(vision_aa) ) 

# Para que esten en global:
fi_t, vision_bb, vision_d, = 0., 0., 0.

# datos fijos:
cte= pi/180.
R=6371000. # radio de la tierra en m
aa_px=720  # anchura del frame de vision, en px.
bb_px=720  # altuta del frame de vision, en px.
scal_delado= 200/R # escala para frame_delado en px/m
 
# datos a tomar de gui
vision_aa=1.        # grados de vision horiz (semiangulo)
h=2.                # altura yo = 2m
globo_d=16
globo_h=0
globo_dimx=4
globo_dimy=4
paca_anterior=False
relleno=''



###########################
### INTERFAZ DE USUARIO ###
###########################

v0=Tk()
v0.title('TerraBola')
ojo_img00= PhotoImage(file= './imagenes/ojo_00.png')
ojo_img20= PhotoImage(file= './imagenes/ojo_20.png')
ojo_img45= PhotoImage(file= './imagenes/ojo_45.png')

frame_lienzo= Canvas(v0, width=aa_px, height=bb_px, background='white')
frame_lienzo.grid(column=0, row=0, rowspan=3)

frame_yo= ttk.Frame(v0, height=bb_px)
frame_yo.grid(column=1,row=0, rowspan=3, ipadx=3)

frame_delado= Canvas(v0, width=300, height=500, background='white')
frame_delado.grid(column=2, row=0, sticky='n')  

frame_delglobo= ttk.Frame(v0, width=300, height=250)
frame_delglobo.grid(column=2,row=1,ipadx=3, ipady=3, sticky='n')

frame_botones= ttk.Frame(v0, width=300)
frame_botones.grid(column=2,row=2)

boton_ayuda=ttk.Button(frame_botones,text='Ayuda',command= ayuda)
boton_ayuda.grid(column=0, row=0, padx=3, pady=3)

boton_salir=ttk.Button(frame_botones,text='Salir',
    command= lambda : print(vision_d) )
boton_salir.grid(column=1, row=0, padx=3, pady=3)

# rellenar frame_yo

zoom_strv=StringVar(value='60')
zoom_scal=ttk.Scale(frame_yo, orient=VERTICAL, length=bb_px-20, from_=0.05, to=60., 
        variable=zoom_strv, command=update_vision)
zoom_scal.grid(column=0, row=0)
ttk.Label(frame_yo, text='zoom').grid(column=0, row=1)

hlog_strv=StringVar(value='1') # aprox 2m, el minimo (h sera 2** eso)
h_scal=ttk.Scale(frame_yo, orient=VERTICAL, length=bb_px-20, from_=23, to=1,
        variable=hlog_strv, command=update_h)
h_scal.grid(column=1, row=0)
ttk.Label(frame_yo, text=' h ').grid(column=1, row=1)

# rellenar frame_delglobo

ttk.Label(frame_delglobo,text='OBJETO:').grid(column=0,row=0, pady=6)

globo_dlog_strv=StringVar(value='4') # 2**5=32m de distancia
globo_d_scal=ttk.Scale(frame_delglobo, orient=HORIZONTAL, length=260, from_=4, to=23, 
        variable=globo_dlog_strv, command=update_globo_d) # de 16m a 8e6 m de distancia
globo_d_scal.grid(column=0, row=1, sticky='w')
ttk.Label(frame_delglobo, text=' dist ', font=('Mono', 10)).grid(column=1, row=1, sticky='e')

globo_hlog_strv=StringVar(value='-7') # 2**10=1024m de altitud (de la base)
globo_h_scal=ttk.Scale(frame_delglobo, orient=HORIZONTAL, length=260, from_=-7, to=22, 
        variable=globo_hlog_strv, command=update_globo_h) # de 8mm~0 a 4e6 m de altitud
globo_h_scal.grid(column=0, row=2, sticky='w')
ttk.Label(frame_delglobo, text=' alti ', font=('Mono', 10)).grid(column=1, row=2, sticky='e')

globo_dimxlog_strv=StringVar(value='2') # ancho del globo 2**2=4m
globo_dimx_scal=ttk.Scale(frame_delglobo, orient=HORIZONTAL, length=260, from_=0, to=14, 
        variable=globo_dimxlog_strv, command=update_globo_dimx) # de 1m a 16km de ancho
globo_dimx_scal.grid(column=0, row=3, sticky='w')
ttk.Label(frame_delglobo, text=' dimx ', font=('Mono', 10)).grid(column=1, row=3, sticky='e')

globo_dimylog_strv=StringVar(value='2') # alto del globo 2**2=4m
globo_dimy_scal=ttk.Scale(frame_delglobo, orient=HORIZONTAL, length=260, from_=1, to=14, 
        variable=globo_dimylog_strv, command=update_globo_dimy) # de 2m a 16km de alto
globo_dimy_scal.grid(column=0, row=4, sticky='w')
ttk.Label(frame_delglobo, text=' dimy ', font=('Mono', 10)).grid(column=1, row=4, sticky='e')

avisos=['\nObjeto en el campo de visión. Ok.\n ', 
    'El objeto excede el campo de visión.\nPuede haber ligeras aberraciones'+
    '\nen la perspectiva.', 
    'Parte del objeto está tras "el ojo".\nDisminuya sus dimensiones o'+
    '\naumente su distancia...']
globo_aviso_strv=StringVar(value= avisos[0])
globo_aviso_lbl=Label(frame_delglobo, textvariable=globo_aviso_strv, font=('Mono',10),
    background='#D9D9D9', width=36)
globo_aviso_lbl.grid(column=0, row=5, columnspan=2, pady=6)


# actualizar la 1ª vez dependientes de h & vision_aa:
h = 2.
fi_t = arccos(1. /(1.+h/R))
vision_aa= 1.05 # 1 rad ~ 60 grados
vision_bb = vision_aa * bb_px/aa_px
vision_d = aa_px / (2000.* tan(vision_aa))
pinta_gui()

v0.mainloop()



















