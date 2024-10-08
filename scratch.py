import matplotlib.pyplot as plt

accuracies = [0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.00]
plt.figure(figsize=(8,6))
plt.plot(range(1, 11), accuracies, marker='o')
plt.title('Accuracy vs Number of Known People')
plt.xlabel('Number of Known People')
plt.ylabel('Accuracy')
plt.grid(True)
plt.show()