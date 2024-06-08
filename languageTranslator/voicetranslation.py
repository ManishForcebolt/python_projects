import googletrans

# print(googletrans.LANGCODES)
translator = googletrans.Translator()
translation = translator.translate("Hello", dest="fr")
print(translation)