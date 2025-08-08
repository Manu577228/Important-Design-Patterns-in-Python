# The Adapter pattern allows incompatible interfaces to 
# work together by converting one interface into another expected by the client.

# Useful when integrating legacy code or external libraries with different method names or formats.

class EnglishSpeaker:
    def speak_english(self):
        return "Hello"
    
class Adapter:
    def __init__(self, obj):
        self.obj = obj

    def speak(self):
        return self.obj.speak_english();

eng = EnglishSpeaker()
adapted = Adapter(eng)
print(adapted.speak())        