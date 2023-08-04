def problem1():
    scores = {
    'Kim': {'math': 50, 'english': 70},
    'Park': {'math': 70, 'english': 60},
    'Lee': {'math': 80, 'english': 50}
    }
    total= 0
    total = sum([score['english'] for score in scores.values()])

def problem2():
    students = [
    {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
    {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},
    {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
    ]
  #  for student in students:
        

def problem3():
    students = [
    {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
    {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},
    {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
    ]
    for student in students:
        student['score']['total'] = sum(student['score'].values())
    print(students)

def sum_scores():
    students =[
    {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
    {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},
    {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
    {'id': 4, 'name': 'Choi', 'score': {'math': 70, 'english': 50}},
    ]
   #{'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
   #{'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},
    for student in students:
        result= sum([sum(student['score'].values()) for student in students])
    return result

def Nope():
    result =(lambda x, y:x+y(2,3))
    print (result)

    # 리스트 원소 각각에 적용하고 싶은 함수
    my_list=[1,2,3]
    result =map(lambda x:f'안녕하세요{x}',my_list)
    print(list(result))
    my_list = [1,2,3]
    result =filter(lambda x:x>=2, my_list)
    print(list(result))
    my_list = [1,2,3,4,5,6]
    result = reduce(lambda x, y:x+y, my_list)
    print(result)
    
    response =requests.get("https://www.naver.com")
    response = requests.post('https://jsonplacehoder.typicode.com/posts',{'title': '내글','body':'내용'})
    print(response.text)  

    
from functools import reduce


"""
    - **0) 💯 연습문제 풀어보기 - lambda 와 map, filter, reduce**
    
    **[(필독) 문제 풀기 전 추가 개념 설명]**
    
    ```python
    a = {'math': 50, 'science': 30}
    b = {'english': 70, 'history': 20}
    ```
    
    이라는 딕셔너리가 있을 때, 두 딕셔너리의 요소를 모두 가진 딕셔너리는
    
    ```python
    c = {**a, **b}
    ```
    
    의 형태로 만들 수 있습니다.
    
    **문제를 푸실 때, 리스트 컴프리헨션은 사용 금지입니다!!!!!!!!!!!!!**
    
    1. 아래 리스트에서 수학, 영어 점수의 총합이 140 이상인 사람만 남긴 리스트를 만들어주세요. (filter 활용)
    
    ```python
    students = [
        {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
        {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60}},
        {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
    ]
    ```
    
    1. 아래 리스트에서 모든 점수의 총합을 구하는 코드를 작성해주세요. (reduce 활용)
    
    ```python
    students = [
        {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70, 'science': 60}},
        {'id': 2, 'name': 'Park', 'score': {'math': 80, 'english': 60, 'science': 100}},
        {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50, 'science': 40}},
    ]
    ```
    
    1. 아래 리스트에서 모든 사람들의 이름이 Park 으로 바뀐 리스트를 만들어주세요. (map 활용)
    
    ```python
    students = [
        {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
        {'id': 2, 'name': 'Kim', 'score': {'math': 80, 'english': 60}},
        {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
    ]
    ```
    
    1. 아래 리스트에서 이름이 Kim 인 사람들만 score 에 science: 100 이 추가된 리스트를 만들어주세요. (filter, map 활용)
    
    ```python
    students = [
        {'id': 1, 'name': 'Kim', 'score': {'math': 50, 'english': 70}},
        {'id': 2, 'name': 'Kim', 'score': {'math': 80, 'english': 60}},
        {'id': 3, 'name': 'Lee', 'score': {'math': 70, 'english': 50}},
    ]
    ```
    
    1. 아래 리스트에서, 학생 별로 `total: (점수 총합)` 을 추가하는 코드를 작성하세요. (map 활용)
    """