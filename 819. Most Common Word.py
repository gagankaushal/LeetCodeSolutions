import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        for i in paragraph:
            if i in string.punctuation:
                paragraph = paragraph.replace(i, ' ')
        
        listOfWordsinParagraph = paragraph.lower().split()
        
        freqOfWords = collections.Counter(listOfWordsinParagraph)
        sortedfreq = sorted(freqOfWords.items(), key = lambda x : x[1], reverse = True)
        
        #return sortedfreq
        for i in sortedfreq:
            if i[0] not in banned:
                return i[0]
        #return freqOfWords