#################
# USAGE EXAMPLE #
#################
# 1. read image as numpy array
image_np = plt.imread('cup.jpg')

# 2. resize image to 300, 300 
image_np = cv2.resize(image_np, dsize=(300, 300), interpolation=cv2.INTER_CUBIC)

# 3. reshape the image into (1, n, m, l) from (n, m, l)
image_np = image_np.reshape(1, image_np.shape[0],image_np.shape[1], image_np.shape[2])

# 4. normalize the image
image_np = image_np / 255.0;

# 5. load the neural network (should be called only once at first when the program is running)
model = load_model()

# call predict on the image. This will return a string that should be displayed on the screen
predict(model, image_np)

