def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars = {}
    for c in text:
        chars[c.lower()] = chars.get(c.lower(), 0) + 1

    return chars

def sort_report(items):
    return items["num"]

def print_default_report(chars):
    char_report = []
    for char,num in chars.items():
        char_report.append({"char": char, 
                            "num": num}
                            )
    char_report.sort(reverse=True, key=sort_report)
    return char_report

