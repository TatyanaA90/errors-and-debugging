def map_character_frequency(words):
    char_map = {}
    for word in words:
        for character in word:
            if character not in char_map:
                char_map[character] = 1
            else:
                char_map[character] += 1
    return char_map

def test_map_character_frequency():
    colors = ["red", "orange"]
    char_map = map_character_frequency(colors)
    expected = {
        "r": 2,
        "e": 2,
        "d": 1,
        "o": 1,
        "a": 1,
        "n": 1,
        "g": 1,
    }
    assert char_map == expected

def syntax_errors():
    test_map_character_frequency()
