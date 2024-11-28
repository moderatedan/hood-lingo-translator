# Define slang dictionaries for different levels
slang_dict = {
    "Level 1": {
        "hello": "yo",
        "friend": "homie",
        "what's up": "wassup",
        "going to": "gonna",
        "them": "them",
        "my": "mah",
    },
    "Level 2": {
        "hello": "wassup",
        "friend": "fam",
        "what's up": "sup",
        "going to": "finna",
        "them": "dem",
        "my": "ma",
    },
    "Level 3": {
        "hello": "ayyo",
        "friend": "dawg",
        "what's up": "wazzuh",
        "going to": "boutta",
        "them": "dem",
        "my": "mah",
    },
}

def translate_to_hood_lingo(text, level):
    """
    Translates input text into hood lingo based on the chosen level.
    :param text: The input text (string).
    :param level: Lingo level (1, 2, or 3).
    :return: Translated text.
    """
    if level not in [1, 2, 3]:
        raise ValueError("Invalid level. Choose 1, 2, or 3.")
    
    # Get the appropriate slang dictionary
    lingo_dict = slang_dict[f"Level {level}"]

    # Split text into words and translate
    words = text.split()
    translated_words = []
    for word in words:
        # Check for slang replacement
        translated_words.append(lingo_dict.get(word.lower(), word))

    # Return the translated sentence
    return " ".join(translated_words)


# Example usage
if __name__ == "__main__":
    print("Welcome to the Hood Lingo Translator!")
    print("Levels: 1 (Mild), 2 (Moderate), 3 (Extreme)")

    user_input = input("Enter your text: ")
    level = int(input("Choose a slang level (1, 2, or 3): "))
    
    try:
        translated_text = translate_to_hood_lingo(user_input, level)
        print(f"Translated Text (Level {level}): {translated_text}")
    except ValueError as e:
        print(e)
