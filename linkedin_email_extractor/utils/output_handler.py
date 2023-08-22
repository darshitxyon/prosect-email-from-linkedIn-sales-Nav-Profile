```python
import os

def write_output(union_emails, output_file):
    """
    Function to write the extracted emails and metadata to a text file.
    """
    if not os.path.exists(os.path.dirname(output_file)):
        try:
            os.makedirs(os.path.dirname(output_file))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(output_file, 'w') as f:
        for email_data in union_emails:
            f.write(f"Email: {email_data['email']}\n")
            f.write(f"Metadata: {email_data['metadata']}\n")
            f.write("\n")

    print(f"Extraction completed. Check the output file at {output_file}")
```