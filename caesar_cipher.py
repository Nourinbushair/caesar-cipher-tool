def caesar_cipher(text, shift, mode):

    result = ""

    # Decrypt mode
    if mode == "decrypt":
        shift = -shift

    for char in text:

        # Uppercase letters
        if char.isupper():

            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Lowercase letters
        elif char.islower():

            result += chr((ord(char) + shift - 97) % 26 + 97)

        else:
            result += char

    return result


print("=" * 55)
print("        Caesar Cipher Encryption Tool")
print("=" * 55)

mode = input("Choose mode (encrypt/decrypt): ").lower()

message = input("Enter message: ")

shift = int(input("Enter shift value: "))

output = caesar_cipher(message, shift, mode)

print(f"\nResult: {output}")