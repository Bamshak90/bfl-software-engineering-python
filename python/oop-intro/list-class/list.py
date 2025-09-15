class MyList():
  def __init__(self):
    self.data = []

  def append(self, item):
    self.data.append(item)

  def remove(self, item):
    self.data.remove(item)

  def __getitem__(self, index):
    return self.data[index]

  def __setitem__(self, index, value):
    self.data[index] = value

  def __len__(self):
    return len(self.data)
  
  def __iter__(self):
    return iter(self.data)
  
  def __str__(self):
    return str(self.data)
  


nums = MyList()
nums.append(5)
nums.append(15)
nums.append(25)

nums.remove(25)
print(nums)         
print(nums[1])      
nums[1] = 100
print(nums)         
print(len(nums))  

for n in nums:
    print(n)
