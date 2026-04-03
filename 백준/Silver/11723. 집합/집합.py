import sys


def control_set(line):
    """
    분기 처리를 통한 집합 구현

    집합 메소드 관련
    set.remove()->해당 원소가 존재하지 않는다면, 에러를 뱉기 때문에,
                  set.discard()로 대체
    존재 여부 확인-> ~ in set 사용
    set 합집합-> set.update(이터러블 객체)
                +) 해당 문제에서는 집합에 들어오는 원소가 1~20으로, all연산자를 통해 대체되는 값이 1~20으로
                    단순 합집합을 통해 구현할 수 있지만, 그렇지 않은 경우, 별도의 플래그값을 통해
                    집합의 없는 값들을 모아놓는 형태로 구현(블랙리스트 느낌으로, 1~n까지는 다 값이 있다는 전제이기 때문)

    +) 메모리 초과 관련
    대개 알고리즘 문제 풀이시, data=sys.stdin.read().splitlines()를 통해 별도의 리스트를 만들지만,
    해당 문제에서는 메모리 제한 4MB이기 떄문에, 대햑 4*10^6정도이다. data가 최악의 경우 3*10^6개의 줄을 받는다면,
    8byte(리스트 공간값)*3*10^^6으로 메모리 초과가 발생하기 떄문에, 루프를 통해 들어오는 족족 처리하는 방식을 채택해야했다.

    :param line: 입력으로 주어지는 명령행
    :return: None(원본 set을 함수에서 관리)
    """
    command_component = line.split()
    command = command_component[0]
    if command == 'add':
        set_val.add(command_component[1])
    elif command == "remove":
        set_val.discard(command_component[1])
    elif command == "check":
        print(1 if command_component[1] in set_val else 0)
    elif command == "toggle":
        if command_component[1] in set_val:
            set_val.discard(command_component[1])
        else:
            set_val.add(command_component[1])
    elif command == "all":
        set_val.update(default_set)
    elif command == "empty":
        set_val.clear()
    pass


# sys.stdin = open("input.txt", "r")
set_val = set()
default_set = set([str(i) for i in range(1, 21)])
for line in sys.stdin:
    control_set(line)
