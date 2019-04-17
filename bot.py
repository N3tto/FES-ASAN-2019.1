import telepot
from random import randint
bot = telepot.Bot('670138261:AAE0shcREGsaR2-Ybn91wYVjtNBXzqqRwpU')

def dado(nDado, qDado):
    lista = []
    for e in range(qDado):
        lista.append(randint(1, nDado))
    return lista

def Msg(msg):
    palavra = msg['text']
    if palavra == '/Classe':
        classes = ['Bárbaro', 'Bardo', 'Bruxo', 'Clérigo', 'Druida', 'Feiticeiro', 'Guerreiro', 'Ladino', 'Mago', 'Monge', 'Paladino', 'Patrulheiro']
        x = randint(0,11)
        bot.sendMessage('Chat ID', classes[x])
    elif palavra == '/Raca':
        racas = ['Anão', 'Elfo', 'Halfling', 'Humano', 'Draconato', 'Gnomo', 'Meio-Elfo', 'Meio-Orc', 'Tiefling']
        x = randint(0,9)
        bot.sendMessage('Chat ID', racas[x])
    elif palavra == '/Nome_masculino':
        nomesM = ['Neto', 'Danilo', 'Jobinha', 'Caio', 'Jesulen', 'Pablo']
        x = randint(0,5)
        bot.sendMessage('Chat ID', nomesM[x])
    elif palavra == '/Nome_feminino':
        nomesF = ['Bia', 'Thammy', 'Brendha', 'Manu', 'Karen', 'Sarah']
        x = randint(0,5)
        bot.sendMessage('Chat ID', nomesF[x])
    elif palavra == '/Status':
        for j in range(6):
            lista = []
            for e in range(4):
                lista.append(randint(1, 6))
            bot.sendMessage('Chat ID', str(lista)[1:-1])
        
    else:
        bot.sendMessage(596431074, 'COMANDO INVALIDO \nLista de comandos:\n\n-/Classe\n-/Raca\n-/Nome_masculino\n-/Nome_feminino\n-/Status')
        

bot.message_loop(Msg)


while True:
    pass
