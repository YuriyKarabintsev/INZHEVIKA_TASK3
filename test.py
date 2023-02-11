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
        return f'Function {func.__name__}{args} {kwargs} Took {total_time:.10f} seconds Result:\n\t{result}'

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
_x = 3
_y = 3
data = []


@timeit
def linear_function(x, y):
    result = []
    get_possible_moves(xchip=x, ychip=y, direction="right", distance=3, result=result)
    get_possible_moves(xchip=x, ychip=y, direction="down", distance=3, result=result)
    get_possible_moves(xchip=x, ychip=y, direction="up", distance=3, result=result)
    get_possible_moves(xchip=x, ychip=y, direction="left", distance=3, result=result)
    return set(result)


@timeit
def threading_function(x, y):
    result = []
    t1 = threading.Thread(target=get_possible_moves, args=(x, y, "right", 3, result))
    t2 = threading.Thread(target=get_possible_moves, args=(x, y, "down", 3, result))
    t3 = threading.Thread(target=get_possible_moves, args=(x, y, "up", 3, result))
    t4 = threading.Thread(target=get_possible_moves, args=(x, y, "left", 3, result))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t1.join()
    t1.join()
    t1.join()
    return set(result)


if __name__ == "__main__":
    print(linear_function(3, 3))
    print(threading_function(3, 3))
