# PDF Manager Application
A desktop application for PDF manipulation using PyQt6 and PyPDF2.

## Libraries Used
- **PyQt6**: GUI framework
- **PyPDF2**: PDF manipulation library

## Features
- Merge multiple PDFs
- Split PDF into separate pages
- Rotate PDF pages
- Extract text from PDF
- Add watermark to PDF

## Installation
```bash
pip install -r requirements.txt
```

## Retrospective Report

### 1. Planned Tasks
Using PyQt6:
- Create a responsive desktop application
- Implement user-friendly interface
- Handle file dialogs and user interactions
- Display operation status messages

Using PyPDF2:
- Implement PDF manipulation operations
- Handle PDF file reading and writing
- Manage PDF content modifications

### 2. Library Choice Rationale
**PyQt6:**
- Well-established GUI framework
- Rich feature set
- Cross-platform compatibility
- Good documentation and community support
- Modern and actively maintained

**PyPDF2:**
- Pure Python library (no external dependencies)
- Comprehensive PDF manipulation capabilities
- Active development and maintenance
- Simple and straightforward API

### 3. Installation and Setup Experience
Both libraries were straightforward to install via pip:
```bash
pip install PyQt6 PyPDF2
```
No additional configuration was required. PyQt6 automatically handles platform-specific requirements.

### 4. Documentation Quality
**PyQt6:**
- Comprehensive official documentation
- Numerous tutorials and examples available
- Well-organized class hierarchy
- Clear method descriptions

**PyPDF2:**
- Clear API documentation
- Good examples for basic operations
- Some advanced features could use better documentation
- Active GitHub discussions for complex cases

### 5. Library Usage Understanding
**PyQt6 Classes Used:**
- QMainWindow: Main application window
- QWidget: Base widget class
- QVBoxLayout: Vertical layout manager
- QPushButton: Button widgets
- QFileDialog: File selection dialogs
- QMessageBox: Status/error messages

**PyPDF2 Classes Used:**
- PdfReader: Reading PDF files
- PdfWriter: Writing PDF files
- PdfMerger: Merging PDF files

The implementation process was logical and followed object-oriented principles.

### 6. Usage Convenience
**PyQt6:**
- Required boilerplate code is minimal
- Layout system is intuitive
- Event handling is straightforward

**PyPDF2:**
- Clean and simple API
- Direct methods for common operations
- Minimal code required for basic tasks

### 7. Behavior Predictability
**PyQt6:**
- Consistent behavior across platforms
- Clear error messages
- Predictable event handling

**PyPDF2:**
- Reliable for basic operations
- Some edge cases with complex PDFs
- Clear error handling

### 8. Integration Experience
The integration between PyQt6 and PyPDF2 was smooth:
- PyQt6 handles UI and user interaction
- PyPDF2 processes PDF operations
- Clean separation of concerns
- Easy error handling and status reporting

### 9. Encountered Issues
1. PDF Rotation:
   - Issue: Rotation angles limited to 90-degree increments
   - Solution: Added validation for rotation angles

2. Memory Usage:
   - Issue: Large PDF files consumption
   - Solution: Implemented proper file handling and cleanup

### 10. Positive Aspects
**PyQt6:**
- Modern and professional-looking UI
- Excellent performance
- Rich widget set
- Good development tools

**PyPDF2:**
- Simple and efficient API
- Good performance
- Reliable for basic operations
- Active maintenance

### 11. Negative Aspects
**PyQt6:**
- Steep learning curve for beginners
- Large package size
- Documentation can be overwhelming

**PyPDF2:**
- Limited advanced PDF features
- Some operations can be slow with large files
- Inconsistent behavior with some PDF formats

### 12. Future Improvements
Would consider:
- Using async operations for large files
- Adding progress bars for long operations
- Implementing better error handling
- Adding preview functionality
- Using PyMuPDF for more advanced features

## Resources Used
1. [PyQt6 Official Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
   - Primary resource for GUI implementation
   - Very helpful for widget usage

2. [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
   - Essential for PDF operations
   - Good code examples

3. [Stack Overflow](https://stackoverflow.com/)
   - Helpful for specific implementation issues
   - Community solutions for common problems

4. [Real Python PyQt Tutorials](https://realpython.com/qt-designer-python/)
   - Excellent for understanding PyQt concepts
   - Practical examples