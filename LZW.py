
class Alphabet:
    @staticmethod
    def GetCapitalLetters():
        return "#ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    @staticmethod
    def GetAlphabetASCII():
        alphabet=[]
        for i in range(32,128):
            alphabet.append(chr(i))
        return ''.join(alphabet)
            
class LZW(object):
    
    def __init__(self, alphabet):
        self._alphabet = alphabet
    
    def Encode(self, data):
        result=[]
        counter=0
        tableEncode={}
        for c in self._alphabet:
            tableEncode[c]=counter
            counter+=1
        sequence = ''                       
        for c in data+'#':
            if '#' == c:
                result.append(tableEncode[sequence])
                break
            sequenceC = sequence + c
            if sequenceC not in tableEncode:
                tableEncode[sequenceC]=counter
                counter+=1
                result.append(tableEncode[sequence])
                sequence=c
            else:
                sequence=sequenceC                    
        return result
    
    def Decode(self, data):
        result=[]
        counter=0
        tableDecode={}
        conjecture=''
        for c in self._alphabet: 
            tableDecode[counter]=c
            counter+=1
            
        result.append(tableDecode[data[0]])
        conjecture=tableDecode[data[0]]
        for d in data[1:]:
            if d == counter: #tricky case
                tableDecode[counter]=conjecture+conjecture[0]
            result.append(tableDecode[d])
            tmp=conjecture+tableDecode[d][0]  ##### only append one char
            tableDecode[counter]=tmp
            counter+=1
            conjecture = tableDecode[d]
        return ''.join(result)
                          
lzw=LZW(alphabet=Alphabet().GetCapitalLetters())

assert [1, 2, 27, 29]==lzw.Encode("ABABABA")
assert "ABABABA"==lzw.Decode([1, 2, 27, 29])
assert [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34] == lzw.Encode("TOBEORNOTTOBEORTOBEORNOT")
assert "TOBEORNOTTOBEORTOBEORNOT"==lzw.Decode([20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
test="HELLOWORLDHELLOWORLDHETOBEORNOTTOBEORTOBEORNOTLLOWORLDHELLOWORLDHELLOWORLD"
assert test == lzw.Decode(lzw.Encode(test))

lzw=LZW(alphabet=Alphabet().GetAlphabetASCII())
test="Canada is a country in North America. Its ten provinces and three territories extend from the Atlantic to the Pacific and northward into the Arctic Ocean, covering 9.98 million square kilometres (3.85 million square miles), making it the world's second-largest country by total area. Its southern and western border with the United States, stretching 8,891 kilometres (5,525 mi), is the world's longest bi-national land border. Canada's capital is Ottawa, and its three largest metropolitan areas are Toronto, Montreal, and Vancouver."
assert test == lzw.Decode(lzw.Encode(test))

#
#
#
#
        
        