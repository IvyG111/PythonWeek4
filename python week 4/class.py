def read_and_modify_file():
    try:
        # Ask the user for the input file name
        input_file_name = input("Enter the name of the file to read: ")

        # Attempt to open the file for reading
        with open(input_file_name, "r") as input_file:
            content = input_file.read()

        # Modify the content (e.g., convert to uppercase for this example)
        modified_content = content.upper()

        # Ask the user for the output file name
        output_file_name = input("Enter the name of the file to write the modified content to: ")

        # Write the modified content to the new file
        with open(output_file_name, "w") as output_file:
            output_file.write(modified_content)

        print(f"Modified content has been written to {output_file_name}.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: The file could not be read. Please check permissions or file integrity.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
