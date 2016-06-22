class Morse:

    @classmethod
    def to_twos_comp(cls, val, bits):
        if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
            val = val - (1 << bits)        # compute negative value
        return val

    @classmethod
    def from_twos_comp(cls, n, bits):
        s = bin(n & int("1"*bits, 2))[2:]
        return ("{0:0>%s}" % (bits)).format(s)

    @classmethod 
    def split_str(self, string, base):
        """split the binary string according to required bit offsets"""
        iter = len(string) / base
        arr = []
        for i in range(iter + 1):
            bits = string[i * base: (i+1) * base]
            if len(bits) <32:
                bits += '0' * (32 - len(bits))
            arr.append(bits)
        return arr

    @classmethod
    def encode(self,message):

        encoded_str = ['0000' if c ==' ' else self.alpha[c] + '000' for c in message ]

        return [self.to_twos_comp(int(s, 2), len(s)) for s in self.split_str(''.join(encoded_str), 32)]

    @classmethod
    def decode(self, array):
        bit_str = ''
        letter_arr = []
        word_arr = []
        decoded_arr = []
        for digit in array:
            bit_str += self.from_twos_comp(digit, 32)
        bit_str = bit_str.rstrip('0')
        sentence_arr = bit_str.split('0000000')

        word_arr = [s.split('000') for s in sentence_arr]

        for word in word_arr:
            word_decoded = ''
            for c in word:
                word_decoded+=self.inv_alpha[c]

            decoded_arr.append(word_decoded)
        return ' '.join(decoded_arr)


    inv_alpha = {'11101110111011101': '9', '101011101110111': '2', '101011101110101': '?', '11101': 'N', '1110101011101': '/',
                 '1110111': 'M', '10101110111010111': '_', '101110101': 'L', '11101010101': '6', '10111010111010111': '.',
                 '1110101010111': '=', '1011101011101': '+', '11101110101': 'Z', '111': 'T', '10111011101011101': '@',
                 '10111010101': '&', '1010101110111': '3', '10101': 'S', '11101110111': 'O', '101110101011101': '"', 
                 '10101011101010111': '$', '10111011101110111': '1', '111011101': 'G', '101010111': 'V', '1': 'E', 
                 '0': ' ', '1110101110111': 'Y', '11101110111010101': ':', '11101011101011101': ';', '1110111010111': 'Q', 
                 '111010101': 'B', '111011101110101': '8', '111010111011101': '(', '11101010111': 'X', '1010101': 'H', 
                 '101110111': 'W', '1011101': 'R', '10101010111': '4', '1110111010101': '7', '1011101110111011101': "'", 
                 '1110101': 'D', '101': 'I', '10111': 'A', '10111011101': 'P', '1110111011101110111': '0', '1011101110111': 'J', 
                 '101010101': '5', '1110111010101110111': ',', '111010101010111': '-', '1110101110111010111': ')', '11101011101': 'C', 
                 '1010111': 'U', '1110101110101110111': '!', '111010111': 'K', '101011101': 'F'}


    alpha = {' ': '0', '"': '101110101011101', '$': '10101011101010111', '&': '10111010101', '(': '111010111011101', 
             ',': '1110111010101110111', '.': '10111010111010111', '0': '1110111011101110111', '2': '101011101110111', 
             '4': '10101010111', '6': '11101010101', '8': '111011101110101', ':': '11101110111010101', '@': '10111011101011101', 
             'B': '111010101', 'D': '1110101', 'F': '101011101', 'H': '1010101', 'J': '1011101110111', 'L': '101110101', 'N': '11101', 
             'P': '10111011101', 'R': '1011101', 'T': '111', 'V': '101010111', 'X': '11101010111', 'Z': '11101110101', 
             '!': '1110101110101110111', "'": '1011101110111011101', ')': '1110101110111010111', '+': '1011101011101', 
             '-': '111010101010111', '/': '1110101011101', '1': '10111011101110111', '3': '1010101110111', '5': '101010101', 
             '7': '1110111010101', '9': '11101110111011101', ';': '11101011101011101', '=': '1110101010111', '?': '101011101110101', 
             'A': '10111', 'C': '11101011101', 'E': '1', 'G': '111011101', 'I': '101', 'K': '111010111', 'M': '1110111', 'O': '11101110111', 
             'Q': '1110111010111', 'S': '10101', 'U': '1010111', 'W': '101110111', 'Y': '1110101110111', '_': '10101110111010111'}
 
import re
class Morse:
    @classmethod
    def encode(self, message):
        bits = "0000000".join(["000".join([Morse.alpha[char] for char in word])
                               for word in message.split(' ')])
        return [int((int("{0:0<32s}".format(bit32), base=2) + 0x80000000) % 0x100000000 - 0x80000000)
                for bit32 in re.findall(r'.{1,32}', bits)]
    
    @classmethod
    def decode(self,array):
        code = ''.join(["{0:032b}".format((i + 0x100000000) % 0x100000000) for i in array]).rstrip('0')
        return ' '.join([ ''.join([Morse.alpha_re[char] for char in word.split("000")])
                          for word in  code.split("0000000")])
