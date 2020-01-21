class TrieNode:
    """docstring for Trie"""
    def __init__(self, val):
        self.val = val
        self.children={}
        self.word_list= []

    def add_child(self, node, key):
        self.children[key] = node

class Solution:
    def __init__(self):
        self.trieroot = None

    def insert_in_trie(self, word, root):
        for i in range(len(word)):
            if word[i] in root.children:
                root.word_list.append(word)
                root = root.children[word[i]]
            else:
                # print(word[i])
                root.children[word[i]]= TrieNode(word[:i+1])
                root.word_list.append(word)
                root = root.children[word[i]]
        root.word_list.append(word)
    def build_trie(self, words):
        self.trieroot = TrieNode("")
        for word in words:
            self.insert_in_trie(word.lower(), self.trieroot)

    def search_word(self, query):
        root = self.trieroot
        sugg = []
        self.trieroot
        for i in range(len(query)):
            if query[i] in root.children:
                root = root.children[query[i]]
                sugg = root.word_list
            else:
                sugg = []
        sugg.sort()
        return sugg[:3]
    def return_results(self,query):
        res = []
        for i in range(2,len(query)+1):
            res.append(s.search_word(query[:i]))
        return res
    def test_trie(self):
        # trie = Trie()
        products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
        self.build_trie(products)
        query = "mouse"
        expected = [["mobile", "moneypot", "monitor"], ["mouse", "mousepad"], ["mouse", "mousepad"], ["mouse", "mousepad"]]
        if self.return_results(query)==expected:
        # print(self.return_results(query))
            print("Done")

        products = ["ps4", "ps4 slim", "ps4 pro", "xbox", "tissue",
                    "standing table", "house", "true love", "tracking device"]
        self.build_trie(products)
        query = "ps4"
        expected = [["ps4", "ps4 pro", "ps4 slim"], ["ps4", "ps4 pro", "ps4 slim"]]
        if self.return_results(query)==expected:
        # print(self.return_results(query))
            print("Done")


        products = ["tracking device", "true love"]
        self.build_trie(products)
        query = "tru"
        expected = [["tracking device", "true love"], ["true love"]]
        if self.return_results(query)==expected:
        # print(self.return_results(query))
            print("Done")

if __name__ == '__main__':
    s = Solution()
    words = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    s.build_trie(words)
    query = "mouse"
    
    for i in range(2,len(query)+1):
        print(s.search_word(query[:i]))
    s.test_trie()

                




# class Trie:
#     def __init__(self):

