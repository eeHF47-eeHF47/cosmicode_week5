# Implement a class to handle basic file operations (reading, writing, appending) for text files.
class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, content):
        """Write content to a file, overwriting any existing content."""
        with open(self.file_name, 'w') as file:
            file.write(content)
        print(f"Content written to {self.file_name}")

    def append_to_file(self, content):
        """Append content to the end of the file."""
        with open(self.file_name, 'a') as file:
            file.write(content)
        print(f"Content appended to {self.file_name}")

    def read_from_file(self):
        """Read and return the entire content of the file."""
        try:
            with open(self.file_name, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return f"Error: {self.file_name} does not exist."

# Example usage:
file_manager = FileManager('example.txt')

# Writing to the file (overwrites existing content)
file_manager.write_to_file('This is the first line.\n')

# Appending to the file
file_manager.append_to_file('This is the second line.\n')
file_manager.append_to_file('This is the third line.\n')

# Reading from the file
content = file_manager.read_from_file()
print("\nFile content:")
print(content)
