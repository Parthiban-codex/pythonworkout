class binarysearch():
    def BS(self):
        array = input().split()
        target = input()
        array.sort()
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = (low + high) // 2
            if array[mid] == target:
                return f"Found {target},position {mid}"
            elif array[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        print("not found")
        
        
        
        
obj = binarysearch()
print(obj.BS())