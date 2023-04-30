from Modelo import Model
from Vista import Vista
class View:
    obj_Model= Model()
    obj_view = Vista()
    obj_Model.setHE(obj_view.HE)
    obj_Model.setSB(obj_view.SB)
    SB = float(obj_Model.getSB())
    HE = float(obj_Model.getHE())
    option = int(obj_view.option)

    if option == 1:
        obj_Model.ED(SB, HE)
    elif option == 2:
         obj_Model.RN(SB, HE)
    elif option == 3:
         obj_Model.EN(SB, HE)
    elif option == 4:
         obj_Model.EDD(SB, HE)
    elif option == 5:
         obj_Model.EDN(SB, HE)

    print("EL VALOR DE LA HORA ES: ", obj_Model.getResult())   
