import os
from docx import Document

class FileHandler:
    """
    Handles reading text files into a string to be sent to the openAI API
    """
    def __init__(self, input_dir="input", output_dir="output"):
        self.input_dir = input_dir
        self.output_dir = output_dir

        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def find_docx_files(self):
        """
        Finds the first .docx file in the input directory.
        Returns the filename or None if no .docx files are found.
        """
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".docx"):
                return filename
            return None

    def read_file(self):
        """
        Reads a docx text file to a string to be sent to the openAI API
        """
        file_name = self.find_docx_files()
        if file_name is None:
            print("Error: No .docx file found in the input directory.")
            return None

        filepath = os.path.join(self.input_dir, file_name)
        try:
            doc = Document(filepath)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text.strip()
        except FileNotFoundError:
            print(f"Error: File {file_name} not found.")
            return None
        except Exception as e:
            print(f"Error reading document {file_name}: {e}")
            return None
