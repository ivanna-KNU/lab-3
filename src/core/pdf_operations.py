import os
from PyPDF2 import PdfReader, PdfWriter

class PDFOperations:
    def merge_pdfs(self, input_files, output_file):
        merger = PdfWriter()
        for pdf in input_files:
            merger.append(pdf)
        with open(output_file, 'wb') as output:
            merger.write(output)

    def split_pdf(self, input_file, output_dir):
        reader = PdfReader(input_file)
        for page_num in range(len(reader.pages)):
            writer = PdfWriter()
            writer.add_page(reader.pages[page_num])
            output_file = os.path.join(output_dir, f'page_{page_num + 1}.pdf')
            with open(output_file, 'wb') as output:
                writer.write(output)

    def rotate_pdf(self, input_file, output_file):
        reader = PdfReader(input_file)
        writer = PdfWriter()
        for page in reader.pages:
            page.rotate(90)
            writer.add_page(page)
        with open(output_file, 'wb') as output:
            writer.write(output)

    def extract_text(self, input_file, output_file):
        reader = PdfReader(input_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(text)

    def add_watermark(self, input_file, watermark_file, output_file):
        reader = PdfReader(input_file)
        watermark = PdfReader(watermark_file)
        writer = PdfWriter()

        for page in reader.pages:
            page.merge_page(watermark.pages[0])
            writer.add_page(page)

        with open(output_file, 'wb') as output:
            writer.write(output)
