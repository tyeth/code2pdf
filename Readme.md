# Code to PDF Converter

The Code to PDF Converter is a command-line tool that allows you to convert C# or any text files into PDF format. It provides the ability to combine multiple code files into a single PDF, preserving the structure and formatting of the code.

## Features

- Convert C# or text files into PDF format.
- Support for converting files in nested folders.
- Retains code structure and formatting in the generated PDF.
- Easy-to-use command-line interface.

## Requirements

To use the Code to PDF Converter, ensure you have the following installed:

- Python 3.x
- PyPDF2 library
- reportlab library

## Usage

1. Clone the repository or download the project files.

2. Open a command-line interface and navigate to the project directory.

3. Install the required Python libraries if not already installed:
`pip install PyPDF2 reportlab`

4. Run the converter using the following command:
```
python code2pdf.py [-p PATTERN [PATTERN ...]] [-o OUTPUT]

- `-p PATTERN [PATTERN ...]`: Glob pattern(s) to match code files. The default pattern is `*.cs`. You can specify multiple patterns to include different file types, and globbing is supported for recursive searching, e.g. **\*.cs
- `-o OUTPUT`: Output PDF file path and name. The default is `combined_code.pdf`.
```

**Example:**
`python code2pdf.py -p "**\*.cs" -o my_code.pdf`

5. The converter will scan the provided code file(s) and generate a PDF containing the converted code.

## Notes

- Ensure that the code files are properly formatted and have the correct file extension.
- The converter will preserve the structure and formatting of the code. However, it's recommended to review the generated PDF to ensure the desired output.
- Content will overflow the width of pages, this is acceptable to me as the content is for ingestion by machine.