class prueba:
    def __init__(self) -> None:
        self.__asunto: None
        self.__id: None

    @property
    def getsetasunto(self):
        return self.__asunto

    @getsetasunto.setter
    def setasunto(self,asunto):
        self.__asunto: asunto

    @property
    def getsetid(self):
        return self.__id

    def getsetid(self,id):
        self.__id = id

    def __repr__(self) -> str:
        print("Es necesario implementar este metodo")
