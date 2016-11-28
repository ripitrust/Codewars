INF = float('inf')


def text_justify(text, width):
    n = len(text) - 1
    badness = {-1: 0}
    for i in range(0, n):
        min_badness = INF
        for j in range(0, i+1):
            badness_result = how_bad(text[j:i], width) + badness[j-1]
            if badness_result < min_badness:
                min_badness = badness_result
        badness[i] = min_badness
    return badness


def how_bad(text, width):
    if len(text) > width:
        return INF
    return (width - len(text)) ** 3


if __name__ == '__main__':

    text = '1234_5678_912345_qwqwe_23231ff_asdag_Re11sdasdsdsadsadsada123456asd'

    badness = text_justify(text, 8)
    break_points = [k for k, v in badness.items() if v == 0 and k != -1]

    result = str()
    start = 0
    index = 0
    for i in break_points:
        index = i
        result += text[start:index+1] + '\n'
        start = index + 1

    result += text[index+1:]
    print result



