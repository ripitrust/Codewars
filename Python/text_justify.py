INF = float('inf')

# INF = 9999999999

def text_justify(text, width):

    length = len(text) - 1
    dp = {length: 0}

    def get_dp(index):
        if dp.get(index, None):
            return dp.get(index)
        min_badness = INF
        for j in range(index + 1, length + 1):
            b = badness(text[i:j], width) + get_dp(j)
            if b < min_badness:
                min_badness = b
        dp[index] = min_badness
        return min_badness

    for i in range(0, length):

        print get_dp(i)

    return dp


def badness(text, width):

    print text
    if len(text) > width:
        return INF
    return (width - len(text)) ** 3


if __name__ == '__main__':

    result = text_justify('1'
                          '23_4'
                          '5_69'
                          '9987'
                          '5431'
                          '2312', 4)
    print result