message = input('>')

def emoji_converter(message):
    words = message.split(' ')
    output = ''

    emojis = {
        ":)": "😀",
        ":(": "🙁"
    }

    for word in words:
        output += emojis.get(word, word) + " "

    return output

print(emoji_converter(message))
