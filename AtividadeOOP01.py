'''
Aula 14/08 -

Decoradores:
    Getter @property
    Setter @x.setter

'''
class Ponto2D:
    def __init__(self, coord_x = 0, coord_y = 0):
        self.__x = coord_x
        self.__y = coord_y

    @property # "Getter"
    def x(self):
        return self.__x

    @x.setter # "Setter" - Validações
    def x(self, valor):
        if isinstance(valor, (int, float)):

            self.__x = valor

        else:
            raise TypeError("O valor de x deve ser um número")

    @property # "Getter" x
    def y(self):
        return self.__y
    
    @y.setter # "Setter" y - Validações y
    def y(self, valor):
        if isinstance(valor, (int, float)):
            self.__y = valor
    
        else:
            raise TypeError("O valor de y deve ser um número")
        
if __name__=='__main__':
    p1 = Ponto2D(2, 9)
    print(p1.x)
    print(p1.y)