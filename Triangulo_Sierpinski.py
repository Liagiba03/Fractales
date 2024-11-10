import matplotlib.pyplot as plt

def sierpinski(x, y, length, depth):
    if depth == 0:
        # Dibujar un triángulo
        plt.fill([x, x + length/2, x - length/2],
                 [y, y + (length * np.sqrt(3)) / 2, y + (length * np.sqrt(3)) / 2], 'k')
    else:
        # Recursión
        sierpinski(x, y, length/2, depth-1)
        sierpinski(x - length/4, y + (length * np.sqrt(3)) / 4, length/2, depth-1)
        sierpinski(x + length/4, y + (length * np.sqrt(3)) / 4, length/2, depth-1)

plt.figure(figsize=(8, 8))
sierpinski(0, 0, 4, 5)
plt.axis("equal")
plt.axis("off")
plt.title("Triángulo de Sierpinski")
plt.show()
