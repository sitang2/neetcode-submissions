class MyHashSet:

    def __init__(self):
        self.myHashset = [] 

    def add(self, key: int) -> None:
        if key not in self.myHashset:
            self.myHashset.append(key)

    def remove(self, key: int) -> None:
        if key in self.myHashset:
            self.myHashset.remove(key)

    def contains(self, key: int) -> bool:
        for e in self.myHashset:
            if key == e:
                return True

        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)