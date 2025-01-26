import os
import cv2
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def convert_png_to_hdr(input_png_paths, output_directory, upscale_factor=1.0):
    """Convert PNG files to HDR with optional upscaling."""
    for input_png_path in input_png_paths:
        # Read the PNG file
        png_image = cv2.imread(input_png_path, cv2.IMREAD_UNCHANGED)
        if png_image is None:
            messagebox.showerror("Error", f"Cannot read file: {input_png_path}")
            continue

        # Upscale by factor
        if upscale_factor != 1.0:
            original_height, original_width = png_image.shape[:2]
            new_width = int(original_width * upscale_factor)
            new_height = int(original_height * upscale_factor)
            png_image = cv2.resize(png_image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

        # Save the HDR file
        file_name = os.path.splitext(os.path.basename(input_png_path))[0] + ".hdr"
        output_hdr_path = os.path.join(output_directory, file_name)
        cv2.imwrite(output_hdr_path, png_image)
        print(f"Saved HDR: {output_hdr_path}")
    
    messagebox.showinfo("Success", f"Converted {len(input_png_paths)} files to HDR!")


def select_png_files():
    """Open a dialog to select PNG files and perform the conversion."""
    # Get selected options
    upscale_enabled = upscale_checkbox_var.get()
    upscale_factor = float(upscale_factor_var.get()) if upscale_enabled else 1.0

    # Select files
    input_png_paths = filedialog.askopenfilenames(
        title="Select PNG Files",
        filetypes=[("PNG Files", "*.png")],
    )
    if not input_png_paths:
        return

    # Perform the conversion
    output_directory = os.path.expanduser("~/Desktop")
    convert_png_to_hdr(input_png_paths, output_directory, upscale_factor)


def show_help():
    """Display help instructions and credits."""
    help_text = (
        "Instructions:\n"
        "- Set options (e.g., upscale factor) before selecting files.\n"
        "- Click 'Select PNG Files' to choose files to convert.\n"
        "- The converted HDR files will be saved to your Desktop.\n\n"
        "Developed by: Mitchell Cohen\n"
        "Newton, MA. 2025.\n"
        "www.mitchellcohen.net"
    )
    messagebox.showinfo("Help", help_text)


# Main UI
root = tk.Tk()
root.title("PNG to HDR Converter")

# Add an icon (optional)
icon_path = "icon.ico"  # Replace with your icon path
try:
    root.iconbitmap(icon_path)
except:
    pass

# Instruction Label
instructions = tk.Label(root, text="Convert PNG to HDR (Saved on Desktop)", pady=10)
instructions.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Upscale Checkbox and Dropdown
upscale_checkbox_var = tk.BooleanVar(value=False)
upscale_checkbox = tk.Checkbutton(root, text="Enable Upscaling", variable=upscale_checkbox_var)
upscale_checkbox.grid(row=1, column=0, sticky="w", padx=10)

upscale_factor_var = tk.StringVar(value="1.0")
upscale_factor_dropdown = ttk.Combobox(root, textvariable=upscale_factor_var, state="readonly", width=10)
upscale_factor_dropdown["values"] = ["0.5", "1.0", "1.5", "2.0", "2.5", "3.0"]
upscale_factor_dropdown.grid(row=1, column=1, sticky="w", padx=10)
upscale_factor_dropdown.current(1)  # Default to 1.0x

# Buttons
select_button = tk.Button(root, text="Select PNG Files", command=select_png_files, width=20)
select_button.grid(row=2, column=0, columnspan=2, pady=10)

help_button = tk.Button(root, text="?", command=show_help, width=5)
help_button.grid(row=3, column=0, columnspan=2, pady=5)

root.mainloop()
