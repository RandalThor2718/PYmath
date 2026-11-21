import matplotlib.pyplot as plt

seed = int(input("seed"))

def collatz(seed):
  sequence = [seed]
  while seed != 1:
    if seed % 2 == 0:
      seed = seed // 2
    else:
      seed = 3 * seed + 1
    sequence.append(seed)
  return sequence

sequence = collatz(seed)
print(sequence)

plt.figure(figsize=(10, 6))
plt.plot(sequence, marker='o', linestyle='-')
plt.xlabel('Step')
plt.ylabel('Value')
plt.grid(True)
plt.xticks(range(len(sequence)))
plt.show()
