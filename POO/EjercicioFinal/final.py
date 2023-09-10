# from textblob import TextBlob


# class AnalizadorDeSentimientos:
#     def analizar(self, texto):
#         analisis = TextBlob(texto)
#         if analisis.sentiment.polarity > 0:
#             return 'Positivo'
#         elif analisis.sentiment.polarity == 0:
#             return 'Neutral'
#         else:
#             return 'Negativo'
        

import openai

openai.api_base = "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"

system_rol = """Has como si fueras un analizador de sentimientos. 
                yo te paso sentimientos y tu analizas el sentimiento de los mensajes y me das una respuesta
                con al menos 1 caracter y como maximo 4 caracteres SOLO RESPUESTAS NUMERICAS, donde -1 es negatividad maxima,
                0 es neutral  y 1 es positividad maxima (puedes responder con ints o floats)"""


mensajes = [{"role": "system", "content": system_rol}]

class AnalizadorDeSentimientos:
    def analizar(self, polaridad):
        if polaridad > -0.8 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo"  + "\x1b[0;37m"
        elif polaridad > -0.3 and polaridad < -0.1:
            return "\x1b[1;31m" + "Algo negativo"  + "\x1b[0;37m"
        elif polaridad >= -0.1 and polaridad <= 0.1:
            return "\x1b[1;33m" + "Neutral"  + "\x1b[0;37m"
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return "\x1b[1;32m" + "Algo positivo"  + "\x1b[0;37m"
        elif polaridad >= 0.4 and polaridad <= 0.9:
            return "\x1b[1;32m" + "Positivo"  + "\x1b[0;37m"
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "Muy positivo"  + "\x1b[0;37m"
        else:
            return "\x1b[1;32m" + "MUY negativo" + "\x1b[0;37m"
        

analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m" + "\n Decime algo: " + "\x1b[0;37m")
    mensajes.append({"role": "user", "content": user_prompt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )
    respuesta = completion.choices[0].messages["content"]
    mensajes.append({"role": "assistant", "content": respuesta})
    sentimiento = analizador.analizar(float(respuesta))
    print(sentimiento)
