class Trie:
    def __init__(self):
        self.trie={}

    def insert(self, word: str) -> None:
        node=self.trie
        for i in word:
            node=node.setdefault(i,{})
        node['end']=1

    def search(self, word: str) -> bool:
        node=self.trie
        for i in word:
            if i not in node : return 0
            node=node[i]
        return 'end' in node

    def startsWith(self, prefix: str) -> bool:
        node=self.trie
        for i in prefix:
            if i not in node : return 0
            node=node[i]
        return 1
    
    def delete(self, word: str) -> bool:
        node = self.trie
        a = []
        for i in word:
            if i not in node: return 0
            a.append([node, i])
            node=node[i]
        if len(node)-('end' in node)>0:
            return node.pop('end',0)
        node.pop('end',0)
        while a and len(a[-1][0])-('end' in a[-1][0])==1:
            node=a[-1][0]
            node.pop(a[-1][1])
            if 'end' in node: return 1
            a.pop()
        return 1