from math import sqrt

class Point:
    def __init__(self, x=0, y=0):                   
        self.x, self.y = x,y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):            # 클래스멤버에서 equal 연산을 x,y 좌표가 동일한 조건으로 설정
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)