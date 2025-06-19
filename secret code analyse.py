def encode(word):
    if len(word) > 3:
        word=word[1:]+word[0]
        word="huk"+word+"kkt"
    else:
        word=word[::-1]
    return word
def decode(word):
    if len(word)<3:
        word=word[::-1]
    else:
        word=word[3:-3]
        word=word[-1]+word[ :-1]
    return word

def main():
    choice=input("Hi Welcome to Nextgen Encryption.Please let us know if you want to encode or decode your text : ").strip().lower()
    message=input("Please enter your text: ")
    words=message.split()
    if choice=="encode":
        result=[encode(word) for word in words]
    elif choice=="decode":
        result=[decode(word) for word in words]
    else:
        print("Invalid choice. Please enter 'encode' or 'decode'.")
        return
    print(" ".join(result))

main()
# This code is a simple text encoding and decoding program.

