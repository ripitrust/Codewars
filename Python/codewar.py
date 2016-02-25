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

def rotate2(arr, n):

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

