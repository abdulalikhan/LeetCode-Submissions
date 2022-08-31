class SnapshotArray:
    
    def __init__(self, length: int):
        self.snap_id = 0
        self.snapshots = {0: defaultdict(int)}
        

    def set(self, index: int, val: int) -> None:
        self.snapshots[self.snap_id][index] = val

    def snap(self) -> int:
        self.snap_id += 1
        self.snapshots[self.snap_id] = defaultdict(int)
        for index, val in self.snapshots[self.snap_id-1].items():
            self.snapshots[self.snap_id][index] = val
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshots[snap_id][index]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)