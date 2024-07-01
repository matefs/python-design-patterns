from Utils.Burguer import Burguer

class BurguerFactory:
    
    def createBurguer(self):
        ingredients = ["hamburger","cheese","fries"]
        return Burguer(ingredients)
    
    def createDeluxeCheeseBurguer(self):
        ingredients = ["hamburger","cheese","fries","bacon"]
        return Burguer(ingredients)

burguerFactory = BurguerFactory()
print(burguerFactory)
burguerFactory.createBurguer().print()
burguerFactory.createDeluxeCheeseBurguer().print()

