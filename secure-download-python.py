import bcrypt
import time

# Mock file database
files = {
    "file123": {
        "path": "uploads/demo.txt",
        "password": bcrypt.hashpw(b"admin123", bcrypt.gensalt()),
        "expiry_time": time.time() + 300  # expires in 5 minutes
    }
}

def verify_download(file_id, input_password):
    file = files.get(file_id)

    if not file:
        return "❌ File not found"

    # Check expiry
    if time.time() > file["expiry_time"]:
        return "❌ Link expired"

    # Check password
    if bcrypt.checkpw(input_password.encode(), file["password"]):
        return f"✅ Access granted. File ready: {file['path']}"
    else:
        return "❌ Incorrect password"


# Test cases
print(verify_download("file123", "admin123"))  # correct
print(verify_download("file123", "wrongpass"))  # incorrect
