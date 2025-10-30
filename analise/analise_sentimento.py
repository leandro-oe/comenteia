from textblob import TextBlob

class AnaliseSentimento:
    def classificar_texto(self, texto):
        analise = TextBlob(texto)
        polaridade = analise.sentiment.polarity

        if polaridade > 0:
            return "Positivo"
        elif polaridade < 0:
            return "Negativo"
        else:
            return "Neutro"
