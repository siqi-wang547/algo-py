class solution:
    """
    LC273. Integer to English Words
    """
    def int2eng(self, x):
        lt20 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen' \
               'Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        if x < 20:
            return lt20[x-1:x]
        elif x < 100:
            return [tens[int(x/10)-2]] + self.int2eng(x%10)
        elif x < 1000:
            return self.int2eng(int(x/100)) + ['Hundred'] + self.int2eng(x%100)
        elif x < 1000000:
            return self.int2eng(int(x/1000)) + ['Thousand'] + self.int2eng(x%1000)
        elif x < 1000000000:
            return self.int2eng(int(x/1000000)) + ['Million'] + self.int2eng(x%1000000)
        else:
            return self.int2eng(int(x/1000000000)) + ['Billion'] + self.int2eng(x%1000000000)

    def numberToWords(self, num):
        return ' '.join(self.int2eng(num)) or 'Zero'

if __name__ == '__main__':
    s = solution()
    print(s.numberToWords(100))