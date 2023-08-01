# 클래스의 형태를 눈으로 익혀봅시다.
class Calculator: # 클래스 선언

    def __init__(self, x, y): # 초기화함수
        self.x = x # 클래스 내 변수 초기화
        self.y = y

    def my_sum(self): # 함수 정의
        z = self.x + self.y
        return z

    def my_minus(self):
        z = self.x - self.y
        return z

    def my_multiply(self):
        z = self.x * self.y
        return z

    def my_division(self):
        z = self.x / self.y
        return z