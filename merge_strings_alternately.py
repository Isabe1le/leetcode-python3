# https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_word_len = min(len(word1), len(word2))
        merged_word  = ""

        # Merge the words alternately
        for i in range(min_word_len):
            word1_c = word1[i]
            word2_c = word2[i]
            merged_word += f"{word1_c}{word2_c}"

        # Add on any excess chars
        merged_word += word1[min_word_len::]
        merged_word += word2[min_word_len::]

        return merged_word
