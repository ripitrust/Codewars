
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

    """
    the c array in ths function is the smallest sum cost of justification,
    the p array is the parent point array

    For example, 'a b c d e' justify to width 3:

    c[i] means the smallest cost of justify from 1 to i words
    p[i] means the end word index for start word i of the optimal solution

    there is a choice between constructing the pointer array from end to start
    or from start to end

    in the case of cubed cost function, only from end to start works


    """

    c = [INF for _ in range(len(text) + 1)]
    p = [INF for _ in range(len(text) + 1)]
    n = len(text)

    c[0] = 0

    for i in range(1, n+1):
        for j in range(1, i+1):

            badness = cost(text[j-1:i], width, i, j) + c[j-1]

            if badness <= c[i] and badness != INF:
                c[i] = badness
            # if badness < c[j]: #update parent pointer
                p[i] = j

    return c, p


def cost(words, width, i, j):

    """ cubic error will not work here, because in some cases, the second line error, when cubed,
    will be significantly larger than some previous line error , this lead to the parent pointer not
     updated and be inf, so the cost function determines how should the line be justified, if a cube cost is used,
      it means that the space for each line must be as even as possible,  since one space for each line costs much less
      than three space for one line and zero for two other lines:

            1 ** 3 + 1 ** 3 + 1** 3 = 3  <<  3 ** 3 + 0 + ) = 27

    So if the cost function is cubed, the algorithm will try to spread the word as even as possible, but when not cubed,

    it will pack as many word as possible for one line, but will not care the uneven big spaces in the following lines

    and the latter is what leetcode / codewars are asking for

    """

    num_space = (i - j)
    length = reduce(lambda y, w: len(w) + y, words, 0)
    if length + num_space > width:
        return INF
    return (width - length - num_space) ** 3



def print_wrap(p, text, width):
    i = 1
    result = []
    while i <= len(text) and p[i] != INF:

        words = text[i-1: p[i]]
        total_length = reduce(lambda y, w: y + len(w), words, 0)
        extra_space = width - total_length - p[i] + i  # extra spaces , not include space between words

        pos = 0

        while extra_space > 0:
            if pos > len(words) - 2:
                pos = 0
            words[pos] += ' '
            pos += 1
            extra_space -= 1

        result .append(' '.join(words))
        i = p[i] + 1

    if i-1 < len(text):
        words = text[i-1:]

        result.append(words)

    return result

def print_wrap_end(p, text, width):

    i = len(text)

    result = []

    while i >= 0 and p[i] != INF:

        print p[i], i

        word = text[p[i] - 1: i]

        res = ' '.join(word)

        result.append(res)

        i = p[i] - 1

    return result[::-1]


if __name__ == '__main__':

    # text = 'a b c d e'.split()

    # text = 'Lorem  ipsum  dolor  sit amet, consectetur  adipiscing  elit. Vestibulum    sagittis   dolor mauris,  at  elementum  ligula'.split()
    text = 'Lorem  ipsum  dolor  sit amet, consectetur  adipiscing  elit.'.split()

    # text = 'Here is an example of text justification'.split()
    # text = 'what must be shall be.'.split()

    # text = 'hello world come to the dark side of the force'.split()
    width = 20
    c, p = justify2(text, width)
    print c
    print p

    print "Ref".center(width, "-")
    print justify_best_practice(' '.join(text), width)
    print "=".center(width, "-")

    result = print_wrap_end(p, text, width)

    # result[len(result) - 1] = (' '.join(result[len(result) - 1].split())).ljust(width)  #only works for leetcode

    print result











