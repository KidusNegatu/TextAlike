from spellchecker import SpellChecker
import re

class TextPreprocess():
    def __init__(self, userInput):
        self.userInput = userInput
        self.noiseRemoved = self.noiseRemove()
        
    def noiseRemove(self):
        return re.sub(r"[^\w\s]", "", self.userInput)
    
    def spellCheck(self):
        spell = SpellChecker()
        words = self.noiseRemoved.lower().split()
        checkedWords = []
        
        for word in words:
            corrected = spell.correction(word)
            if corrected is None:
                checkedWords.append(word)
            else:
                checkedWords.append(corrected)
                
        output = " ".join(checkedWords)
        return output

    def __str__(self):
        return str(self.spellCheck())
