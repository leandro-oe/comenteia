# analise/comentario.py
class Comentario:
    ...

    def exibir_info(self):
        return f"O comentário '{self.__texto}' foi classificado como: {self.__sentimento}"

# Subclasses
class ComentarioPositivo(Comentario):
    def exibir_info(self):
        return f"😊 POSITIVO: {self.get_texto()}"

class ComentarioNegativo(Comentario):
    def exibir_info(self):
        return f"😞 NEGATIVO: {self.get_texto()}"

class ComentarioNeutro(Comentario):
    def exibir_info(self):
        return f"😐 NEUTRO: {self.get_texto()}"
