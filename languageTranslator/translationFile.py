from googletrans import Translator, LANGUAGES


def get_language_code(language_name):
    # Get the language code for the given language name
    for code, name in LANGUAGES.items():
        if name.lower() == language_name.lower():
            return code
    return None


def main():
    print("Welcome to the Text Translator!")

    while True:
        source_lang = input("Enter the source language: ")
        source_lang_code = get_language_code(source_lang)
        if source_lang_code:
            break
        else:
            print("Invalid source language. Please try again.")

    while True:
        target_lang = input("Enter the target language: ")
        target_lang_code = get_language_code(target_lang)
        if target_lang_code:
            break
        else:
            print("Invalid target language. Please try again.")

    text = input(f"Enter the text in {source_lang}: ")

    translator = Translator()
    translation = translator.translate(text, src=source_lang_code, dest=target_lang_code)

    print(f"\nTranslation from {source_lang} to {target_lang}:")
    print(translation.text)


if __name__ == "__main__":
    main()
