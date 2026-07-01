import math


def solution(prices):
    prices_size = len(prices)
    answer = [math.inf] * prices_size
    monotonic_stack = [[0, prices[0]]]
    for price_idx, price_val in enumerate(prices):

        while monotonic_stack and price_val < monotonic_stack[-1][1]:
            popped_idx = monotonic_stack.pop()[0]
            answer[popped_idx] = price_idx - popped_idx

        monotonic_stack.append([price_idx, price_val])

    for remained_price in monotonic_stack:
        idx = remained_price[0]
        answer[idx] = prices_size - (1 + idx)
    return answer