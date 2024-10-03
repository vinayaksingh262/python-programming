from PIL import Image
import imagehash
import cv2

def dhash(image_path, hash_size=8):
    # Open the image, convert it to grayscale, and resize it
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hash_size + 1, hash_size))

    # Compute the (relative) horizontal gradient between adjacent pixels
    diff = resized[:, 1:] > resized[:, :-1]

    # Convert the difference to a hash
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

def image_similarity(hash1, hash2):
    # Compute the Hamming distance between two hashes
    return bin(hash1 ^ hash2).count('1')

def detect_image_forgery(original_path, manipulated_path, threshold=5):
    # Calculate hash for the original and manipulated images
    original_hash = dhash(original_path)
    manipulated_hash = dhash(manipulated_path)

    # Compare the similarity of the hashes
    similarity = image_similarity(original_hash, manipulated_hash)

    # Check if the similarity is below the threshold
    if similarity == threshold:
        print("Image are Same...")
    else:
        print("Images are likely different.")

# Example usage
original_image_path = r'C:\\Users\DELL\\Downloads\\instagram-image-size - Copy.jpg'
manipulated_image_path = r'C:\\Users\DELL\\Downloads\\instagram-image-size - Copy.jpg'
detect_image_forgery(original_image_path, manipulated_image_path)
