# Diccionario que guarda algunas palabras modernas y su significado
meme_dict = {
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "LOL": "Una respuesta común a algo gracioso",
    "ROFL": "ROFL se utiliza como reacción a algo gracioso, similar a LOL"
    "HOLA": "Saludar"
    "COMO ESTAS": "Es para saber como estas emocionalmente"
    
}

# Pedimos al usuario que escriba una palabra en mayúsculas
word = input("Escribe una palabra moderna que no entiendas (¡utiliza mayúsculas!): ")

# Verificamos si la palabra está en nuestro diccionario
if word in meme_dict.keys():  # .keys() obtiene todas las palabras que tenemos en el diccionario
    print(meme_dict[word])  # Si la palabra está, mostramos su significado
else:
    print("Todavía no tenemos esta palabra... Pero estamos trabajando en ella.")  # Si no está, damos un mensaje amigable
