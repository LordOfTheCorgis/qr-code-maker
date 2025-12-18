# QR Code Generator

A simple desktop application to generate QR codes from URLs and save them as PNG images.

## Features

- Enter a URL and generate a QR code
- Save the QR code as a PNG file
- Custom window and taskbar icon

## Usage

1. Download the `qr_app.exe` from the [Releases](https://github.com/LordOfTheCorgis/qr-code-maker/releases/tag/Official) page.
2. Open the application.
3. Enter a URL and click **Generate QR Code**.
4. Click **Save QR Code** to save the image.

## Source Code

The Python source code is available in this repository. You can run it using Python 3 with the required dependencies:

```bash
pip install qrcode[pil] pillow
python qr_app.py
