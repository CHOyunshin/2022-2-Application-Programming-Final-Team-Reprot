class Student:
    def __init__(self, first_name, last_name, height):
        self.first_name, self.last_name, self.height = first_name, last_name, height

    def __str__(self):
        '''
            main.py 스크립트 외부에서 호출이 없어 pass 했다. 
        '''
        pass                

    def __add__(self, other):                  
        '''
            생성된 class instance 사이에서 class 외부에서 + 연산이 없고 
            길어진 문자열의 add 연산은 같은 instance 의 속성간의 연산이고 내부에서 연산이 되므로 pass 했다. 
        '''
        pass  

    def __eq__(self, other):
        return self.height == other.height

    def __lt__(self, other):
        return self.height < other.height

    def __le__(self, other):
        return self.height > other.height

    def get_id(self):
        '''
            asc : str 형태에서 3자리수로 formating 한뒤 문자열을 더해주었다.

            SUM : name의 type인 문자열은 iterable 하기떄문에 map function 을 이용해서 iterator 내부 element를 
            아스키 코드에 해당하는 숫자로 변환해 주는 ord function으로 변환후 list로 저장한후 list의 모든 element를 
            더해주는 sum을 이용해 각 name의 합을 구하였다.
            
            return : str 인 asc를 정수로 변환뒤 합을 구한다음 str로 반환해주었다. 
        '''
        asc = '2021' + '{0:03d}'.format(ord(self.first_name[0])) + '{0:03d}'.format(ord(self.last_name[0]))
        SUM = sum(list(map(ord, list(self.first_name)))) + sum(list(map(ord, list(self.last_name))))
        return str(SUM + int(asc))