#Victor Lin NommiesOrNo? HackKu
from tkinter import *
from usda import UsdaClient
client = UsdaClient('p1ehKOFsAoCUPS0TuxbTQMUytqlMLPQr11nJNLMZ')
class findNommies:
    def __init__(self):
        window = Tk()
        window.geometry("500x500")
        window.title("Nommies Or No?")

 #       for nutrient in report.nutrients:
#          print(nutrient.name, nutrient.value, nutrient.unit)

        def result(fuud):
            foods_list = client.list_foods(10)
            for _ in range(10):
                food_item = next(foods_list)
                print(food_item.name)
            foods_search = client.search_foods(fuud, 1)
            newFuud = next(foods_search)

            report = client.get_food_report(newFuud.id)
            for nutrient in report.nutrients:
                biz=nutrient.name, nutrient.value, nutrient.unit
                lblresult.delete(0,END)
                lblresult.insert(0,biz)
            return

        Label1 = Label(window, text = "Enter your food item").grid(row = 1, column = 1, sticky = W)

        self.number1Var = StringVar()
        Entry1 = Entry(window, textvariable = self.number1Var, justify = RIGHT).grid(row = 1, column = 2)


        Label3 = Label(window, text = "Here are the Nutrition Facts").grid(row = 3, column = 1, sticky = W)
        Label(window, text = "Here are the Nutrition Facts").columnconfigure(0, weight=10)

        lblresult = Entry(window, justify = RIGHT)
        lblresult.grid(row = 3, column = 2, sticky = E)

        btresult = Button(window,text="Check Nutrition",command=lambda:result(self.number1Var.get()))
        btresult.grid(row = 4, column = 2, sticky = E)

        window.mainloop()

findNommies()




