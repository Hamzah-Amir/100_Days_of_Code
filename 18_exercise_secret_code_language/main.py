try:
    def encode():
        message = input("Enter your message: ").upper()
        
        if len(message) > 3:
            encoded_message = message.split()
            encoded_words = []
            for word in encoded_message:
                encoded_word = word[1:] + word[0]
                encoded_word = 'uon' + encoded_word
                encoded_word = encoded_word + "acs"
                encoded_words.append(encoded_word)
            return ' '.join(encoded_words)
        else:
            encoded_message = message
            return encoded_message[::-1]
except Exception as e:
    print("An error occurred during encoding:", e)

try:
    def decode():
        encoded_message = input("Enter your encoded message: ").upper()
        encoded_message = encoded_message.split()
        decoded_words = []
        for word in encoded_message:
            if len(word) > 3:
                decoded_word = word[3:-3]
                decoded_word = decoded_word[-1] + decoded_word[:-1]
                decoded_words.append(decoded_word)
            else:
                decoded_message = encoded_message
                decoded_message = " ".join(encoded_message[::-1])
                return decoded_message[::-1]
        return ' '.join(decoded_words)
except Exception as e:
    print("An error occurred during decoding:", e)

choice = input("Do you want to encode or decode a message or quit the program? (e/d/quit): ").lower()
try:
    while choice  !='quit':
        if choice == 'e':
            print("Encoded message:", encode())
            
        elif choice == 'd':
            print("Decoded message:", decode())
        else:
            print("Invalid choice. Please enter 'e' to encode or 'd' to decode or quit to end the program.")
        choice = input("Do you want to encode or decode a message or quit the program? (e/d/quit): ").lower()
    print("Thank you for using the secret code language program!")
except Exception as e:
    print("An error occurred:", e)