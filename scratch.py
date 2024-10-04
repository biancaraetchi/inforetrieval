import matplotlib.pyplot as plt

accuracies = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
plt.figure(figsize=(8,6))
plt.plot(range(1, 11), accuracies, marker='o')
plt.title('Accuracy vs Number of Known People')
plt.xlabel('Number of Known People')
plt.ylabel('Accuracy')
plt.grid(True)
plt.show()