class SeteSegmentos(object):
    "Representa um display de sete segmentos para um digito de um numero"
    
    def __init__(self, x, y, w, h, v=0):
        u"""Constroi o display dado seu canto superior esquerdo (x,y) largura (w)
        e altura(h). O valor v deve ser um numero inteiro entre 0 e 9"""
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.v = v
            
    def draw(self):
        u"""Desenha os segmentos do display"""
        
        self.a = a = (self.x, self.y, self.x+self.w, self.y)
        self.b = b = (self.x+self.w, self.y, self.x + self.w, self.y +self.h/2)
        self.c = c = (self.x + self.w, self.y + self.h/2, self.x + self.w, self.y + self.h)
        self.d = d = (self.x, self.y + self.h, self.x + self.w, self.y + self.h)
        self.e = e = (self.x, self.y + self.h/2, self.x, self.y + self.h)
        self.f = f = (self.x, self.y, self.x, self.y + self.h/2)
        self.g = g = (self.x, self.y + self.h/2, self.x + self.w, self.y + self.h/2)

        if self.v == 0 or self.v==10 or self.v==20 or self.v==30 or self.v==40 or self.v==50 or self.v==60:
            return line(a[0],a[1],a[2],a[3]),line(b[0],b[1],b[2],b[3]),line(c[0],c[1],c[2],c[3]),line(d[0],d[1],d[2],d[3]),line(e[0],e[1],e[2],e[3]),line(f[0],f[1],f[2],f[3])
        elif self.v == 1 or self.v==11 or self.v==21 or self.v==31 or self.v==41 or self.v==51:
            return line(b[0],b[1],b[2],b[3]),line(c[0],c[1],c[2],c[3])
        elif self.v == 2 or self.v==12 or self.v==22 or self.v==32 or self.v==42 or self.v==52:
            return line(a[0],a[1],a[2],a[3]),line(b[0],b[1],b[2],b[3]),line(d[0],d[1],d[2],d[3]),line(e[0],e[1],e[2],e[3]),line(g[0],g[1],g[2],g[3])
        elif self.v == 3 or self.v==13 or self.v==23 or self.v==33 or self.v==43 or self.v==53:
            return line(a[0],a[1],a[2],a[3]),line(b[0],b[1],b[2],b[3]),line(c[0],c[1],c[2],c[3]),line(d[0],d[1],d[2],d[3]),line(g[0],g[1],g[2],g[3])
        elif self.v == 4 or self.v==14 or self.v==24 or self.v==34 or self.v==44 or self.v==54:
            return line(b[0],b[1],b[2],b[3]),line(c[0],c[1],c[2],c[3]),line(f[0],f[1],f[2],f[3]),line(g[0],g[1],g[2],g[3])
        elif self.v == 5 or self.v==15 or self.v==25 or self.v==35 or self.v==45 or self.v==55:
            return line(a[0],a[1],a[2],a[3]),line(c[0],c[1],c[2],c[3]),line(d[0],d[1],d[2],d[3]),line(f[0],f[1],f[2],f[3]),line(g[0],g[1],g[2],g[3])
        elif self.v == 6 or self.v==16 or self.v==26 or self.v==36 or self.v==46 or self.v==56:
            return line(a[0],a[1],a[2],a[3]),line(c[0],c[1],c[2],c[3]),line(d[0],d[1],d[2],d[3]),line(e[0],e[1],e[2],e[3]),line(f[0],f[1],f[2],f[3]),line(g[0],g[1],g[2],g[3])
        elif self.v == 7 or self.v==17 or self.v==27 or self.v==37 or self.v==47 or self.v==57:
            return line(a[0],a[1],a[2],a[3]),line(b[0],b[1],b[2],b[3]),line(c[0],c[1],c[2],c[3])
        elif self.v == 8 or self.v==18 or self.v==28 or self.v==38 or self.v==48 or self.v==58:
            return line(a[0],a[1],a[2],a[3]),line(b[0],b[1],b[2],b[3]),line(c[0],c[1],c[2],c[3]),line(d[0],d[1],d[2],d[3]),line(e[0],e[1],e[2],e[3]),line(f[0],f[1],f[2],f[3]),line(g[0],g[1],g[2],g[3])
        elif self.v == 9 or self.v==19 or self.v==29 or self.v==39 or self.v==49 or self.v==59:
            return line(a[0],a[1],a[2],a[3]),line(b[0],b[1],b[2],b[3]),line(c[0],c[1],c[2],c[3]),line(f[0],f[1],f[2],f[3]),line(g[0],g[1],g[2],g[3])
        else:
            return line(g[0],g[1],g[2],g[3])
        

class Tempo(object):
    u"""Representa um instante ou um intervalo de tempo"""
    
    def __init__(self,hh=0,mm=0,ss=0):
        u"""Construtor a partir do número de horas, minutos e segundos"""
        self.hh = hh
        self.mm = mm
        self.ss = ss
        
    def seconds(self):
        u"Retorna o numero de segundos do tempo - um valor entre 0 e 59"
        self.ss = second()
        return self.ss  # Values from 0 - 59
    
    def minutes(self):
        u"Retorna o número de minutos do tempo - um valor entre 0 e 59"
        self.mm = minute()
        return self.mm  # Values from 0 - 59

    
    def hours(self):
        u"Retorna o número de minutos do tempo - um valor entre 0 e 23"
        self.hh = hour()
        return self.hh  # Values from 0 - 23
    
class Relogio(object):
    u"Exibe um relógio analógico"
    
    def __init__(self,x,y,w,h,t=Tempo()):
        u"""Constrói um relógio a ser exibido dentro de um retângulo
        com canto superior esquerdo em (x,y), largura w e altura h,
        marcando o tempo t (objeto da classe Tempo)"""
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.t = t
        
    def setTime(self,t):
        u"""Muda o tempo do relógio para t (objeto da classe Tempo)"""
        # -------------------------------------------------------------
        
    def draw(self):
        u"Desenha o relógio com ponteiros de horas, minutos e segundos"
        
        r  = self.h/2
        x0 = self.x+(self.w/2)
        y0 = self.y+(self.h/2)
        
        fill(255,255,255)
        ellipse(x0,y0,self.w,self.h)               #ellipse grande
        fill(0,0,0)
        ellipse(x0,y0,5,5)                         #ellipse pequena do ponto central
        
        #linhas de marcação do relogio
        for i in range(12):
            strokeWeight (6)
            line(x0 + (r*0.9)*cos(radians(i*720/24) -pi/2), y0 + (r*0.9)*sin(radians(i*720/24) -pi/2), x0 + r*cos(radians(i*720/24) -pi/2) ,y0 + r*sin(radians(i*720/24) -pi/2)) 
        for j in range(60):
            strokeWeight (1)
            line(x0 + (r*0.95)*cos(radians(j*360/60.0) -pi/2), y0 + (r*0.95)*sin(radians(j*360/60.0) -pi/2), x0 + r*cos(radians(j*360/60.0) -pi/2) ,y0 + r*sin(radians(j*360/60.0) -pi/2))  
        
        #ponteiros-------------------------------------
        strokeWeight (2)
        line(x0, y0, x0 + (r*0.9)*cos(((self.t.seconds()*2*pi/60) - pi/2)) ,y0 + (r*0.9)*sin((self.t.seconds()*2*pi/60) - pi/2))   # second pointer
        strokeWeight (4)
        line(x0, y0, x0 + (r*0.8)*cos(radians(self.t.minutes()*360/60) -pi/2) ,y0 + (r*0.8)*sin(radians(self.t.minutes()*360/60) - pi/2))   # minute pointer
        strokeWeight (6)
        line(x0, y0, x0 + (r*0.7)*cos(radians(self.t.hours()*720/24) -pi/2) ,y0 + (r*0.7)*sin(radians(self.t.hours()*720/24) -pi/2))      # hour pointer
       
        
class RelogioDigital(object):
    u"Exibe um relógio digital"
    
    def __init__(self,x,y,w,h,t=Tempo()):
        u"""Constroi um relógio a ser exibido dentro de um retângulo
        com canto superior esquerdo em (x,y), largura w e altura h,
        marcando o tempo t (objeto da classe Tempo)"""
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.t = t
        
    def setTime(self,t):
        u"""Muda o tempo do relógio para t"""
         # -------------------------------------------------------------
        
    def draw(self):
        u"""Desenha o relógio com displays de sete segmentos marcando 
        horas,minutos e segundos"""
        space_3  = self.w * 0.03
        space_8 = self.w * 0.08
        space_12_5 = self.w *0.125

        strokeWeight(5)
        Segmento1_ss = SeteSegmentos(self.x + 5*space_12_5 + 3*space_3 + 2*space_8 , self.y  , space_12_5 , self. h , self.t.seconds())
        Segmento1_ss.draw()
        Segmento2_ss = SeteSegmentos(self.x + 4*space_12_5 + 2*space_3 + 2*space_8 , self.y  , space_12_5 , self. h , self.t.seconds()/10)
        Segmento2_ss.draw()
        Segmento3_mm = SeteSegmentos(self.x + 3*space_12_5 + 2*space_3 + space_8   , self.y  , space_12_5 , self. h , self.t.minutes())
        Segmento3_mm.draw()
        Segmento4_mm = SeteSegmentos(self.x + 2*space_12_5 + space_3 + space_8     , self.y  , space_12_5 , self. h , self.t.minutes()/10)
        Segmento4_mm.draw()
        Segmento5_hh = SeteSegmentos(self.x + space_12_5 + space_3                 , self.y  , space_12_5 , self. h , self.t.hours())
        Segmento5_hh.draw()
        Segmento6_hh = SeteSegmentos(self.x                                        , self.y  , space_12_5 , self. h , self.t.hours()/10)
        Segmento6_hh.draw()

            
from processing import *
from time import localtime
from math import *
    
def mousePressed():
    global relogio,analogico,digital 
    if relogio == analogico:
        relogio = digital
    else:
        relogio = analogico
        
def setup():
    size (400,400)
    strokeCap(SQUARE)
    global relogio,analogico,digital 
    relogio = analogico = Relogio (50,50,300,300)
    digital = RelogioDigital (20,150,360,100)
    
def draw():
    background(200)
    t = localtime()
    tempo = Tempo(t[3],t[4],t[5])
    relogio.setTime(tempo)
    relogio.draw()