import pyautogui as bot
programa = 1
"""
1: fazer espada, armadura
2: descobrir mouse
3: fazer barra

"""
contador = 0

if programa == 1:
    while contador <= 26:

        try:
            #clicar runescape
            bot.click(x=163, y=744)
            bot.sleep(1)

            #clicar forja
            bot.click(x=1244, y=546)
            bot.sleep(1)

            #clicar iniciar projeto
            bot.click(x=1291, y=625)
            bot.sleep(1)

            #clicar minimizar
            bot.click(x=1244, y=355)
            bot.sleep(1)

        except:
            print("Erro, tentando novamente!")

        contador += 1
        print(contador)

        # tempo do mouse
        bot.sleep(75)


elif programa == 2:
    #descobrir posição
    bot.sleep(2)
    print(bot.position())

elif programa == 3:
    while True:
        #clicar runescape
        bot.click(x=168, y=756)
        bot.sleep(1)

        #clicar forja
        bot.click(x=1197, y=504)
        bot.sleep(1)

        #clicar esvaziar
        bot.click(x=1051, y=628)
        bot.sleep(1)

        #clicar runebar
        bot.click(x=1168, y=494)
        bot.sleep(1)

        #clicar iniciar projeto
        bot.click(x=1281, y=621)
        bot.sleep(1)

        #clicar minimizar
        bot.click(x=1237, y=354)
        bot.sleep(1)

        bot.sleep(48)

#fim