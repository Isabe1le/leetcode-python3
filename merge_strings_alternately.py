# https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        min_word_len = min(word1_len, word2_len)
        merged_word  = ""

        # Merge the words alternately
        # While-loops are faster than for-loops for
        # small integers as of 3.11
        i = 0
        while i < min_word_len:
            word1_c = word1[i]
            word2_c = word2[i]
            merged_word += word1_c + word2_c
            i += 1

        # Add on any excess chars
        merged_word += word1[min_word_len::]
        merged_word += word2[min_word_len::]

        return merged_word
