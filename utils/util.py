import io
from PIL import Image
import pdfplumber

class Utils:

    def read_text_from_file(self, filename):
        file_extension = filename.split(".")[-1]
        match(file_extension):
            case "txt":
                return self.read_from_txt(filename)
            case "pdf":
                return self.read_from_pdf(filename)

    def retrieved_rag_data(self, results):
        data = []
        for index, row in results[0].iterrows():
            if row.iloc[2] == 'image':
                image = Image.open(row.iloc[1])
                #TODO: Figure out how to send images as well in the prompt later.
                image.show()
            elif row.iloc[2] == 'text':
                text = row.iloc[1]
                data.append(text)
        return data

    def read_from_txt(self, filename):
        try:
            # Open the file in read mode ('r')
            with open(filename, 'r') as file:
                # Read the contents of the file into a string
                text = file.read()
                file.close()
            return text
        except IOError as e:
            # Handle any I/O errors
            print(f"An error occurred: {e}")
            return None

    def read_from_pdf(self, filename):
        try:
            text = ""
            with pdfplumber.open(filename) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() + "\n"
            return text
        
        except Exception as e:
            print(f"An error has occured: {e}")
            return None