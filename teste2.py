import telebot

CHAVE_API = "token"

bot = telebot.TeleBot(CHAVE_API)

# Dicionário para armazenar informações das pessoas
pessoas = {}

# Dicionário para mapear números para animais
numero_para_animal = {
    1: "Avestruz",
    2: "Águia",
    3: "Burro",
    4: "Borboleta",
    5: "Cachorro",
    6: "Cabra",
    7: "Carneiro",
    8: "Camelo",
    9: "Cobra",
    10: "Coelho",
    11: "Cavalo",
    12: "Elefante",
    13: "Galo",
    14: "Gato",
    15: "Jacaré",
    16: "Leão",
    17: "Macaco",
    18: "Porco",
    19: "Pavão",
    20: "Perú",
    21: "Touro",
    22: "Tigre",
    23: "Urso",
    24: "Veado",
    25: "Vaca",
}

def extrair_animal_e_valor(texto):
    partes = texto.split()
    if len(partes) == 2:
        animal, valor = partes
        if animal.isdigit():
            return int(animal), float(valor)
        else:
            for numero, nome in numero_para_animal.items():
                if nome.lower() == animal.lower():
                    return numero, float(valor)
    return None, None

mensagem_sucesso = "Aposta de {} em {} no valor de R${} registrada com sucesso."

@bot.message_handler(commands=["iniciar"])
def iniciar(mensagem):
    texto = "Seu prêmio?\n" \
            "- 20 vezes mais que o valor apostado🤑🤑🤑🤑\n\n" \
            "EXEMPLO DE GANHOS: 👇🏻\n" \
            "$     3 GANHA 60\n" \
            "$     4 GANHA 80\n" \
            "$     5 GANHA 100\n" \
            "$     6 GANHA 120\n" \
            "$     7 GANHA 140\n" \
            "$     8 GANHA 160\n" \
            "$     9 GANHA 180\n" \
            "$   10 GANHA 200\n" \
            "$   15 GANHA 300\n" \
            "$   20 GANHA 400\n" \
            "$   25 GANHA 500\n" \
            "$   30 GANHA 600\n" \
            "$   50 GANHA 1000\n" \
            "$ 100 GANHA 2000\n\n" \
            "🚨 Boa sorte 😘 🚨\n\n" \
            "⚠ RESULTADOS ANTERIORES\n" \
            "07:20⏰- 🐄\n" \
            "09:20⏰- 🐇\n" \
            "11:20⏰- 🦁\n" \
            "14:20⏰- 🦌\n" \
            "16:20⏰- 🐐\n" \
            "18:20⏰-\n" \
            "21:20⏰-\n" \
            "23:20⏰-\n\n" \
            "🍀🍀🍀🍀🥳🥳🥳🥳\n\n" \
            "Apostas mínima R$3,00\n\n" \
            "1: Avestruz\n" \
            "2: Águia\n" \
            "3: Burro\n" \
            "4: Borboleta\n" \
            "5: Cachorro\n" \
            "6: Cabra\n" \
            "7: Carneiro\n" \
            "8: Camelo\n" \
            "9: Cobra\n" \
            "10: Coelho\n" \
            "11: Cavalo\n" \
            "12: Elefante\n" \
            "13: Galo\n" \
            "14: Gato\n" \
            "15: Jacaré\n" \
            "16: Leão\n" \
            "17: Macaco\n" \
            "18: Porco\n" \
            "19: Pavão\n" \
            "20: Perú\n" \
            "21: Touro\n" \
            "22: Tigre\n" \
            "23: Urso\n" \
            "24: Veado\n" \
            "25: Vaca\n" \
            "Qual o seu nome:"

    bot.send_message(mensagem.chat.id, texto)
    bot.register_next_step_handler(mensagem, receber_nome)

def receber_nome(mensagem):
    chat_id = mensagem.chat.id
    nome = mensagem.text
    pessoas[chat_id] = {'nome': nome}
    texto = f"Olá, {nome}! Agora, por favor, escolha o número ou nome do animal e o valor da aposta."
    bot.send_message(chat_id, texto)
    bot.register_next_step_handler(mensagem, receber_aposta)

def receber_aposta(mensagem):
    chat_id = mensagem.chat.id
    texto = mensagem.text
    try:
        nome = pessoas[chat_id]['nome']
        animal, valor = extrair_animal_e_valor(texto)
        if animal and valor:
            if animal not in pessoas:
                pessoas[animal] = []
            pessoas[animal].append({'nome': nome, 'valor': valor, 'status': False})
            mensagem_atualizada = atualizar_mensagem()
            bot.send_message(chat_id, mensagem_atualizada)
        else:
            texto = "Desculpe, não entendi a mensagem. Por favor, envie o nome ou número do animal e o valor da aposta."
            bot.send_message(chat_id, texto)
    except KeyError:
        texto = "Por favor, inicie a conversa usando o comando /iniciar."
        bot.send_message(chat_id, texto)

def extrair_animal_e_valor(texto: str):
    partes = texto.split()
    if len(partes) == 2:
        animal, valor = partes
        if animal.isdigit():
            return int(animal), float(valor)
        else:
            for numero, nome in numero_para_animal.items():
                if nome.lower() == animal.lower():
                    return numero, float(valor)
    return None, None

def atualizar_mensagem():
    mensagem = "Apostas mínima R$3,00\n\n"
    for numero_animal, animal in numero_para_animal.items():
        if animal in pessoas:
            mensagem += f"1:Avestruz\n" \
            "2: Águia\n" \
            "3: Burro\n" \
            "4: Borboleta\n" \
            "5: Cachorro\n" \
            "6: Cabra\n" \
            "7: Carneiro\n" \
            "8: Camelo\n" \
            "9: Cobra\n" \
            "10: Coelho\n" \
            "11: Cavalo\n" \
            "12: Elefante\n" \
            "13: Galo\n" \
            "14: Gato\n" \
            "15: Jacaré\n" \
            "16: Leão\n" \
            "17: Macaco\n" \
            "18: Porco\n" \
            "19: Pavão\n" \
            "20: Perú\n" \
            "21: Touro\n" \
            "22: Tigre\n" \
            "23: Urso\n" \
            "24: Veado\n" \
            "25: Vaca\n" \
                        f"{numero_animal} 🦅 - {animal}\n"
            for aposta in pessoas[animal]:
                nome = aposta['nome']
                valor = aposta['valor']
                mensagem += f"{nome}, R${valor}\n"
    mensagem += f"1:Avestruz\n" \
            "2: Águia\n" \
            "3: Burro\n" \
            "4: Borboleta\n" \
            "5: Cachorro\n" \
            "6: Cabra\n" \
            "7: Carneiro\n" \
            "8: Camelo\n" \
            "9: Cobra\n" \
            "10: Coelho\n" \
            "11: Cavalo\n" \
            "12: Elefante\n" \
            "13: Galo\n" \
            "14: Gato\n" \
            "15: Jacaré\n" \
            "16: Leão\n" \
            "17: Macaco\n" \
            "18: Porco\n" \
            "19: Pavão\n" \
            "20: Perú\n" \
            "21: Touro\n" \
            "22: Tigre\n" \
            "23: Urso\n" \
            "24: Veado\n" \
            "25: Vaca\n" 
    return mensagem

if __name__ == "__main__":
    bot.polling()


#  import telebot

# CHAVE_API = "token"
# bot = telebot.TeleBot(CHAVE_API)

# # Dicionário para armazenar informações das pessoas
# pessoas = {}

# # Dicionário para mapear números para animais
# numero_para_animal = {
#     1: "Avestruz",
#     2: "Águia",
#     3: "Burro",
#     4: "Borboleta",
#     5: "Cachorro",
#     # Adicione o restante dos animais
# }

# @bot.message_handler(commands=["iniciar"])
# def iniciar(mensagem):
#     chat_id = mensagem.chat.id
#     texto = "BOLADA DA LOOK\n\n" \
#             "Pix 📲 16992407850 (CELULAR)\n" \
#             "Nome 👉🏼  VANUSA B SILVA\n\n" \
#             "BANCO SICOB\n\n" \
#             "Seu prêmio?\n" \
#             "- 20 vezes mais que o valor apostado🤑🤑🤑🤑\n\n" \
#             "EXEMPLO DE GANHOS: 👇🏻\n" \
#             "$     3 GANHA 60\n" \
#             "$     4 GANHA 80\n" \
#             # Continue com o restante do texto

#     bot.send_message(chat_id, texto)
#     bot.register_next_step_handler(mensagem, receber_nome)

# def receber_nome(mensagem):
#     chat_id = mensagem.chat.id
#     nome = mensagem.text
#     pessoas[chat_id] = {'nome': nome}
#     texto = f"Olá, {nome}! Agora, por favor, escolha o número ou nome do animal e o valor da aposta."
#     bot.send_message(chat_id, texto)
#     bot.register_next_step_handler(mensagem, receber_aposta)

# def receber_aposta(mensagem):
#     chat_id = mensagem.chat.id
#     texto = mensagem.text
#     try:
#         nome = pessoas[chat_id]['nome']
#         animal, valor = extrair_animal_e_valor(texto)
#         if animal and valor:
#             if animal not in pessoas:
#                 pessoas[animal] = []
#             pessoas[animal].append({'nome': nome, 'valor': valor})
#             mensagem_atualizada = atualizar_mensagem()
#             bot.send_message(chat_id, mensagem_atualizada, parse_mode="Markdown")
#         else:
#             texto = "Desculpe, não entendi a mensagem. Por favor, envie o nome ou número do animal e o valor da aposta."
#             bot.send_message(chat_id, texto)
#     except KeyError:
#         texto = "Por favor, inicie a conversa usando o comando /iniciar."
#         bot.send_message(chat_id, texto)

# def extrair_animal_e_valor(texto):
#     partes = texto.split()
#     if len(partes) == 2:
#         animal, valor = partes
#         if animal.isdigit():
#             return int(animal), float(valor)
#         else:
#             for numero, nome in numero_para_animal.items():
#                 if nome.lower() == animal.lower():
#                     return numero, float(valor)
#     return None, None

# def atualizar_mensagem():
#     mensagem = "Apostas mínima R$3,00\n\n"
#     for numero_animal, animal in numero_para_animal.items():
#         if animal in pessoas:
#             mensagem += f"{numero_animal} 🐦 - {animal}\n"
#             for aposta in pessoas[animal]:
#                 nome = aposta['nome']
#                 valor = aposta['valor']
#                 mensagem += f"<b>{nome}</b>, R${valor}\n"
#             mensagem += "___________________________\n"
#     mensagem += "\n⚠ FECHAMENTO DAS APOSTAS DE CADA CORRIDA:\n\n9:00\n11:00\n14:00\n16:00\n18:00\n21:00\n\n⚠ PAGAMENTOS IMEDIATOS🚨\n☘☘ PEDIU, PAGOU, GANHOU RECEBEU ☘☘\nObs: Somente será válido se for pago antes do sorteio!"
#     return mensagem

# if __name__ == "__main__":
#     bot.polling()
   
# import re
# ... from telegram import Update
# ... from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# ... 
# ... # Dicionário para mapear números para animais
# ... numero_para_animal = {
# ...     1: "Avestruz",
# ...     2: "Águia",
# ...     # ... Adicione os outros animais aqui ...
# ...     25: "Vaca",
# ... }
# ... 
# ... # Dicionário para armazenar informações das pessoas
# ... pessoas = {}
# ... 
# ... # Função para receber e processar a mensagem do usuário
# ... def receber_mensagem(update: Update, context: CallbackContext):
# ...     nome = update.message.from_user.first_name
# ...     mensagem = update.message.text
# ... 
# ...     match = re.search(r'(\d+) (.+)', mensagem)
# ...     if match:
# ...         numero_animal = int(match.group(1))
# ...         if numero_animal in numero_para_animal:
# ...             animal = numero_para_animal[numero_animal]
# ...             valor = float(match.group(2))
# ...             if animal not in pessoas:
# ...                 pessoas[animal] = []
# ...             pessoas[animal].append((nome, valor))
# ...             update.message.reply_text(f"Aposta de {nome} em {animal} de R${valor} adicionada com sucesso.")
# ...         else:
# ...             update.message.reply_text("Número de animal inválido.")
# ...     else:
# ...         update.message.reply_text("Formato da mensagem inválido. Use o formato 'NÚMERO NOME_DO_ANIMAL VALOR'.")

# # Função para listar as apostas
# def listar_apostas(update: Update, context: CallbackContext):
#     mensagem = "Apostas:\n"
#     for animal, apostas in pessoas.items():
#         mensagem += f"{animal}:\n"
#         for nome, valor in apostas:
#             mensagem += f"- {nome}: R${valor}\n"
#     update.message.reply_text(mensagem)

# def main():
#     # Coloque o token do seu bot aqui
#     token = "Token"

#     updater = Updater(token, use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("listar_apostas", listar_apostas))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, receber_mensagem))

#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()
