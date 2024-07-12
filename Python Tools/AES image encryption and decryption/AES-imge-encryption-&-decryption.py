from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os
from PIL import Image
import io

# Function to encrypt an image
def encrypt_image(input_file, output_file, password):
    # Generate a key and nonce from the password using scrypt
    salt = get_random_bytes(16)
    key = scrypt(password, salt, 32, N=2**14, r=8, p=1)
    nonce = get_random_bytes(16)

    # Initialize AES cipher in GCM mode
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

    # Read the input image
    with open(input_file, 'rb') as f:
        image_data = f.read()

    # Encrypt the image data
    ciphertext, tag = cipher.encrypt_and_digest(image_data)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Write salt, nonce, tag, and ciphertext to the output file
    with open(output_file, 'wb') as f:
        f.write(salt)
        f.write(nonce)
        f.write(tag)
        f.write(ciphertext)

    print(f'Encryption successful. Encrypted image saved at: {output_file}')

# Function to decrypt an image
def decrypt_image(input_file, output_file, password):
    try:
        # Read salt, nonce, tag, and ciphertext from the input file
        with open(input_file, 'rb') as f:
            salt = f.read(16)
            nonce = f.read(16)
            tag = f.read(16)
            ciphertext = f.read()

        # Generate key from password and salt using scrypt
        key = scrypt(password, salt, 32, N=2**14, r=8, p=1)

        # Initialize AES cipher in GCM mode
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

        # Decrypt the ciphertext
        decrypted_data = cipher.decrypt_and_verify(ciphertext, tag)

        # Create an image from decrypted data
        decrypted_image = Image.open(io.BytesIO(decrypted_data))

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Save the decrypted image with a valid image extension
        decrypted_image.save(output_file)

        print(f'Decryption successful. Decrypted image saved at: {output_file}')

    except ValueError:
        print("Decryption failed. The provided key is incorrect. Please try again with the correct key.")

# Function to get user input for operation (encryption or decryption)
def get_operation_choice():
    while True:
        choice = input("Enter 'E' for encryption or 'D' for decryption: ").strip().upper()
        if choice == 'E' or choice == 'D':
            return choice
        else:
            print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

# Function to get user input for image file path
def get_image_path():
    while True:
        image_path = input("Enter the full path of the image file: ").strip()
        if os.path.isfile(image_path):
            return image_path
        else:
            print(f"File not found at '{image_path}'. Please enter a valid image file path.")

# Main function
if __name__ == '__main__':
    # Get operation choice (encryption or decryption)
    operation = get_operation_choice()

    # Get image file path
    image_path = get_image_path()

    # Determine output file paths
    file_directory = os.path.dirname(image_path)
    image_filename = os.path.basename(image_path)
    image_name, image_extension = os.path.splitext(image_filename)

    if operation == 'E':
        output_file = os.path.join(file_directory, image_name + '_encrypted.enc')
    elif operation == 'D':
        output_file = os.path.join(file_directory, image_name + '_decrypted.png')

    # Get password
    password = input("Enter password (must be at least 16 characters long): ").encode('utf-8')  # Convert to bytes

    # Perform chosen operation
    if operation == 'E':
        encrypt_image(image_path, output_file, password)
    elif operation == 'D':
        decrypt_image(image_path, output_file, password)
