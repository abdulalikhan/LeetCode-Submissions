#User function Template for python3
class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word_end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode("")        

    def insert(self, word: str) -> None:
        temp = self.root
        for char in word:
            if char in temp.children:
                temp = temp.children[char]
            else:
                new_node = TrieNode(char)
                temp.children[char] = new_node
                temp = new_node
        temp.word_end = True

    def search(self, word: str) -> bool:
        temp = self.root
        for char in word:
            if char in temp.children:
                temp = temp.children[char]
            else:
                return False
        if temp.word_end:
            return True
        else:
            return False

    def dfs(self, node: TrieNode, prefix: str) -> None:
        if node.word_end:
            self.output.append(prefix + node.char)
        for child in node.children.values():
            self.dfs(child, prefix + node.char)

    def startsWith(self, prefix: str):
        temp = self.root
        self.output = []
        for char in prefix:
            if char in temp.children:
                temp = temp.children[char]
            else:
                return []
        self.dfs(temp, prefix[:-1])
        return sorted(self.output)
        
class Solution:
    def displayContacts(self, n, contact, s):
        trie = Trie()
        for entry in contact:
            trie.insert(entry)
        ans = []
        query = ""
        for i in range(len(s)):
            query += s[i]
            this_ans = trie.startsWith(query)
            if len(this_ans) == 0:
                ans.append([0])
            else:
                ans.append(this_ans)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
# } Driver Code Ends