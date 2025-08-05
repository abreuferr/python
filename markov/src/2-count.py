def count_vowels_and_consonants(text):
    """
    Count the number of vowels and consonants in the given text.
    Returns a tuple (vowel_count, consonant_count).
    """
    # Define vowels (both lowercase and uppercase)
    vowels = set("aeiouàáâãéêíóôõúAEIOUÀÁÂÃÉÊÍÓÔÕÚ")

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
        with open(filename, "r", encoding="utf-8") as file:
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
    Returns the formatted text for saving to file.
    """
    output_lines = []

    separator1 = "=" * 50
    header = "VOWEL AND CONSONANT COUNT RESULTS"
    separator2 = "=" * 50
    vowel_line = f"Vowels:     {vowel_count:,}"
    consonant_line = f"Consonants: {consonant_count:,}"
    dash_separator = "-" * 30
    total_line = f"Total letters: {total_chars:,}"
    separator3 = "=" * 50

    print(separator1)
    print(header)
    print(separator2)
    print(vowel_line)
    print(consonant_line)
    print(dash_separator)
    print(total_line)
    print(separator3)

    output_lines.extend(
        [
            separator1,
            header,
            separator2,
            vowel_line,
            consonant_line,
            dash_separator,
            total_line,
            separator3,
        ]
    )

    # Calculate percentages if there are letters
    if total_chars > 0:
        vowel_percentage = (vowel_count / total_chars) * 100
        consonant_percentage = (consonant_count / total_chars) * 100

        percentage_header = "PERCENTAGE BREAKDOWN:"
        vowel_perc_line = f"Vowels:     {vowel_percentage:.2f}%"
        consonant_perc_line = f"Consonants: {consonant_percentage:.2f}%"
        final_separator = "=" * 50

        print(percentage_header)
        print(vowel_perc_line)
        print(consonant_perc_line)
        print(final_separator)

        output_lines.extend(
            [percentage_header, vowel_perc_line, consonant_perc_line, final_separator]
        )

    return "\n".join(output_lines)


def save_results_to_file(content, output_filename):
    """
    Save the analysis results to a file.
    """
    try:
        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"\nResults saved to: {output_filename}")
        return True
    except Exception as e:
        print(f"\nError saving results to file: {str(e)}")
        return False


def main():
    """
    Main function to execute the vowel and consonant counting.
    """
    filename = "normalization_result.txt"
    output_filename = "count_result.txt"

    print("Starting vowel and consonant count...")
    print(f"Reading from file: {filename}")
    print(f"Output will be saved to: {output_filename}")
    print("-" * 50)

    # Read the content from normalization_result.txt
    content = read_result_file(filename)

    if content is None:
        return

    if not content.strip():
        print("The file is empty or contains no text.")
        return

    # Count vowels and consonants
    vowel_count, consonant_count = count_vowels_and_consonants(content)
    total_letters = vowel_count + consonant_count

    # Display the results and collect output for saving
    results_output = display_results(vowel_count, consonant_count, total_letters)

    # Additional information
    file_size_line = f"File size: {len(content):,} characters (including non-letters)"
    letters_processed_line = f"Letters processed: {total_letters:,}"

    print(file_size_line)
    print(letters_processed_line)

    # Combine all output content
    additional_info = f"\n{file_size_line}\n{letters_processed_line}"
    final_output = results_output + additional_info

    # Save results to file
    save_results_to_file(final_output, output_filename)


if __name__ == "__main__":
    main()
