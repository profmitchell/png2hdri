import os
import cv2
import streamlit as st


def convert_png_to_hdr(input_png_paths, output_directory, upscale_factor=1.0):
    """Convert PNG files to HDR with optional upscaling."""
    for input_png_path in input_png_paths:
        png_image = cv2.imread(input_png_path, cv2.IMREAD_UNCHANGED)
        if png_image is None:
            st.error(f"Cannot read file: {input_png_path}")
            continue

        if upscale_factor != 1.0:
            original_height, original_width = png_image.shape[:2]
            new_width = int(original_width * upscale_factor)
            new_height = int(original_height * upscale_factor)
            png_image = cv2.resize(png_image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

        file_name = os.path.splitext(os.path.basename(input_png_path))[0] + ".hdr"
        output_hdr_path = os.path.join(output_directory, file_name)
        cv2.imwrite(output_hdr_path, png_image)
        st.success(f"Saved HDR: {output_hdr_path}")


# Streamlit App
st.title("PNG to HDR Converter")
st.write("Modern, minimal UI. Converted files are saved to your Desktop.")

# Upscaling Options
enable_upscale = st.checkbox("Enable Upscaling")
upscale_factor = st.selectbox("Upscale Factor", ["0.5x", "1x", "1.5x", "2x", "2.5x", "3x"], index=1)
upscale_factor = float(upscale_factor.replace("x", "")) if enable_upscale else 1.0

# File Upload
uploaded_files = st.file_uploader("Upload PNG Files", accept_multiple_files=True, type=["png"])

if st.button("Convert to HDR"):
    if uploaded_files:
        output_directory = os.path.expanduser("~/Desktop")
        for uploaded_file in uploaded_files:
            input_png_path = uploaded_file.name
            with open(input_png_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            convert_png_to_hdr([input_png_path], output_directory, upscale_factor)
        st.success("Conversion completed!")
    else:
        st.error("Please upload at least one PNG file.")
