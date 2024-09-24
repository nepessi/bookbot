def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lowered = file_contents.lower()  # Convert the entire text to lowercase
    
    def count_words():
        words = lowered.split()  # Split words after lowering the case
        count = len(words)
        return count
    
    #print(count_words())  # Count and print the number of words

    def count_characters():
        char_count = {}
        for char in lowered:
            if char.isalpha():  # Check if the character is alphabetic
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        return char_count

    # print(count_characters())  # Print the character count dictionary
    def print_report():
        word_count = count_words()
        characters = count_characters()
        print(f"--- Begin the report of Frankenstein.txt ---")
        print("")
        print(f"{word_count} words found in the document")
        print("")
        sorted_char = sorted(characters.items(), key=lambda x: x[1], reverse=True)
        for char, count in sorted_char:
            print(f"The '{char}' character was found {count} times")
        print("")
        print("---THE END---")
    print_report()
                
main()
