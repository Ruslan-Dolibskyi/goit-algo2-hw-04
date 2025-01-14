from trie import Trie

class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not strings or not all(isinstance(s, str) for s in strings):
            return ""

        # Знайти найдовший спільний префікс
        prefix = strings[0]
        for string in strings[1:]:
            # Скорочуємо prefix, поки він не стане спільним
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["same", "same", "same"]
    assert trie.find_longest_common_word(strings) == "same"

    trie = LongestCommonWord()
    strings = ["prefix", "pref", "pre"]
    assert trie.find_longest_common_word(strings) == "pre"

    print("Усі тести пройдено успішно!")
