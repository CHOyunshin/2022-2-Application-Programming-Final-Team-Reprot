class Normal:
    def __init__(self, mileage):        # instance가 생성될때 constructor 선언
        self.mileage = mileage
        
    def __str__(self):                  # instance가 print를 통해 str로 출력되는 return을 설정
        return f'mileage = {str(self.mileage)}'
        
    def _calc(self, amount):            # method의 parameter의 경우 별도로 self를 사용하지 않음
        return amount + self.mileage
        
    def deposit(self, amount):          # 클래스 멤버 method를 다른 멤버 method에서 접근할때에도 self를 이용
        return self._calc(amount)

class Vip(Normal):                      # Normal로 부터 클래스 멤버변수 mileage를 받음 
    def _calc(self, amount):
        return 2*amount + self.mileage