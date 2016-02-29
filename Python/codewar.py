def validate(n):
    step0_list = str(n)[::-1]
    print step0_list
    step1_list = [ int(value) * 2 if index % 2 is 0 else int(value) for index, value in enumerate(step0_list) ]
    print step1_list
    step2_list = [ value - 9 if value >9 else value for value in step1_list]
    print step2_list
    result3 = reduce(lambda x,y:x+y, step2_list)
    return result3 % 10 is 0


def chained(functions):

    def operation(operand):
	result = operand
        for f in functions:
            result = f(result)
	    print result

    return operation



def rotate(nums, k):
    # ...
    n = len(nums)
    if k ==0:
        pass
    else:
        k = k % n
        nums[:n-k:1] = nums[-(k+1):-(n+1):-1]
        nums[n-k:n:1] = nums[-1:-(k+1):-1]
        nums[::1] = nums[::-1]

    return nums

def rotate_clever(arr, n):

    n = n % len(arr)
    return arr[-n:] + arr[:-n]

def likes(names):
    n = len(names)
    if n == 0:
        return 'no one likes this'

    elif n == 1:
    	return '%s likes this' % (names[0])
    elif n == 2:
    	return '%s and %s like this' % (names[0], names[1])
    elif n == 3:
    	return '%s, %s, and %s like this' % (names[0], names[1], names[2])
    else:
    	return '%s, %s, and %d others like this' % (names[0], names[1], n - 2)


def likes_best(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True

    elif num % 2 == 0 or num % 3 ==0:
    	return False

    else:
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i+2) == 0 :
                return False

            i += 6

        return True


def unique_in_order(iterable):
    result = []
    prev = None
    for i in iterable:
        if i == prev:
            pass
        else:
            result.append(i)
            prev = i
    return result


def valid_parentheses(string):
    sum = 0
    for i in string:
        if sum < 0 :
            return False
        if i == '(':
            sum += 1
        elif i == ')':
            sum -=1
    return sum == 0


def to_underscore(input):
    result = []
    string = str(input)
    result.append(string[0].lower())

    for i in xrange(1,len(string)):

        s = string[i]

        if s.isupper():
            result.append('_')

        result.append(s.lower())


    return ''.join(result)




def get_score(n):
    return 50 * sum(range(1,n+1))


def done_or_not(board): #board[i][j]

    dim = len(board)
    
    for b in board : #row check
    
        if len(set(b)) != dim:
        
            return 'Try again!'
            
    for i in range(dim): # column check
    
        if len(set([a[i] for a in board])) != dim :
        
            return 'Try again!'
    
    for i in range(0,dim,3): #region check
    
        if len(set([board[j][k] for j in range(i,i+3) for k in range(i,i+3)])) != 9:
          
            return 'Try again!'
            
            
    return 'Finished!'


def done_or_not_clever(board):
  rows = board
  cols = [map(lambda x: x[i], board) for i in range(9)]
  squares = [
    board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
      for i in range(0, 9, 3)
      for j in range(0, 9, 3)]
    
  for clusters in (rows, cols, squares):
    for cluster in clusters:
      if len(set(cluster)) != 9:
        return 'Try again!'
  return 'Finished!'



def multiplication_table(row,col):
    
    list = [i*j for i in xrange(1,row+1) for j in xrange(1,col+1)]
    
    return [list[i:i+col] for i in xrange(0,row * col,col)]


def multiplication_table_bp(row,col):
    return [[(i+1)*(j+1) for j in range(col)] for i in range(row)]


def multiplication_table_clever(row,col):
    return [range(i,i*col+1,i) for i in range(1,row+1)]



def create_iterator(func, n):

    def _iterator(value):
        for i in xrange(n):
            value += func(value)
        return value
            
    return _iterator



def create_iterator_bp_clever(func, n):
  if n == 1: return func
  return lambda x : func(create_iterator(func, n-1)(x))




def rot13(message):
    map = { 'A': 'N', 'C': 'P', 'B': 'O', 'E': 'R', 'D': 'Q', 'G': 'T', 'F': 'S', 
            'I': 'V', 'H': 'U', 'K': 'X', 'J': 'W', 'M': 'Z', 'L': 'Y', 'O': 'B',
            'N': 'A', 'Q': 'D', 'P': 'C', 'S': 'F', 'R': 'E', 'U': 'H', 'T': 'G',
            'W': 'J', 'V': 'I', 'Y': 'L', 'X': 'K', 'Z': 'M', 'a': 'n', 'c': 'p', 
            'b': 'o', 'e': 'r', 'd': 'q', 'g': 't', 'f': 's', 'i': 'v', 'h': 'u', 
            'k': 'x', 'j': 'w', 'm': 'z', 'l': 'y', 'o': 'b', 'n': 'a', 'q': 'd',
            'p': 'c', 's': 'f', 'r': 'e', 'u': 'h', 't': 'g', 'w': 'j', 'v': 'i', 
            'y': 'l', 'x': 'k', 'z': 'm'}
            
            
    return ''.join([map.get(char,char) for char in message])



def rot13_bp(message):
    def decode(c):
        if 'a' <= c <= 'z':
            base = 'a'
        elif 'A' <= c <= 'Z':
            base = 'A'
        else:
            return c
        return chr((ord(c) - ord(base) + 13) % 26 + ord(base))
    return "".join(decode(c) for c in message)