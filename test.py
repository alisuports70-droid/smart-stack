from stack import SmartStack

s = SmartStack()
s.push(5); s.push(10); s.push(3)
print(f"Sum: {s.get_sum()}, Max: {s.get_max()}, Min: {s.get_min()}")