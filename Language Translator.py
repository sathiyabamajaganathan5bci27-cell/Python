from googletrans import Translator

translator = Translator()
text = "How are you?"
translated = translator.translate(text, dest='ta')
print(translated.text) # "நீங்கள் எப்படி இருக்கிறீர்கள்?"
