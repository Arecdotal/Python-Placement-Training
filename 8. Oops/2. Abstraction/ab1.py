'''1st way to achieve Abstraction Method'''

class Meal:
    def _cookrajma(self): # _ lagane se normal se private ho gya
        print("Rajma Prepared")
    def __cookrumaliroti(self):
        print("Roomali Roti Prepare") 
    def __cooksalad(self):
        print("Salad Prepared Prepared")
    def __cookrice(self):
        print("Rice prepared")
    def __cooksweet(self):
        print("Sweet Prepared...")   

    def cookmeal(self):
        self.__cookrajma()
        self.__cookrumaliroti()
        self.__cooksalad()
        self.__cookrice()
        self.__cooksweet()    

if __name__ == '_main_':
    m = Meal()
    m.cookmeal()