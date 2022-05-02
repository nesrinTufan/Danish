class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('__enter__')
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, *args):
        print('__exit__')
        self.file.close()


with OpenFile('DANISH_VERBS.csv', 'r') as f:
    rawData = f.read()



#print(rawData)
lines = rawData.split('\n')
line_gen = (l.split(',') for l in lines) #generation expression/comprehension is the more succint way to create the list
#I am using the generator without calling a function, which yields the row

"""

def csv_reader(filename):
    for roe in open(filename, "r"):
        yield row

"""

print(next(line_gen))


DICT = {}
reading = True
while reading:
    L = next(line_gen, None) #None is an optional argument that is the by default value if generator is exhausted
    if L == None: 
        break #break out of the loop as there are no more lines
    try : 
        presperf = L[-2].split(' ') #I access the 'present perfect' element and split it up by spaces
        L[-2] = presperf[-1] #Replacing. Now the 'present perfect' element (-2) takes only the last part of the string
        DICT[L[1]] = L[2:-1] #I get rid of the example element. It is about populating the dict with only the useful data
    except: # for additional lines in examples
        pass
    

print(DICT['gøre'])
N = len(DICT.keys()) #N = 332 verb stems. I need N because we later generate a random number which represents the key

#flashcardsInf = [k for k in DICT.keys()] #flashcards = ['ae', 'afgå', 'aflevere' ... ]
flashcardsInf = list(DICT.keys()) # 
tenses = ['english', 'present', 'past', 'present perfect']
print(N)


#Hall of Fame - Name, score, precision 