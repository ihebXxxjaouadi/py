import PyPDF2
import re
import pandas as pd

# Open the PDF file and read its content
with open('cv.pdf', 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    num_pages = len(pdf_reader.pages)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()

# Define regular expressions for extracting name, email, and phone number
name_regex = r"([A-Z][a-z]+[\s|-][A-Z][a-z]+)"
email_regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
phone_regex = r"(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"

# Extract name, email, and phone number from the text
name_match = re.search(name_regex, text)
if name_match:
    name = name_match.group(0)
else:
    name = 'N/A'
email_match = re.search(email_regex, text)
if email_match:
    email = email_match.group(0)
else:
    email = 'N/A'
phone_match = re.search(phone_regex, text)
if phone_match:
    phone = phone_match.group(0)
else:
    phone = 'N/A'

# Normalize the data and store it in a pandas DataFrame
data = {'Name': [name], 'Email': [email], 'Phone': [phone]}
df = pd.DataFrame(data)

# Print the normalized data
print(df)
