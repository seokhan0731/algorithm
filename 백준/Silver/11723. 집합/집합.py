import sys


def control_set(line):
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


# sys.stdin = open("input.txt", "r")
set_val = set()
default_set = set([str(i) for i in range(1, 21)])
for line in sys.stdin:
    control_set(line)
