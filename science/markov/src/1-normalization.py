import os


def is_vowel_or_consonant(char):
    """
    Check if a character is a vowel or consonant (letter).
    Returns True for vowels and consonants, False for other characters.
    """
    return char.isalpha()


def clean_text(text):
    """
    Remove all characters that are not vowels or consonants.
    Keeps only alphabetic characters (vowels and consonants).
    """
    # Keep only alphabetic characters (letters)
    cleaned = "".join(char for char in text if is_vowel_or_consonant(char))
    return cleaned


def process_files_in_directory(directory_path):
    """
    Read all files in the specified directory, clean their content,
    and combine the results.
    """
    combined_result = []

    # Check if directory exists
    if not os.path.exists(directory_path):
        print(f"Directory '{directory_path}' does not exist.")
        return ""

    # Get all files in the directory
    files = [
        f
        for f in os.listdir(directory_path)
        if os.path.isfile(os.path.join(directory_path, f))
    ]

    if not files:
        print(f"No files found in directory '{directory_path}'.")
        return ""

    print(f"Found {len(files)} files to process:")

    # Process each file
    for filename in files:
        file_path = os.path.join(directory_path, filename)
        print(f"Processing: {filename}")

        try:
            # Try different encodings to handle various file types
            encodings = ["utf-8", "latin-1", "cp1252"]
            content = None

            for encoding in encodings:
                try:
                    with open(file_path, "r", encoding=encoding) as file:
                        content = file.read()
                    break
                except UnicodeDecodeError:
                    continue

            if content is None:
                print(f"Warning: Could not read file '{filename}' with any encoding.")
                continue

            # Clean the content
            cleaned_content = clean_text(content)

            if cleaned_content:
                combined_result.append(cleaned_content)
                print(
                    f"  - Processed {len(content)} characters -> {len(cleaned_content)} letters"
                )
            else:
                print(f"  - No valid characters found in {filename}")

        except Exception as e:
            print(f"Error processing file '{filename}': {str(e)}")

    return "".join(combined_result)


def main():
    """
    Main function to execute the text processing workflow.
    """
    # Define the data directory path
    data_directory = "data"
    output_file = (
        "normalization_result.txt"  # Save in the same directory as the Python script
    )

    print("Starting text processing...")
    print(f"Source directory: {data_directory}")
    print(f"Output file: {output_file}")
    print("-" * 50)

    # Process all files in the data directory
    processed_content = process_files_in_directory(data_directory)

    if processed_content:
        try:
            # Save the result to result.txt in the same directory as the script
            # This will automatically overwrite if the file already exists
            with open(output_file, "w", encoding="utf-8") as result_file:
                result_file.write(processed_content)

            print("-" * 50)
            print(f"Processing completed successfully!")
            print(f"Result saved to: {output_file}")
            print(f"Total characters in result: {len(processed_content)}")

        except Exception as e:
            print(f"Error saving result file: {str(e)}")
    else:
        print("No content to save. Please check if files exist in the data directory.")


if __name__ == "__main__":
    main()
