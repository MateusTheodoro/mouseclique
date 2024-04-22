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
            bot.click(x=344, y=742)
            bot.sleep(1)

            #clicar forja
            bot.click(x=1228, y=434)
            bot.sleep(1)

            #clicar iniciar projeto
            bot.click(x=1271, y=528)
            bot.sleep(1)

            #clicar minimizar
            bot.click(x=1253, y=192)
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
        bot.click(x=347, y=745)
        bot.sleep(1)

        #clicar forja
        bot.click(x=1173, y=385)
        bot.sleep(1)

        #clicar esvaziar
        bot.click(x=1016, y=535)
        bot.sleep(1)

        #clicar runebar
        bot.click(x=1138, y=379)
        bot.sleep(1)

        #clicar iniciar projeto
        bot.click(x=1294, y=531)
        bot.sleep(1)

        #clicar minimizar
        bot.click(x=1260, y=182)
        bot.sleep(1)

        bot.sleep(48)

#fim