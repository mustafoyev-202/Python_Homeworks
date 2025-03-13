import numpy as np
from PIL import Image


# Task 1: Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5.0 / 9.0


temperatures = np.array([32, 68, 100, 212, 77])
vectorized_fahrenheit_to_celsius = np.vectorize(fahrenheit_to_celsius)
celsius_temperatures = vectorized_fahrenheit_to_celsius(temperatures)
print("Celsius temperatures:", celsius_temperatures)


# Task 2: Custom function to calculate power
def power_function(base, exponent):
    return base**exponent


bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
vectorized_power_function = np.vectorize(power_function)
powers = vectorized_power_function(bases, exponents)
print("Powers:", powers)

# Task 3: Solve the system of equations
A = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
B = np.array([7, 4, 5])
solution = np.linalg.solve(A, B)
print("Solution to the system of equations:", solution)

# Task 4: Solve the electrical circuit equations
A_circuit = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
B_circuit = np.array([12, -5, 15])
currents = np.linalg.solve(A_circuit, B_circuit)
print("Currents in the branches:", currents)


# Image Manipulation with NumPy and PIL
def flip_image(image_array):
    return np.flipud(np.fliplr(image_array))


def add_noise(image_array):
    noise = np.random.randint(0, 50, image_array.shape, dtype="uint8")
    return np.clip(image_array + noise, 0, 255)


def brighten_channels(image_array, value=40):
    return np.clip(image_array + value, 0, 255)


def apply_mask(image_array):
    h, w, _ = image_array.shape
    mask_size = 100
    start_h = (h - mask_size) // 2
    start_w = (w - mask_size) // 2
    image_array[start_h : start_h + mask_size, start_w : start_w + mask_size] = [
        0,
        0,
        0,
    ]
    return image_array


# Read the image
image = Image.open("lesson-14\homework\image.png")
image_array = np.array(image)

# Apply manipulations
flipped_image = flip_image(image_array)
noisy_image = add_noise(image_array)
brightened_image = brighten_channels(image_array)
masked_image = apply_mask(image_array)

# Convert numpy array to image and save
Image.fromarray(flipped_image).save("birds_flipped.png")
Image.fromarray(noisy_image).save("birds_noisy.png")
Image.fromarray(brightened_image).save("birds_brightened.png")
Image.fromarray(masked_image).save("birds_masked.png")
