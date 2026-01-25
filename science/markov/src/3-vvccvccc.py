def is_vowel(char):
    """
    Check if a character is a vowel.
    Returns True for vowels, False for consonants.
    """
    vowels = set("aeiouàáâãéêíóôõúAEIOUÀÁÂÃÉÊÍÓÔÕÚ")
    return char in vowels


def analyze_two_character_sequences(text):
    """
    Analyze sequences of two consecutive letters in the text.
    Returns a dictionary with counts for each type of sequence.
    """
    # Initialize counters
    vowel_vowel = 0
    vowel_consonant = 0
    consonant_vowel = 0
    consonant_consonant = 0

    # Process the text character by character
    for i in range(len(text) - 1):
        char1 = text[i]
        char2 = text[i + 1]

        # Only analyze if both characters are letters
        if char1.isalpha() and char2.isalpha():
            first_is_vowel = is_vowel(char1)
            second_is_vowel = is_vowel(char2)

            # Classify the sequence
            if first_is_vowel and second_is_vowel:
                vowel_vowel += 1
            elif first_is_vowel and not second_is_vowel:
                vowel_consonant += 1
            elif not first_is_vowel and second_is_vowel:
                consonant_vowel += 1
            else:  # not first_is_vowel and not second_is_vowel
                consonant_consonant += 1

    return {
        "vowel_vowel": vowel_vowel,
        "vowel_consonant": vowel_consonant,
        "consonant_vowel": consonant_vowel,
        "consonant_consonant": consonant_consonant,
    }


def read_result_file(filename):
    """
    Read the content from the normalization_result.txt file.
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


def display_sequence_results(results):
    """
    Display the sequence analysis results in a formatted way.
    Returns the formatted text for saving to file.
    """
    output_lines = []

    print("=" * 60)
    output_lines.append("=" * 60)
    print("TWO-CHARACTER SEQUENCE ANALYSIS RESULTS")
    output_lines.append("TWO-CHARACTER SEQUENCE ANALYSIS RESULTS")
    print("=" * 60)
    output_lines.append("=" * 60)

    # Calculate total sequences
    total_sequences = sum(results.values())

    if total_sequences == 0:
        message = "No two-character sequences found in the file."
        print(message)
        output_lines.append(message)
        return "\n".join(output_lines)

    # Display counts
    line1 = f"Vowel + Vowel:         {results['vowel_vowel']:,}"
    line2 = f"Vowel + Consonant:     {results['vowel_consonant']:,}"
    line3 = f"Consonant + Vowel:     {results['consonant_vowel']:,}"
    line4 = f"Consonant + Consonant: {results['consonant_consonant']:,}"
    separator = "-" * 40
    total_line = f"Total sequences:       {total_sequences:,}"

    print(line1)
    print(line2)
    print(line3)
    print(line4)
    print(separator)
    print(total_line)
    print("=" * 60)

    output_lines.extend([line1, line2, line3, line4, separator, total_line, "=" * 60])

    # Display percentages
    header = "PERCENTAGE BREAKDOWN:"
    perc1 = (
        f"Vowel + Vowel:         {(results['vowel_vowel']/total_sequences)*100:.2f}%"
    )
    perc2 = f"Vowel + Consonant:     {(results['vowel_consonant']/total_sequences)*100:.2f}%"
    perc3 = f"Consonant + Vowel:     {(results['consonant_vowel']/total_sequences)*100:.2f}%"
    perc4 = f"Consonant + Consonant: {(results['consonant_consonant']/total_sequences)*100:.2f}%"
    final_separator = "=" * 60

    print(header)
    print(perc1)
    print(perc2)
    print(perc3)
    print(perc4)
    print(final_separator)

    output_lines.extend([header, perc1, perc2, perc3, perc4, final_separator])

    return "\n".join(output_lines)


def find_sample_sequences(text, sequence_type, max_samples=5):
    """
    Find sample sequences of the specified type for demonstration.
    Returns a list of sample sequences.
    """
    samples = []
    vowels = set("aeiouAEIOU")

    for i in range(len(text) - 1):
        if len(samples) >= max_samples:
            break

        char1 = text[i]
        char2 = text[i + 1]

        if char1.isalpha() and char2.isalpha():
            first_is_vowel = char1 in vowels
            second_is_vowel = char2 in vowels

            sequence_matches = False
            if sequence_type == "vowel_vowel" and first_is_vowel and second_is_vowel:
                sequence_matches = True
            elif (
                sequence_type == "vowel_consonant"
                and first_is_vowel
                and not second_is_vowel
            ):
                sequence_matches = True
            elif (
                sequence_type == "consonant_vowel"
                and not first_is_vowel
                and second_is_vowel
            ):
                sequence_matches = True
            elif (
                sequence_type == "consonant_consonant"
                and not first_is_vowel
                and not second_is_vowel
            ):
                sequence_matches = True

            if sequence_matches:
                samples.append(char1 + char2)

    return samples


def display_sample_sequences(text, results):
    """
    Display sample sequences for each category.
    Returns the formatted text for saving to file.
    """
    output_lines = []

    header = "SAMPLE SEQUENCES:"
    separator = "-" * 40

    print(header)
    print(separator)
    output_lines.extend([header, separator])

    sequence_types = [
        ("vowel_vowel", "Vowel + Vowel"),
        ("vowel_consonant", "Vowel + Consonant"),
        ("consonant_vowel", "Consonant + Vowel"),
        ("consonant_consonant", "Consonant + Consonant"),
    ]

    for seq_type, description in sequence_types:
        if results[seq_type] > 0:
            samples = find_sample_sequences(text, seq_type)
            if samples:
                line = f"{description}: {', '.join(samples[:5])}"
            else:
                line = f"{description}: (no samples found)"
        else:
            line = f"{description}: (none found)"

        print(line)
        output_lines.append(line)

    final_separator = "=" * 60
    print(final_separator)
    output_lines.append(final_separator)

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
    Main function to execute the two-character sequence analysis.
    """
    filename = "normalization_result.txt"
    output_filename = "vvccvccc_result.txt"

    print("Starting two-character sequence analysis...")
    print(f"Reading from file: {filename}")
    print(f"Output will be saved to: {output_filename}")
    print("-" * 60)

    # Read the content from normalization_result.txt
    content = read_result_file(filename)

    if content is None:
        return

    if not content.strip():
        print("The file is empty or contains no text.")
        return

    # Analyze two-character sequences
    results = analyze_two_character_sequences(content)

    # Display and collect the results for saving
    output_content = []

    # Display the results and collect output
    results_output = display_sequence_results(results)
    output_content.append(results_output)

    # Display sample sequences and collect output
    samples_output = display_sample_sequences(content, results)
    output_content.append(samples_output)

    # Additional file information
    total_chars = len(content)
    letter_count = sum(1 for char in content if char.isalpha())
    possible_sequences = max(0, letter_count - 1)

    stats_lines = [
        f"File statistics:",
        f"  Total characters: {total_chars:,}",
        f"  Total letters: {letter_count:,}",
        f"  Possible sequences: {possible_sequences:,}",
    ]

    for line in stats_lines:
        print(line)

    output_content.append("\n".join(stats_lines))

    # Combine all output content
    final_output = "\n".join(output_content)

    # Save results to file
    save_results_to_file(final_output, output_filename)
    """
    Main function to execute the two-character sequence analysis.
    """
    filename = "normalization_result.txt"

    print("Starting two-character sequence analysis...")
    print(f"Reading from file: {filename}")
    print("-" * 60)

    # Read the content from normalization_result.txt
    content = read_result_file(filename)

    if content is None:
        return

    if not content.strip():
        print("The file is empty or contains no text.")
        return

    # Analyze two-character sequences
    results = analyze_two_character_sequences(content)

    # Display the results
    display_sequence_results(results)

    # Display sample sequences
    display_sample_sequences(content, results)

    # Additional file information
    total_chars = len(content)
    letter_count = sum(1 for char in content if char.isalpha())
    print(f"File statistics:")
    print(f"  Total characters: {total_chars:,}")
    print(f"  Total letters: {letter_count:,}")
    print(f"  Possible sequences: {max(0, letter_count - 1):,}")


if __name__ == "__main__":
    main()
