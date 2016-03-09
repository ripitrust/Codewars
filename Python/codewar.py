def validate(n):
    return reduce(lambda x,y:x+y,\
          [ value - 9 if value >9 else value for value in \
                [ int(value) * 2 if index % 2 is not 0 else int(value) for index, value in enumerate(str(n)[::-1])]]) % 10 is 0

    

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

    import math

    dim = len(board)

    region = math.sqrt(dim)
    
    for b in board : #row check
    
        if len(set(b)) != dim:
        
            return 'Try again!'
            
    for i in range(dim): # column check
    
        if len(set([a[i] for a in board])) != dim :
        
            return 'Try again!'
    
    for i in range(0,dim,region): #region check
    
        if len(set([board[j][k] for j in range(i,i+region) for k in range(i,i+region)])) != dim:
          
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


def validBraces(string):
    paren_sum = 0
    brack_sum = 0
    curly_sum = 0
    
    for s in string:
        if paren_sum <0 or brack_sum < 0 or curly_sum < 0:
            return False
        if s =='(':
            paren_sum += 1
        elif s == '[':
            brack_sum += 1
        elif s == '{':
            curly_sum += 1
        elif s == ')':
            paren_sum -=1
        elif s == ']':
            brack_sum -= 1
        elif s == '}':
            curly_sum -=1
    return paren_sum ==0 and curly_sum == 0 and brack_sum ==0



import math
class Sudoku(object):
    def __init__(self, board):
        self.board = board
        
        def is_valid(self):
            board = self.board
            dim = len(board)
            region = int(sqrt(dim))
            for b in board : #row check
                if len(set(b)) != dim or set(b) != set(range(1,dim+1)):
                    return False
                else:
                    for j in range(0,dim):
                        if  isinstance(b[j], bool) or b[j] > dim:
                            return False
            for i in range(dim): # column check
                b = [a[i] for a in board]
                if len(set(b)) != dim :
                    return False
            for i in range(0,dim,region): #region check
                b = [board[j][k] for j in range(i,i+region) for k in range(i,i+region)]
                if len(set(b)) != dim :
                    return False
            return True


    def is_valid_bp(self):
        if not isinstance(self.board, list):
            return False
        n = len(self.board)
        rootN = int(round(math.sqrt(n)))
        if rootN * rootN != n:
            return False
        isValidRow = lambda r : (isinstance(r, list) and
                                 len(r) == n and
                                 all(map(lambda x : type(x) == int, r)))
        if not all(map(isValidRow, self.board)):
            return False
        oneToN = set(range(1, n + 1))
        isOneToN = lambda l : set(l) == oneToN
        tranpose = [[self.board[j][i] for i in range(n)] for j in range(n)]
        squares = [[self.board[p+x][q+y] for x in range(rootN) 
                                         for y in range(rootN)] 
                                         for p in range(0, n, rootN)
                                         for q in range(0, n, rootN)] 
        return (all(map(isOneToN, self.board)) and
                all(map(isOneToN, tranpose)) and
                all(map(isOneToN, squares)))




import re
def is_valid_IP(strng):

    return bool(re.match(r"^(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$", strng))



def is_valid_IP_bp(strng):
  lst = strng.split('.')
  passed = 0
  for sect in lst:
    if sect.isdigit():
      if sect[0] != '0':
        if 0 < int(sect) <= 255:
          passed += 1
  return passed == 4




def strip_comments(string, markers):
    if markers:
        pattern = "[" + escape("".join(markers)) + "]"
    else:
        pattern = ''
    return '\n'.join(split(pattern, line)[0].rstrip() for line in string.splitlines())


def roman_to_int(roman):
    roman_map = { 'I':1 , 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    result = 0
    prev_val = 0
    for c in roman[::-1]:
        curr_val  = roman_map[c]
        if (curr_val < prev_val):
          curr_val = 0 - curr_val
        result += curr_val
        prev_val = curr_val
    return result




def strip_url_params(url, params_to_strip = []):
    uri = url.split('?')[0]
    if len(url.split('?')) > 1:  
        params =  url.split('?')[1].split('&')
    else :
        params = []
    params_obj = {}
    for pair in params :
        key = pair.split('=')[0]
        value = pair.split('=')[1]
        if key not in params_to_strip and key not in params_obj:
            params_obj[key] = value
    new_param = ['{0}={1}'.format(k,v) for k,v in params_obj.iteritems()]
    if len(new_param) == 0:
        return uri
    return '?'.join([uri, '&'.join(new_param)])


def same_structure_as(original,other):

    if (isinstance(original,list) and not isinstance(other,list)) or (not isinstance(original,list) and isinstance(other,list)):
        return False
    elif isinstance(original,list) and isinstance(other,list) :
        if len(original) != len(other):
            return False
        for a,b in zip(original,other):
            if not same_structure_as(a,b):
                return False
    return True


class Automaton(object):

    def __init__(self):
        self.states = ['q1','q2','q3']
        self.current_state = self.states[0]
        
    def read_commands(self, commands):
        for c in commands :
            if self.current_state == self.states[0]:
                if c == '0':
                    pass
                elif c =='1':
                    self.current_state = self.states[1]
            elif self.current_state == self.states[1]:
                if c == '0':
                    self.current_state = self.states[2]
                elif c =='1':
                    pass
            elif self.current_state == self.states[2]:
                if c == '0' or c =='1':
                    self.current_state = self.states[1]
                    
        return self.current_state == self.states[1]
                    
my_automaton = Automaton()


class Automaton_bp(object):

    def __init__(self):
        self.automata = {('q1', '1'): 'q2', ('q1', '0'): 'q1', 
                         ('q2', '0'): 'q3', ('q2', '1'): 'q2',
                         ('q3', '0'): 'q2', ('q3', '1'): 'q2'}
        self.state = "q1"

    def read_commands_bp(self, commands):
        for c in commands:
            self.state = self.automata[(self.state, c)]
        return self.state=="q2"

my_automaton = Automaton()

