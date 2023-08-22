```python
import re
from typing import List, Dict

def extract_emails_from_text(text: str) -> List[str]:
    """
    Extracts emails from the given text using regex.
    """
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_regex, text)

def extract_emails_from_metadata(metadata: Dict) -> List[str]:
    """
    Extracts emails from the given metadata.
    """
    emails = []
    for key, value in metadata.items():
        if key == 'email':
            emails.append(value)
        elif isinstance(value, str):
            emails.extend(extract_emails_from_text(value))
        elif isinstance(value, dict):
            emails.extend(extract_emails_from_metadata(value))
    return emails
```