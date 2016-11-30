
def justify(text, width):
    words = text.split()
    maxWidth = width
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += ' '
            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)

        result = res + [' '.join(cur).ljust(maxWidth)]
    result[len(result) - 1] = ' '.join(result[len(result) - 1].split())

    new_result = map(lambda s: s.rstrip(), result)

    return '\n'.join(new_result)

def justify_best_practice(text, width):
    length = text.rfind(' ', 0, width+1)
    if length == -1 or len(text) <= width: return text
    line = text[:length]
    spaces = line.count(' ')
    if spaces != 0:
        expand = (width - length) / spaces + 1
        extra = (width - length) % spaces
        line = line.replace(' ', ' '*expand)
        line = line.replace(' '*expand, ' '*(expand+1), extra)
    return line + '\n' + justify(text[length+1:], width)


INF = float('inf')

def justify2(text, width):

    c = [INF for _ in range(len(text) + 1)]
    p = [INF for _ in range(len(text) + 1)]
    n = len(text)

    c[0] = 0

    for i in range(1, n+1):
        for j in range(1, i+1):
            badness = cost(text[j-1:i], width) + c[j-1]
            if badness < c[i]:
                c[i] = badness
                p[i] = j

    return c, p


def cost(words, width):

    num_space = len(words) - 1
    length = reduce(lambda y, w: len(w) + y, words, 0)
    if length + num_space > width:
        return INF
    return (width - length - num_space) ** 3



def print_wrap(c, text):

    pass















if __name__ == '__main__':

    #text = 'a b c d e f'.split()
    text = 'hello world come to the dark side of the force'.split()
    width = 11
    c, p = justify2(text, width)












