print('PC 재고')

class Product:
    def __init__(self, s, y, a, i, c, m ):
        self.stock, self.year, self.amd, self.intel, self.color, self.model = s,y,a,i,c,m

    def ViewState(self):
        print('대수 :', self.stock)
        print('생산년월  :', self.year)
        print('CPU타입(AMD):', self.amd)
        print('CPU타입(INTEL):', self.intel)
        print('컬러 :', self.color)
        print('모델 :', self.model)

    

    

