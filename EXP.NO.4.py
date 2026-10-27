def pluralize(noun):
    lower = noun.lower()

    # Nouns ending in consonant + y
    if lower.endswith('y') and len(noun) > 1 and lower[-2] not in 'aeiou':
        return noun[:-1] + 'ies'

    # Nouns ending in s, sh, ch, x, or z
    elif lower.endswith(('s', 'sh', 'ch', 'x', 'z')):
        return noun + 'es'

    # Default plural rule
    else:
        return noun + 's'

nouns = ["cat", "dog", "bus", "box", "baby", "church"]
for noun in nouns:
    print(noun, "->", pluralize(noun))
