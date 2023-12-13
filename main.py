import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

# CORES----------------------------------
cor0 = '#FFFFFF' # BRANCO
cor1 = '#333333' # TOM DE BRANCO
cor2 = '#fcc058' # LARANJA
cor3 = '#38576b' # 
cor4 = '#000000' # PRETO
cor5 = '#fff873' # AMARELO
cor6 = '#fcc058' # TOM DE LARANJA
cor7 = '#e85151' # VERMELHO
cor8 = '#34eb3d' # TOM DE VERDE
fundo = '#3b3b3b' #

# CONFIGURANDO JANELA PRINCIPAL-----------
janela = Tk()
janela.title('JO KEN POW!')
janela.geometry('400x400')
janela.configure(bg=fundo)

# DIVIDINDO A JANELA PRINCIPAL------------
frame_cima = Frame(janela, width=400, height= 100, bg=cor1, relief='raised')
frame_cima.grid(row= 0, column = 0, sticky=NW) 

frame_baixo = Frame(janela, width=400, height= 300, bg=cor0, relief='raised',border=6)
frame_baixo.grid(row= 1, column = 0, sticky=NW) 

estilo = ttk.Style(janela)
estilo.theme_use('clam')


# CRIANDO JOGADOR01
jogador_01 = Label(frame_cima, text='JOGADOR', height=1, anchor='center', font=('helvetica 10 bold'), bg=cor1, fg=cor0)
jogador_01.place(x=25,y=65)

# LINHA QUE INDICA VITORIA OU DERROTA------
jogador_01_linha = Label(frame_cima, text='', height=10, anchor='center', font=('helvetica 10 bold'), bg=cor0, fg=cor0)
jogador_01_linha.place(x=0,y=0)

# PONTUAÇÃO DO JOGADOR01-------------------
jogador_01_potuacao = Label(frame_cima, text='0', height=1, anchor='center', font=('helvetica 35 bold'), bg=cor1, fg=cor0)
jogador_01_potuacao.place(x=50,y=10)

# DIVISOR DE PONTUAÇÃO---------------------
divisor_pontos = Label(frame_cima, text=':', height=1, anchor='center', font=('helvetica 35 bold'), bg=cor1, fg=cor0)
divisor_pontos.place(x=200,y=10)

# CRIANDO JOGADOR2-------------------------
jogador_02 = Label(frame_cima, text='MÁQUINA', height=1, anchor='center', font=('helvetica 10 bold'), bg=cor1, fg=cor0)
jogador_02.place(x=305,y=65)

# LINHA QUE INDICA VITORIA OU DERROTA------------------------------------
jogador_02_linha = Label(frame_cima, text='', height=10, anchor='center', font=('helvetica 10 bold'), bg=cor0, fg=cor0)
jogador_02_linha.place(x=395,y=0)

# PONTUAÇÃO JOGADOR02----------------------------------------------------
jogador_02_potuacao = Label(frame_cima, text='0', height=1, anchor='center', font=('helvetica 35 bold'), bg=cor1, fg=cor0)
jogador_02_potuacao.place(x=320,y=10)

# LINHA QUE INDICA EMPATE-------------------------------------------------
empate_linha = Label(frame_cima, text='', width=400, anchor='center', font=('helvetica 1 bold'), bg=cor0, fg=cor0)
empate_linha.place(x=0,y=95)

# LABEL DE ESCOLHA DAS AÇÕES---------------------------------------------

escolha_maquina = Label(frame_baixo, text='', height=1, anchor='center', font=('helvetica 10 bold'), bg=cor0, fg=cor0)
escolha_maquina.place(x=300,y=20)

escolha_jogador = Label(frame_baixo, text='', height=1, anchor='center', font=('helvetica 10 bold'), bg=cor0, fg=cor0)
escolha_jogador.place(x=30,y=20)

# VARIAVEIS GLOBAIS------------------------------------------------------

global jogador
global maquina
global rounds
global pontos_jogador
global pontos_maquina

pontos_jogador = 0
pontos_maquina = 0
rounds = 9


# FUNÇÃO LÓGICA DO JOGO--------------------

def jogar(i):
    global rounds
    global pontos_jogador
    global pontos_maquina
    
    if rounds >0:
        print(rounds)
        opcoes = ['PAPEL', 'PEDRA', 'TESOURA']
        maquina = random.choice(opcoes)
        jogador = i
        escolha_maquina['text'] = maquina
        escolha_maquina['fg'] = cor4
        escolha_jogador['text'] = jogador
        escolha_jogador['fg'] = cor4
        
 # CASO DE EMPATE--------------------------
        
        if jogador == 'PAPEL' and maquina == 'PAPEL':
            print('EMPATE')
            jogador_01_linha['bg'] = cor5
            jogador_02_linha['bg'] = cor5
            empate_linha['bg'] = cor5
            
        elif jogador == 'PEDRA' and maquina == 'PEDRA':
            print('EMPATE')
            jogador_01_linha['bg'] = cor5
            jogador_02_linha['bg'] = cor5
            empate_linha['bg'] = cor5
            
        elif jogador == 'TESOURA' and maquina == 'TESOURA':
            print('EMPATE')
            jogador_01_linha['bg'] = cor5
            jogador_02_linha['bg'] = cor5
            empate_linha['bg'] = cor5   
        
# CASO FOR VITORIA/DERROTA---------    

        elif jogador == 'PAPEL' and maquina == 'TESOURA':
            print('PAPEL é cortado por TESOURA - DERROTA!')
            jogador_01_linha['bg'] = cor7
            jogador_02_linha['bg'] = cor8
            empate_linha['bg'] = cor0
            pontos_maquina += 10
            
        elif jogador == 'PAPEL' and maquina == 'PEDRA':
            print('PAPEL encobre PEDRA - VITORIA!')
            jogador_01_linha['bg'] = cor8
            jogador_02_linha['bg'] = cor7
            empate_linha['bg'] = cor0
            pontos_jogador += 10
            
        elif jogador == 'PEDRA' and maquina == 'TESOURA':
            print('PEDRA esmaga TESOURA - VITORIA!')
            jogador_01_linha['bg'] = cor8
            jogador_02_linha['bg'] = cor7
            empate_linha['bg'] = cor0
            pontos_jogador += 10
            
        elif jogador == 'PEDRA' and maquina == 'PAPEL':
            print('PEDRA é encoberta por PAPEL - DERROTA!')
            jogador_01_linha['bg'] = cor7
            jogador_02_linha['bg'] = cor8
            empate_linha['bg'] = cor0
            pontos_maquina += 10
            
        elif jogador == 'TESOURA' and maquina == 'PAPEL':
            print('TESOURA corta PAPEL - VITORIA!')
            jogador_01_linha['bg'] = cor8
            jogador_02_linha['bg'] = cor7
            empate_linha['bg'] = cor0
            pontos_jogador += 10
             
        elif jogador == 'TESOURA' and maquina == 'PEDRA':
            print('TESOURA é esmagada por PEDRA - DERROTA!')
            jogador_01_linha['bg'] = cor7
            jogador_02_linha['bg'] = cor8
            empate_linha['bg'] = cor0
            pontos_maquina += 10
            
# ATUALIZANDO PONTOS-----------------------------------------------------

        jogador_01_potuacao['text']= pontos_jogador
        jogador_02_potuacao['text']= pontos_maquina
        
# ATUALIZANDO NÚMERO DE ROUNDS-------------------------------------------

        rounds -=1
                   
    else:
        jogador_01_potuacao['text']= pontos_jogador
        jogador_02_potuacao['text']= pontos_maquina


# CHAMANDO A FUNÇÃO  TERMINAR    
        fim_jogo()


 
# FUNÇÃO INICIAR O JOGO----------------------------------------------------

def iniciar_jogo():
    global icone_1
    global icone_2
    global icone_3
    global button_icone_1
    global button_icone_2
    global button_icone_3

    button_jogar.destroy()

# ADICIONANDO IMAGENS----------------------
    icone_1 = Image.open('IMAGENS/PAPEL.png')
    icone_1 = icone_1.resize((100,100), Image.ANTIALIAS)
    icone_1 = ImageTk.PhotoImage(icone_1)
#------------------------------------------
    icone_2 = Image.open('IMAGENS/PEDRA.png')
    icone_2 = icone_2.resize((100,100), Image.ANTIALIAS)
    icone_2 = ImageTk.PhotoImage(icone_2)
#------------------------------------------
    icone_3 = Image.open('IMAGENS/TESOURA.png')
    icone_3 = icone_3.resize((100,100), Image.ANTIALIAS)
    icone_3 = ImageTk.PhotoImage(icone_3)


# CRIANDO BOTÃO COM IMAGEM-----------------
    
    button_icone_1 = Button(frame_baixo, command=lambda: jogar('PAPEL'), width=100, image=icone_1, compound=CENTER, bg=cor0, fg=cor0, font=('helvetica 10 bold'), anchor=CENTER, relief=FLAT)
    button_icone_1.place(x=10, y=60)

#------------------------------------------
    button_icone_2 = Button(frame_baixo, command=lambda: jogar('PEDRA'), width=100, image=icone_2, compound=CENTER, bg=cor0, fg=cor0, font=('helvetica 10 bold'), anchor=CENTER, relief=FLAT)
    button_icone_2.place(x=150, y=60)

#------------------------------------------
    button_icone_3 = Button(frame_baixo, command=lambda: jogar('TESOURA'), width=100, image=icone_3, compound=CENTER, bg=cor0, fg=cor0, font=('helvetica 10 bold'), anchor=CENTER, relief=FLAT)
    button_icone_3.place(x=275, y=60)

# FUNÇÃO TERMINAR O JOGO--------------------------------------------------

def fim_jogo():
    global rounds
    global pontos_jogador
    global pontos_maquina
    global jogador_vencedor

# RENICIANDO AS VARIAVEIS---------------------------------------------
    
    pontos_jogador = 0
    pontos_maquina = 0
    rounds = 9

# DESTRUINDO BOTÕES-----------------------------------------------------    

    button_icone_1.destroy()
    button_icone_2.destroy()
    button_icone_3.destroy()

# DEFININDO O GANHADOR---------------------------------------------------

    jogador_jogador = int(jogador_01_potuacao['text'])
    jogador_maquina = int(jogador_02_potuacao['text'])

    if jogador_jogador > jogador_maquina:
        jogador_vencedor= Label(frame_baixo, text='VOCÊ GANHOU!!!', height=1, anchor='center', font=('helvetica 30 bold'), bg=cor0, fg=cor8)
        jogador_vencedor.place(x=30,y=20)
    elif jogador_jogador < jogador_maquina:
        jogador_vencedor= Label(frame_baixo, text='DERROTADO!!!', height=1, anchor='center', font=('helvetica 30 bold'), bg=cor0, fg=cor7)
        jogador_vencedor.place(x=30,y=20)
    else:
        jogador_vencedor= Label(frame_baixo, text='TUDO EMPATADO!!!', height=1, anchor='center', font=('helvetica 30 bold'), bg=cor0, fg=cor5)
        jogador_vencedor.place(x=30,y=20)

# FUNÇÃO JOGAR NOVAMENTE--------------------------------------------------

def  jogar_denovo():
    jogador_01_potuacao['text'] = '0'
    jogador_02_potuacao['text'] = '0'
    jogador_vencedor.destroy()
    button_jogar_novamente.destroy()

    iniciar_jogo()

icone_5 = Image.open('IMAGENS/RESTART.png')
icone_5 = icone_5.resize((40,40),Image.ANTIALIAS)
icone_5 = ImageTk.PhotoImage(icone_5)
button_jogar_novamente = Button(frame_baixo, command=jogar_denovo, width=40, image=icone_5, compound=CENTER, bg=cor0, fg=cor0, font=('helvetica 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
button_jogar_novamente.place(x=180, y=235)






# BOTÃO DE INICIO DO JOGO----------------------------------------------

icone_4 = Image.open('IMAGENS/START.png')
icone_4 = icone_4.resize((40,40),Image.ANTIALIAS)
icone_4 = ImageTk.PhotoImage(icone_4)
button_jogar = Button(frame_baixo, command=iniciar_jogo, width=40, image=icone_4, compound=CENTER, bg=cor0, fg=cor0, font=('helvetica 10 bold'), anchor=CENTER, relief=RAISED, overrelief=RIDGE)
button_jogar.place(x=180, y=235)


janela.mainloop()