import re


def vonnytize(text):
    """
    Returns vonnytized text

    :param str text:
    :rtype str:
    """
    crop_pattern = r'а|е|ё|и|у|о|ю|я|a|e|i|o|u'
    punctuation = ['.', ',', '?', '!', ':', ';', '-', '\\', '|', '/', '+', "'", '*', '"', '[', ']', '{',
                   '}', '@', '#', '№', '$', '^', '&', '*', '(', ')', '=', '<', '>', '`', '~']

    text = re.sub(r'<.*?>', '', text)
    if not text:
        return ''

    text_prepared = text
    for char in punctuation:
        text_prepared = text_prepared.replace(char, '')

    if not text_prepared:
        return ''

    text_prepared = text_prepared.split(' ')
    words = {}
    for word in text_prepared:
        word = word.strip()
        if word in words:
            continue
        if len(word) <= 3:
            continue
        replace_part = word[1:-1]
        vonni_part = re.sub(crop_pattern, '', replace_part, 0, re.UNICODE | re.IGNORECASE)
        words[word] = word.replace(replace_part, vonni_part)

    for origin, changed in words.items():
        text = text.replace(origin, changed)

    return text
