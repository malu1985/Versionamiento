

class Vista:
  
    def __init__(self):

        print ("MENU DE CALCULAR VALOR H.E, R.N, H.E.D, H.E.D.N")
        print("1.VALOR HORA EXTRADIURNA")
        print("2.VALOR RECARGO NOCTURNO")
        print("3.VALOR HORA EXTRA NOCTURNA")
        print("4.VALOR HORA EXTRA DOMINICAL D")
        print("5.VALOR HORA EXTRA DOMINICAL N")

        self.option = input()

        print("INGRESE VALOR HORA LABORAL")
        self.SB = input()
        print("INGRESE TOTAL DE HORAS EXTRAS")
        self.HE = input()
        