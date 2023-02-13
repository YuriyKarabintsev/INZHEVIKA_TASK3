import threading
import time

from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        return f'Function {func.__name__}{args} {kwargs} Took {total_time:.10f} seconds Result:\n\t{result}', result

    return timeit_wrapper


def get_possible_moves(xchip: int, ychip: int, direction: str, distance: int, result=None):
    r"""

    :param result:
        result
    :param xchip:
        x coordinate (max = 7)
    :param ychip:
        x coordinate (max = 7)
    :param direction:
        direction of calculation:
        up, down, left, right
    :param distance:
        travel distance (max = 6)
    :return: list
    """
    if result is None:
        result = []
    possible_moves = []

    if (xchip > 7 or xchip < 0) or (ychip > 7 or ychip < 0):
        return []
    if direction == "down":
        i = 0
        while ychip != ychip - distance and 0 <= ychip <= 7:
            if 0 <= xchip - (distance - i) <= 7 and distance - i >= 0:
                possible_moves.append((xchip - (distance - i), ychip))
            if 0 <= xchip + (distance - i) <= 7 and distance - i >= 0:
                possible_moves.append((xchip + (distance - i), ychip))
            i += 1
            ychip += 1
    elif direction == "up":
        i = 0
        while ychip != ychip + distance and 0 <= ychip <= 7:
            if 0 <= xchip - (distance - i) <= 7 and distance - i >= 0:
                possible_moves.append((xchip - (distance - i), ychip))
            if 0 <= xchip + (distance - i) <= 7 and distance - i >= 0:
                possible_moves.append((xchip + (distance - i), ychip))
            i += 1
            ychip -= 1
    elif direction == "left":
        i = 0
        while xchip != xchip - distance and 0 <= xchip <= 7:
            if 0 <= ychip - (distance - i) <= 7 and distance - i >= 0:
                possible_moves.append((xchip, ychip - (distance - i)))
            if 0 <= ychip + (distance - i) <= 7 and distance - i >= 0:
                possible_moves.append((xchip, ychip + (distance - i)))
            i += 1
            xchip += 1
    else:
        i = 0
        while xchip != xchip + distance and 0 <= xchip <= 7:
            if 0 <= ychip - (distance - i) <= 7 and distance - i >= 0:
                possible_moves.append((xchip, ychip - (distance - i)))
            if 0 <= ychip + (distance - i) <= 7 and distance - i >= 0:
                possible_moves.append((xchip, ychip + (distance - i)))
            i += 1
            xchip -= 1

    result.extend(possible_moves)


desk = [[0] * 8 for i in range(8)]
# print(data := get_possible_moves(x=_x, y=_y, direction="right", distance=3))
_x = 7
_y = 0
data = []

desk[_y][_x] = 2


@timeit
def linear_function(x, y):
    result = []
    get_possible_moves(xchip=x, ychip=y, direction="right", distance=6, result=result)
    get_possible_moves(xchip=x, ychip=y, direction="down", distance=6, result=result)
    get_possible_moves(xchip=x, ychip=y, direction="up", distance=6, result=result)
    get_possible_moves(xchip=x, ychip=y, direction="left", distance=6, result=result)
    return result


@timeit
def threading_function(x, y):
    result = []
    # t1 = threading.Thread(target=get_possible_moves, args=(x, y, "right", 6, result))
    t2 = threading.Thread(target=get_possible_moves, args=(x, y, "down", 1, result))
    # t3 = threading.Thread(target=get_possible_moves, args=(x, y, "up", 6, result))
    # t4 = threading.Thread(target=get_possible_moves, args=(x, y, "left", 6, result))

    # t1.start()
    t2.start()
    # t3.start()
    # t4.start()

    # t1.join()
    t2.join()
    # t3.join()
    # t4.join()
    return result


if __name__ == "__main__":
    print(threading_function(0, 0)[0])
    # print(threading_function(3, 3))

    for x, y in threading_function(_x, _y)[1]:
        desk[y][x] = 1

    print("-------------------------------------")
    for x in range(len(desk)):
        print(f"{7 - x + 1}|\t", end="")
        for y in range(len(desk[0])):
            print(desk[x][y], sep="\t", end="\t")
        print("|")

    print("-------------------------------------")
    print(*["\ta", "b", "c", "d", "e", "f", "g", "h"], sep="\t")