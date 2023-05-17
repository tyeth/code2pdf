import argparse
import glob
import os
from PyPDF2 import PdfMerger, PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import logging
import io

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create a logger for the script
logger = logging.getLogger(__name__)

def add_file_to_pdf(merger, file_path):
    logger.debug(f"Processing file: {file_path}")

    with open(file_path, 'r', encoding='utf-8-sig') as file:
        text_content = file.read()

    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont('Courier', 10)

    lines = text_content.split('\n')

    line_height = 12  # Adjust the line height if needed
    margin = 10  # Adjust the margin if needed

    # Calculate the available height for the content on each page
    available_height = letter[1] - 2 * margin

    y = letter[1] - margin

    # Add file header with separator
    file_header = f"File: {os.path.relpath(file_path)}"
    separator = "=" * (len(file_header) + 4)
    can.drawString(margin, y - line_height, separator)
    can.drawString(margin, y - 2 * line_height, f"// {file_header}")
    y -= 3 * line_height

    line_number = 1
    for line in lines:
        if y - line_height < margin + 3 * line_height:
            # If there is not enough space on the current page, add a new page
            can.showPage()
            y = letter[1] - margin
            can.setFont('Courier', 10)
            can.drawString(margin, y - line_height, separator)
            can.drawString(margin, y - 2 * line_height, f"// {file_header}")
            y -= 3 * line_height

        # Add line number with colon
        line_with_number = f"{line_number:4d}: {line}"
        can.drawString(margin + 30, y - line_height, line_with_number)  # Adjust the position and style of the text if needed
        y -= line_height
        line_number += 1

    can.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)

    merger.append(new_pdf)


def convert_code_to_pdf(code_files, output_path):
    merger = PdfMerger()
    for code_file in code_files:
        add_file_to_pdf(merger, code_file)
    merger.write(output_path)
    merger.close()

if __name__ == '__main__':
    # Create argument parser
    parser = argparse.ArgumentParser(description='Combine code files into a single PDF.')
    parser.add_argument('-p', '--pattern', nargs='+', default=['**\\*.cs'], help='Glob pattern(s) to match code files. Default is "**\\*.cs"')
    parser.add_argument('-o', '--output', default='combined_code.pdf', help='Output PDF file path and name')
    args = parser.parse_args()

    logger.debug(f"Patterns: {args.pattern}")
    # Get all matching code file paths using glob
    code_files = []
    for pattern in args.pattern:
        code_files.extend(glob.glob(pattern, recursive=True))
    logger.debug(f"Code files: {code_files}")
    convert_code_to_pdf(code_files, args.output)
