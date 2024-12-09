from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QPushButton, 
                            QFileDialog, QLabel, QMessageBox)
from PyQt6.QtCore import Qt
from core.pdf_operations import PDFOperations

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Manager")
        self.setMinimumSize(800, 600)
        self.pdf_ops = PDFOperations()
        self.setup_ui()

    def setup_ui(self):
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create title label
        title = QLabel("PDF Manager")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; margin: 20px;")
        layout.addWidget(title)

        # Create buttons
        merge_btn = QPushButton("Merge PDFs")
        split_btn = QPushButton("Split PDF")
        rotate_btn = QPushButton("Rotate PDF")
        extract_btn = QPushButton("Extract Text")
        watermark_btn = QPushButton("Add Watermark")

        # Add buttons to layout
        layout.addWidget(merge_btn)
        layout.addWidget(split_btn)
        layout.addWidget(rotate_btn)
        layout.addWidget(extract_btn)
        layout.addWidget(watermark_btn)

        # Connect buttons to functions
        merge_btn.clicked.connect(self.merge_pdfs)
        split_btn.clicked.connect(self.split_pdf)
        rotate_btn.clicked.connect(self.rotate_pdf)
        extract_btn.clicked.connect(self.extract_text)
        watermark_btn.clicked.connect(self.add_watermark)

    def merge_pdfs(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select PDF files to merge",
            "",
            "PDF files (*.pdf)"
        )
        if files:
            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save merged PDF",
                "",
                "PDF files (*.pdf)"
            )
            if save_path:
                try:
                    self.pdf_ops.merge_pdfs(files, save_path)
                    QMessageBox.information(self, "Success", "PDFs merged successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error merging PDFs: {str(e)}")

    def split_pdf(self):
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Select PDF file to split",
            "",
            "PDF files (*.pdf)"
        )
        if file:
            save_dir = QFileDialog.getExistingDirectory(
                self,
                "Select directory to save split PDFs"
            )
            if save_dir:
                try:
                    self.pdf_ops.split_pdf(file, save_dir)
                    QMessageBox.information(self, "Success", "PDF split successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error splitting PDF: {str(e)}")

    def rotate_pdf(self):
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Select PDF file to rotate",
            "",
            "PDF files (*.pdf)"
        )
        if file:
            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save rotated PDF",
                "",
                "PDF files (*.pdf)"
            )
            if save_path:
                try:
                    self.pdf_ops.rotate_pdf(file, save_path)
                    QMessageBox.information(self, "Success", "PDF rotated successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error rotating PDF: {str(e)}")

    def extract_text(self):
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Select PDF file to extract text",
            "",
            "PDF files (*.pdf)"
        )
        if file:
            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save extracted text",
                "",
                "Text files (*.txt)"
            )
            if save_path:
                try:
                    self.pdf_ops.extract_text(file, save_path)
                    QMessageBox.information(self, "Success", "Text extracted successfully!")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"Error extracting text: {str(e)}")

    def add_watermark(self):
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Select PDF file to watermark",
            "",
            "PDF files (*.pdf)"
        )
        if file:
            watermark_file, _ = QFileDialog.getOpenFileName(
                self,
                "Select watermark PDF",
                "",
                "PDF files (*.pdf)"
            )
            if watermark_file:
                save_path, _ = QFileDialog.getSaveFileName(
                    self,
                    "Save watermarked PDF",
                    "",
                    "PDF files (*.pdf)"
                )
                if save_path:
                    try:
                        self.pdf_ops.add_watermark(file, watermark_file, save_path)
                        QMessageBox.information(self, "Success", "Watermark added successfully!")
                    except Exception as e:
                        QMessageBox.critical(self, "Error", f"Error adding watermark: {str(e)}")
