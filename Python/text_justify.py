
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