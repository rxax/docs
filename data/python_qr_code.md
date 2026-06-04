## QR Code

Prerequisites:

```python
pip install pillow
pip install qrcode
```

Usage:

```python
import qrcode

# Link for website
input_data = "http://localhost:5000/members/register"

# Save QR Code image to file
image = qrcode.make(input_data)
image.save('qrcode_image.png')
```