INF = float('inf')


def text_justify(text, width):

    word_length = [len(word) for word in text.split()]

    n = len(word_length)

    extras = [[INF] * (n+1) for _ in range(n+1)]
    lc = [[INF] * (n+1) for _ in range(n+1)]
    c = [INF for _ in range(n+1)]
    p = [INF for _ in range(n+1)]

    #calculate extra spaces if i to j are in a single line
    for i in range(1, n+1):
        extras[i][i] = width - word_length[i-1]
        for j in range(i+1, n+1):
            extras[i][j] = extras[i][j-1] - word_length[j-1] - 1


    #calculate line cost according to the extra spaces
    for i in range(1, n+1):
        for j in range(i, n+1):
            if extras[i][j] < 0:
                lc[i][j] = INF
            elif j == n and extras[i][j] >= 0: # ignore the last line
                lc[i][j] = 0
            else:
                lc[i][j] = extras[i][j] ** 3

    c[0] = 0

    for j in range(1, n+1):
        c[j] = INF
        for i in range(1, j+1):

            if c[i-1] != INF and lc[i][j] != INF and (c[i-1] + lc[i][j] < c[j]):

                c[j] = c[i-1] + lc[i][j]
                p[j] = i # parent pointers , j is the start word, i is the optimal end word, so p[word] = optimal start

    return p, n, extras, text


def neat_print(p, n, extras, text):

    if p[n] == 1:
        k = 1
        line_text = ''
    else:
        k, line_text = neat_print(p, p[n] - 1, extras, text)

    extra_spaces = extras[p[n]][n]
    words = text.split()[p[n]-1:n]

    wc = len(words)

    # if wc != 1:
    #     space_for_each = (extra_spaces / (wc - 1)) + 1
    #     remains = extra_spaces % (wc - 1)
    #
    # else:
    #     space_for_each = extra_spaces + 1
    #     remains = 0
    #
    # index = 0
    # while remains != 0:
    #     words[index] += '+'
    #     index += 1
    #     remains -= 1

    print k, p[n], n
    line_text += ('+' * 1).join(words)
    line_text += '\n'

    return k, line_text


if __name__ == '__main__':

    # text = '1234 5678 912345 qwqwe 23231ff asdag Re11s dasds dsad sadsada 123456 asd'
    # text = 'hello this world he don know the dark side of the force'

    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ' \
           'Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. ' \
           'In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. ' \
           'Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, ' \
           'nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. ' \
           'Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. ' \
           'Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. ' \
           'In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. ' \
           'Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ' \
           'ut elementum justo nulla et dolor.'

    # text = 'a b c d e'

    width = 25

    k, result = neat_print(*text_justify(text, width))

    result = result[:-1].split('\n')

    result[len(result) - 1] = ' '.join(result[len(result) - 1].split())

    print '\n'.join(result)













