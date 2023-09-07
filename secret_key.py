import os
import base64

# Generate a 256-bit secret key
secret_key = base64.b64encode(os.urandom(32)).decode('utf-8')
print(secret_key)