import numpy as np
import matplotlib.pyplot as plt

# Configuración del conjunto de Mandelbrot
width, height = 800, 800
x_min, x_max = -2, 1
y_min, y_max = -1.5, 1.5
max_iter = 100

# Generar la imagen del fractal
image = np.zeros((height, width))
for x in range(width):
    for y in range(height):
        c = complex(x_min + (x / width) * (x_max - x_min),
                    y_min + (y / height) * (y_max - y_min))
        z = 0
        iter_count = 0
        while abs(z) <= 2 and iter_count < max_iter:
            z = z*z + c
            iter_count += 1
        image[y, x] = iter_count

# Mostrar el fractal
plt.imshow(image, cmap='inferno', extent=(x_min, x_max, y_min, y_max))
plt.colorbar()
plt.title("Conjunto de Mandelbrot")
plt.show()
