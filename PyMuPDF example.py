#!/usr/bin/env python

import fitz

# Open the PDF file
doc = fitz.open("PyMuPDF example.pdf")

# Get the first page of the document
page = doc[0]

#### BEÑAT BLACKLINE TEXT ####

# Define the area to be redacted
rect = fitz.Rect(133.01550874920002, 87.82992395007999, 163.929577416, 94.73601638912)

# Create a redaction annotation with black color fill
page.add_redact_annot(rect, fill=(0, 0, 0))

#### BUSTAMANTE BLACKLINE TEXT ####

# Define the area to be redacted
rect = fitz.Rect(163.85502549240002, 87.91132582719999, 219.9595896564, 94.70768072959999)

# Create a redaction annotation with black color fill
page.add_redact_annot(rect, fill=(0, 0, 0))

#### BEÑAT BLACKLINE IMAGE ####

# Define the area to be redacted
rect = fitz.Rect(138.41771032320003, 165.5578356256, 169.47409023600002, 172.7324736032)

# Create a redaction annotation with black color fill
page.add_redact_annot(rect, fill=(0, 0, 0))

#### BUSTAMANTE BLACKLINE IMAGE ####

# Define the area to be redacted
rect = fitz.Rect(169.3404766152, 165.70278057279998, 226.11229924800003, 172.525437056)

# Create a redaction annotation with black color fill
page.add_redact_annot(rect, fill=(0, 0, 0))

# Apply the redactions to the page
page.apply_redactions()

# Save the modified PDF file
doc.save('PyMuPDF example blacklined.pdf')