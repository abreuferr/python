def count_vowels_and_consonants(text):
    """
    Count the number of vowels and consonants in the given text.
    Returns a tuple (vowel_count, consonant_count).
    """
    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')
    
    vowel_count = 0
    consonant_count = 0
    
    # Iterate through each character in the text
    for char in text:
        if char.isalpha():  # Check if character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

def read_result_file(filename):
    """
    Read the content from the result.txt file.
    Returns the file content as a string.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        print("Please make sure the file exists in the same directory as this script.")
        return None
    except Exception as e:
        print(f"Error reading file '{filename}': {str(e)}")
        return None

def display_results(vowel_count, consonant_count, total_chars):
    """
    Display the counting results in a formatted way.
    """
    print("=" * 50)
    print("VOWEL AND CONSONANT COUNT RESULTS")
    print("=" * 50)
    print(f"Vowels:     {vowel_count:,}")
    print(f"Consonants: {consonant_count:,}")
    print("-" * 30)
    print(f"Total letters: {total_chars:,}")
    print("=" * 50)
    
    # Calculate percentages if there are letters
    if total_chars > 0:
        vowel_percentage = (vowel_count / total_chars) * 100
        consonant_percentage = (consonant_count / total_chars) * 100
        
        print("PERCENTAGE BREAKDOWN:")
        print(f"Vowels:     {vowel_percentage:.2f}%")
        print(f"Consonants: {consonant_percentage:.2f}%")
        print("=" * 50)

def main():
    """
    Main function to execute the vowel and consonant counting.
    """
    filename = "clean_result.txt"
    
    print("Starting vowel and consonant count...")
    print(f"Reading from file: {filename}")
    print("-" * 50)
    
    # Read the content from result.txt
    content = read_result_file(filename)
    
    if content is None:
        return
    
    if not content.strip():
        print("The file is empty or contains no text.")
        return
    
    # Count vowels and consonants
    vowel_count, consonant_count = count_vowels_and_consonants(content)
    total_letters = vowel_count + consonant_count
    
    # Display the results
    display_results(vowel_count, consonant_count, total_letters)
    
    # Additional information
    print(f"File size: {len(content):,} characters (including non-letters)")
    print(f"Letters processed: {total_letters:,}")

if __name__ == "__main__":
    main()