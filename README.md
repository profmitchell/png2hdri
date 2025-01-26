
# PNG to HDR Converter

<img width="406" alt="Screenshot 2025-01-25 at 11 35 42 PM" src="https://github.com/user-attachments/assets/ffd56373-f66b-4a98-9acc-69eb37470b65" />
<img width="692" alt="Screenshot 2025-01-25 at 11 36 10 PM" src="https://github.com/user-attachments/assets/cf2f2ab1-0a1f-4349-b0c8-cf1560f6dbb3" />

This repository provides two Python applications to convert PNG images into HDR format with optional upscaling. Both a **Tkinter GUI version** and a **Streamlit modern web-based version** are included for flexibility and ease of use.

## Features

- **Convert PNG to HDR**: Save HDR files directly to your Desktop.
- **Batch Processing**: Select multiple PNG files for conversion.
- **Upscaling Options**: Enable optional upscaling with predefined factors (`0.5x`, `1x`, `1.5x`, `2x`, etc.).
- **Tkinter GUI**:
  - Robust, compact UI with a checkbox and dropdown for upscaling.
  - Help button with instructions and credits.
- **Streamlit Version**:
  - Modern and minimalistic web-based UI.
  - Streamlined workflow for selecting files and options.

## Installation

### Prerequisites

1. Python 3.8+
2. Required Python libraries:
   ```bash
   pip install opencv-python pillow streamlit
   ```

### Files

- `png_to_hdr_tkinter.py`: Tkinter-based GUI version.
- `png_to_hdr_streamlit.py`: Streamlit-based modern version.

### Optional Icon

To add a custom icon to the Tkinter application, ensure the icon file (`icon.png`) is located at:
```
/Users/mitchellcohen/Desktop/icon.png
```

## Usage

### Tkinter Version

1. Run the application:
   ```bash
   python png_to_hdr_tkinter.py
   ```
2. Use the GUI to select options and files.

#### Packaging as Executable
To package the Tkinter version as a standalone executable:
```bash
pyinstaller --onefile --windowed --icon=/Users/mitchellcohen/Desktop/icon.png png_to_hdr_tkinter.py
```
The packaged file will be in the `dist/` folder.

### Streamlit Version

1. Run the application:
   ```bash
   streamlit run png_to_hdr_streamlit.py
   ```
2. Open the provided localhost link in your browser.

#### Packaging as Executable
To package the Streamlit version as a standalone executable:
```bash
pyinstaller --onefile png_to_hdr_streamlit.py
```

## Features Walkthrough

### Tkinter UI
- **Upscaling Options**: Enable upscaling with a checkbox and select the scale factor (`0.5x`, `1x`, `1.5x`, etc.) using a dropdown menu.
- **Help Button**: Displays instructions and credits.
- **File Selection**: Use the "Select PNG Files" button to choose files.
- **Batch Processing**: Select multiple files at once for conversion.

### Streamlit UI
- **Drag and Drop**: Upload PNG files via the drag-and-drop interface.
- **Upscaling Options**: Enable upscaling with a checkbox and select the scale factor.
- **Modern Design**: Minimal and responsive web-based interface.

## Credits

Developed by **Mitchell Cohen**
Newton, MA, 2025

Visit: [www.mitchellcohen.net](http://www.mitchellcohen.net)

## License

This project is licensed under the MIT License. See the LICENSE file for details.


